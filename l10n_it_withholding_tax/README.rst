|Maturity| |Build Status| |license gpl| |Coverage Status| |Codecov Status| |OCA project| |Tech Doc| |Help| |Try Me|

.. |icon| image:: https://raw.githubusercontent.com/Odoo-Italia-Associazione/oia8/8.0/l10n_it_withholding_tax/static/description/icon.png

==============================
|icon| Italian Withholding Tax
==============================

.. contents::


|en|



|it|






|en|


Installation / Installazione
=============================

+---------------------------------+------------------------------------------+
| |en|                            | |it|                                     |
+---------------------------------+------------------------------------------+
| These instruction are just an   | Istruzioni di esempio valide solo per    |
| example to remember what        | distribuzioni Linux CentOS 7, Ubuntu 14+ |
| you have to do on Linux.        | e Debian 8+                              |
|                                 |                                          |
| Installation is based on:       | L'installazione è basata su:             |
+---------------------------------+------------------------------------------+
| `Zeroincombenze Tools <https://github.com/zeroincombenze/tools>`__         |
+---------------------------------+------------------------------------------+
| Suggested deployment is         | Posizione suggerita per l'installazione: |
+---------------------------------+------------------------------------------+
| /opt/odoo/8.0/oia8/l10n_it_withholding_tax                               |
+----------------------------------------------------------------------------+

|

::

    pip install Babel==1.3
    pip install Jinja2==2.7.3
    pip install Mako==1.0.0
    pip install MarkupSafe==0.23
    pip install Pillow==2.5.1
    pip install Python-Chart==1.39
    pip install PyYAML==3.11
    pip install Werkzeug==0.9.6
    pip install argparse==1.2.1
    pip install decorator==3.4.0
    pip install docutils==0.12
    pip install feedparser==5.1.3
    pip install gdata==2.0.18
    pip install gevent==1.0.2
    pip install greenlet==0.4.7
    pip install jcconv==0.2.3
    pip install lxml==3.3.5
    pip install mock==1.0.1
    pip install passlib==1.6.2
    pip install psutil==2.1.1
    pip install psycogreen==1.0
    pip install psycopg2-binary==2.7.4
    pip install pyPdf==1.13
    pip install pydot==1.0.2
    pip install pyparsing==1.5.7
    pip install pyserial==2.7
    pip install python-dateutil==1.5
    pip install python-ldap==2.4.15
    pip install python-openid==2.2.5
    pip install pytz==2014.4
    pip install qrcode==5.0.1
    pip install reportlab==3.1.44
    pip install requests==2.6.0
    pip install simplejson==3.5.3
    pip install six==1.7.3
    pip install unittest2==0.5.1
    pip install vatnumber==1.2
    pip install vobject==0.6.6
    pip install wsgiref==0.1.2
    pip install xlwt==0.7.5
    pip install unidecode
    pip install python-stdnum
    pip install suds
    pip install requests
    pip install unicodecsv
    pip install xlsxwriter
    pip install xlwt
    pip install python-ldap
    pip install validate_email
    pip install acme_tiny
    pip install IPy
    pip install pydot
    pip install pysftp
    pip install serial
    pip install qrcode
    pip install evdev
    pip install python-openid
    pip install ipwhois
    pip install python-dateutil
    pip install pytz
    pip install pyth
    pip install paramiko
    pip install codicefiscale
    pip install cups
    pip install pyusb>=1.0.0b1
    pip install pyxb==1.2.4
    cd $HOME
    git clone https://github.com/zeroincombenze/tools.git
    cd ./tools
    ./install_tools.sh -p
    export PATH=$HOME/dev:$PATH
    odoo_install_repository oia8 -b 8.0 -O oia


From UI: go to:

|menu| Setting > Modules > Update Modules List

|menu| Setting > Local Modules |right_do| Select **l10n_it_withholding_tax** > Install

|warning| If your Odoo instance crashes, you can do following instruction
to recover installation status:

``run_odoo_debug 8.0 -um l10n_it_withholding_tax -s -d MYDB``








Known issues / Roadmap
=======================

|warning| Questo modulo rimpiazza il modulo OCA. Leggete attentamente il
paragrafo relativo alle funzionalità e differenze.





Issue Tracker
==============

Bug reports are welcome! You can use the issue tracker to report bugs,
and/or submit pull requests on `GitHub Issues
<https://github.com/Odoo-Italia-Associazione/oia8/issues>`_.

In case of trouble, please check there if your issue has already been reported.


Proposals for enhancement
--------------------------

If you have a proposal to change this module, you may want to send an email to
<moderatore@odoo-italia.org> for initial feedback.
An Enhancement Proposal may be submitted if your idea gains ground.






