|Maturity| |Build Status| |license gpl| |Coverage Status| |Codecov Status| |OCA project| |Tech Doc| |Help| |Try Me|

.. |icon| image:: https://raw.githubusercontent.com/Odoo-Italia-Associazione/oia11/11.0/l10n_it_rea/static/description/icon.png

===================
|icon| REA Register
===================

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
| /opt/odoo/11.0/oia11/l10n_it_rea                               |
+----------------------------------------------------------------------------+

|

::

    pip install Babel==2.3.4
    pip install decorator==4.0.10
    pip install docutils==0.12
    pip install ebaysdk==2.1.5
    pip install feedparser==5.2.1
    pip install gevent==1.1.2 ; sys_platform != 'win32'
    pip install greenlet==0.4.10
    pip install html2text==2016.9.19
    pip install Jinja2==2.8
    pip install lxml==3.7.1 ; sys_platform != 'win32'
    pip install lxml ; sys_platform == 'win32'
    pip install Mako==1.0.4
    pip install MarkupSafe==0.23
    pip install mock==2.0.0
    pip install num2words==0.5.4
    pip install ofxparse==0.16
    pip install passlib==1.6.5
    pip install phonenumbers
    pip install Pillow==4.0.0
    pip install psutil==4.3.1; sys_platform != 'win32'
    pip install psycopg2==2.7.3.1; sys_platform != 'win32'
    pip install pydot==1.2.3
    pip install pyldap==2.4.28; sys_platform != 'win32'
    pip install pyparsing==2.1.10
    pip install PyPDF2==1.26.0
    pip install pyserial==3.1.1
    pip install python-dateutil==2.5.3
    pip install pytz==2016.7
    pip install pyusb==1.0.0
    pip install PyYAML==3.12
    pip install qrcode==5.3
    pip install reportlab==3.3.0
    pip install requests==2.11.1
    pip install suds-jurko==0.6
    pip install vatnumber==1.2
    pip install vobject==0.9.3
    pip install Werkzeug==0.11.15
    pip install XlsxWriter==0.9.3
    pip install xlwt==1.3.*
    pip install xlrd==1.0.0
    pip install pypiwin32 ; sys_platform == 'win32'
    cd $HOME
    git clone https://github.com/zeroincombenze/tools.git
    cd ./tools
    ./install_tools.sh -p
    export PATH=$HOME/dev:$PATH
    odoo_install_repository oia11 -b 11.0 -O oia


From UI: go to:

|menu| Setting > Activate Developer mode 

|menu| Apps > Update Apps List

|menu| Setting > Apps |right_do| Select **l10n_it_rea** > Install

|warning| If your Odoo instance crashes, you can do following instruction
to recover installation status:

``run_odoo_debug 11.0 -um l10n_it_rea -s -d MYDB``








Known issues / Roadmap
=======================

|warning| Questo modulo rimpiazza il modulo OCA. Leggete attentamente il
paragrafo relativo alle funzionalità e differenze.





Issue Tracker
==============

Bug reports are welcome! You can use the issue tracker to report bugs,
and/or submit pull requests on `GitHub Issues
<https://github.com/Odoo-Italia-Associazione/oia11/issues>`_.

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
.. |Build Status| image:: https://travis-ci.org/Odoo-Italia-Associazione/oia11.svg?branch=11.0
    :target: https://travis-ci.org/Odoo-Italia-Associazione/oia11
    :alt: github.com
.. |license gpl| image:: https://img.shields.io/badge/licence-LGPL--3-7379c3.svg
    :target: http://www.gnu.org/licenses/lgpl-3.0-standalone.html
    :alt: License: LGPL-3
.. |Coverage Status| image:: https://coveralls.io/repos/github/Odoo-Italia-Associazione/oia11/badge.svg?branch=11.0
    :target: https://coveralls.io/github/Odoo-Italia-Associazione/oia11?branch=11.0
    :alt: Coverage
.. |Codecov Status| image:: https://codecov.io/gh/Odoo-Italia-Associazione/oia11/branch/11.0/graph/badge.svg
    :target: https://codecov.io/gh/Odoo-Italia-Associazione/oia11/branch/11.0
    :alt: Codecov
.. |OCA project| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-oca-11.svg
    :target: https://github.com/OCA/oia11/tree/11.0
    :alt: OCA
.. |Tech Doc| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-11.svg
    :target: https://wiki.zeroincombenze.org/en/Odoo/11.0/dev
    :alt: Technical Documentation
.. |Help| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-11.svg
    :target: https://wiki.zeroincombenze.org/it/Odoo/11.0/man
    :alt: Technical Documentation
.. |Try Me| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-11.svg
    :target: https://odoo11.odoo-italia.org
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
   

