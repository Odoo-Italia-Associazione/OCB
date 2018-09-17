# -*- coding: utf-8 -*-
#    Copyright (C) 2014-2018 Associazione Odoo Italia (<http://www.odoo-italia.org>)
#    Copyright (C) 2016      Andrea Gallina (Apulia Software)
#    Copyright (C) 2018      Antonio Vigliotti <https://www.zeroincombenze.it>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
#
import logging
from odoo import models, fields, api
_logger = logging.getLogger(__name__)
try:
    import codicefiscale
except ImportError as err:
    _logger.debug(err)


SPLIT_MODE = [('LF', 'Last/First'),
              ('FL', 'First/Last'),
              ('LFM', 'Last/First Middle'),
              ('L2F', 'Last last/First'),
              ('L2FM', 'Last last/First Middle'),
              ('FML', 'First middle/Last'),
              ('FL2', 'First/Last last'),
              ('FML2', 'First Middle/Last last')]


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.model
    def _commercial_fields(self):
        res = super(ResPartner, self)._commercial_fields()
        res += ['fiscalcode']
        return res

    @api.multi
    def check_fiscalcode(self):
        for partner in self:
            if not partner.fiscalcode:
                return True
            elif len(partner.fiscalcode) != 16 and partner.individual:
                return False
            else:
                return True

    @api.multi
    def _join_lastname_particle(self, fields):
        """Join most common surname particles"""
        if len(fields) > 1:
            particles = ['de', 'der', 'des', 'di', 'mc', 'van', 'von', 'zu']
            for particle in particles:
                i = [i for i, x in enumerate(fields) if x == particle]
                if i:
                    i = i[0]
                    fields[i + 1] = '%s %s' % (fields[i], fields[i + 1])
                    del fields[i]
                    break
        return fields

    @api.multi
    def _split_last_name(self):
        for partner in self:
            lastname, firstname = self._split_last_first_name(
                partner=partner)
            self.lastname = lastname

    @api.multi
    def _split_first_name(self):
        for partner in self:
            lastname, firstname = self._split_last_first_name(
                partner=partner)
            self.firstname = firstname

    @api.multi
    def _split_last_first_name(self, partner=None, name=None, splitmode=None):
        if partner:
            if not partner.individual and partner.is_company:
                return '', ''
            name = partner.name
            if not splitmode:
                if hasattr(partner, 'splitmode') and partner.splitmode:
                    splitmode = partner.splitmode
                else:
                    splitmode = self._default_splitmode()
        elif not splitmode:
            splitmode = self._default_splitmode()
        if not isinstance(name, basestring) or \
                not isinstance(splitmode, basestring):
            return '', ''
        f = self._join_lastname_particle(name.split(' '))
        if len(f) == 1:
            if splitmode[0] == 'F':
                return '', f[0]
            elif splitmode[0] == 'L':
                return f[0], ''
        elif len(f) == 2:
            if splitmode[0] == 'F':
                return f[1], f[0]
            elif splitmode[0] == 'L':
                return f[0], f[1]
        elif len(f) == 3:
            if splitmode in ('LFM', 'LF', 'L2FM'):
                return f[2], '%s %s' % (f[0], f[1])
            elif splitmode in ('FML', 'FL', 'FML2'):
                return '%s %s' % (f[0], f[1]), f[2]
            elif splitmode == 'L2F':
                return '%s %s' % (f[0], f[1]), f[2]
            elif splitmode == 'FL2':
                return '%s %s' % (f[1], f[2]), f[0]
        else:
            if splitmode[0] == 'F':
                return '%s %s' % (f[2], f[3]), '%s %s' % (f[0], f[1])
            elif splitmode[0] == 'L':
                return '%s %s' % (f[0], f[1]), '%s %s' % (f[2], f[3])
        return '', ''

    fiscalcode = fields.Char(
        'Fiscal Code', size=16, help="Italian Fiscal Code")
    individual = fields.Boolean(
        'Individual', default=False,
        help="If checked the C.F. is referred to a Individual Person")
    splitmode = fields.Selection(SPLIT_MODE,
                                 'First Last format',
                                 default='LF')
    firstname = fields.Char('First Name',
                            compute='_split_first_name',
                            store=True,
                            readonly=True)
    lastname = fields.Char('Last Name',
                           compute='_split_last_name',
                           store=True,
                           readonly=True)
    split_next = fields.Boolean(
        'First<->Last',
        default=False,
        help="Check for change first/last name format")

    _constraints = [
        (check_fiscalcode,
         "The fiscal code doesn't seem to be correct.", ["fiscalcode"])
    ]


    @api.onchange('fiscalcode')
    def onchange_fiscalcode(self):
        name = 'fiscalcode'
        if self.fiscalcode:
            if self.country_id and self.country_id.code != 'IT':
                self.individual = True
            elif len(self.fiscalcode) == 11:
                res_partner_model = self.env['res.partner']
                chk = res_partner_model.simple_vat_check('it', self.fiscalcode)
                if not chk:
                    return {'value': {name: False},
                            'warning': {
                        'title': 'Invalid fiscalcode!',
                        'message': 'Invalid vat number'}
                    }
                self.individual = False
            elif len(self.fiscalcode) != 16:
                return {'value': {name: False},
                        'warning': {
                    'title': 'Invalid len!',
                    'message': 'Fiscal code len must be 11 or 16'}
                }
            else:
                self.fiscalcode = self.fiscalcode.upper()
                chk = codicefiscale.control_code(self.fiscalcode[0:15])
                if chk != self.fiscalcode[15]:
                    value = self.fiscalcode[0:15] + chk
                    return {'value': {name: value},
                            'warning': {
                                'title': 'Invalid fiscalcode!',
                                'message': 'Fiscal code could be %s' % (value)}
                            }
                self.individual = True
        self.individual = False

    @api.onchange('name')
    def onchange_name(self):
        lastname, firstname = self._split_last_first_name(
            name=self.name, splitmode=self.splitmode)
        self.firstname = firstname
        self.lastname = lastname
        self.split_next = False

    @api.onchange('splitmode')
    def onchange_splitmode(self):
        lastname, firstname = self._split_last_first_name(
            name=self.name, splitmode=self.splitmode)
        self.firstname = firstname
        self.lastname = lastname
        self.split_next = False

    @api.onchange('split_next')
    def onchange_split_next(self):
        i = [i for i, x in enumerate(SPLIT_MODE) if x[0] == self.splitmode][0]
        i = (i + 1) % len(SPLIT_MODE)
        self.splitmode = SPLIT_MODE[i][0]
        self.onchange_splitmode()

    def _default_splitmode(self):
        return 'LF'