Credits
========

Authors
--------

* `SHS-AV s.r.l. <https://www.zeroincombenze.it/>`__

Contributors
-------------

* Antonio Maria Vigliotti <antoniomaria.vigliotti@gmail.com>

Maintainers
------------

|Odoo Italia Associazione|

This module is maintained by the Odoo Italia Associazione.

To contribute to this module, please visit https://odoo-italia.org/.




----------------

**Odoo** is a trademark of `Odoo S.A. <https://www.odoo.com/>`__
(formerly OpenERP)

**OCA**, or the `Odoo Community Association <http://odoo-community.org/>`__,
is a nonprofit organization whose mission is to support
the collaborative development of Odoo features and promote its widespread use.

**Odoo Italia Associazione**, or the `Associazione Odoo Italia <https://www.odoo-italia.org/>`__
is the nonprofit Italian Community Association whose mission
is to support the collaborative development of Odoo designed for Italian law and markeplace.
Since 2017 Odoo Italia Associazione issues modules for Italian localization not developed by OCA
or available only with Odoo Proprietary License.
Odoo Italia Associazione distributes code under `AGPL <https://www.gnu.org/licenses/agpl-3.0.html>`__
or `LGPL <https://www.gnu.org/licenses/lgpl.html>`__ free license.

`Odoo Italia Associazione <https://www.odoo-italia.org/>`__ è un'Associazione senza fine di lucro
che dal 2017 rilascia moduli per la localizzazione italiana non sviluppati da OCA
o disponibili solo con `Odoo Proprietary License <https://www.odoo.com/documentation/user/9.0/legal/licenses/licenses.html>`__

Odoo Italia Associazione distribuisce il codice esclusivamente con licenza `AGPL <https://www.gnu.org/licenses/agpl-3.0.html>`__
o `LGPL <https://www.gnu.org/licenses/lgpl.html>`__



|

Last Update / Ultimo aggiornamento: 2018-10-19

.. |Maturity| image:: https://img.shields.io/badge/maturity-Alfa-red.png
    :target: https://odoo-community.org/page/development-status
    :alt: Alfa
.. |Build Status| image:: https://travis-ci.org/Odoo-Italia-Associazione/oia8.svg?branch=8.0
    :target: https://travis-ci.org/Odoo-Italia-Associazione/oia8
    :alt: github.com
.. |license gpl| image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |Coverage Status| image:: https://coveralls.io/repos/github/Odoo-Italia-Associazione/oia8/badge.svg?branch=8.0
    :target: https://coveralls.io/github/Odoo-Italia-Associazione/oia8?branch=8.0
    :alt: Coverage
.. |Codecov Status| image:: https://codecov.io/gh/Odoo-Italia-Associazione/oia8/branch/8.0/graph/badge.svg
    :target: https://codecov.io/gh/Odoo-Italia-Associazione/oia8/branch/8.0
    :alt: Codecov
.. |OCA project| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-oca-8.svg
    :target: https://github.com/OCA/oia8/tree/8.0
    :alt: OCA
.. |Tech Doc| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-8.svg
    :target: https://wiki.zeroincombenze.org/en/Odoo/8.0/dev
    :alt: Technical Documentation
.. |Help| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-8.svg
    :target: https://wiki.zeroincombenze.org/it/Odoo/8.0/man
    :alt: Technical Documentation
.. |Try Me| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-8.svg
    :target: https://odoo8.odoo-italia.org
    :alt: Try Me
.. |Odoo Italia Associazione| image:: https://www.odoo-italia.org/images/Immagini/Odoo%20Italia%20-%20126x56.png
   :target: https://odoo-italia.org
   :alt: Odoo Italia Associazione
.. |en| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/flags/en_US.png
   :target: https://www.facebook.com/groups/openerp.italia/
.. |it| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/flags/it_IT.png
   :target: https://www.facebook.com/groups/openerp.italia/
.. |check| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/check.png
.. |no_check| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/no_check.png
.. |menu| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/menu.png
.. |right_do| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/right_do.png
.. |exclamation| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/exclamation.png
.. |warning| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/warning.png
.. |xml_schema| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/certificates/iso/icons/xml-schema.png
   :target: https://raw.githubusercontent.com/zeroincombenze/grymbcertificates/iso/scope/xml-schema.md
.. |DesktopTelematico| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/certificates/ade/icons/DesktopTelematico.png
   :target: https://raw.githubusercontent.com/zeroincombenze/grymbcertificates/ade/scope/DesktopTelematico.md
.. |FatturaPA| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/certificates/ade/icons/fatturapa.png
   :target: https://raw.githubusercontent.com/zeroincombenze/grymbcertificates/ade/scope/fatturapa.md
   

