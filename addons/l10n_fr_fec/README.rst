[![Build Status](https://travis-ci.org/Odoo-Italia-Associazione/OCB.svg?branch=10.0)](https://travis-ci.org/Odoo-Italia-Associazione/OCB)
[![license lgpl](https://img.shields.io/badge/licence-LGPL--3-7379c3.svg)](https://www.gnu.org/licenses/lgpl.html)
[![Coverage Status](https://coveralls.io/repos/github/Odoo-Italia-Associazione/OCB/badge.svg?branch=10.0)](https://coveralls.io/github/Odoo-Italia-Associazione/OCB?branch=10.0)
[![codecov](https://codecov.io/gh/Odoo-Italia-Associazione/OCB/branch/10.0/graph/badge.svg)](https://codecov.io/gh/Odoo-Italia-Associazione/OCB/branch/10.0)
[![OCA_project](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-oca-10.svg)](https://github.com/OCA/OCB/tree/10.0)
[![Tech Doc](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-10.svg)](http://wiki.zeroincombenze.org/en/Odoo/10.0/dev)
[![Help](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-10.svg)](http://wiki.zeroincombenze.org/en/Odoo/10.0/man/)
[![try it](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-10.svg)](http://erp10.zeroincombenze.it)


[![en](http://www.shs-av.com/wp-content/en_US.png)](http://wiki.zeroincombenze.org/it/Odoo/7.0/man)

Fichier d'Échange Informatisé (FEC) pour la France
==================================================

Ce module permet de générer le fichier FEC tel que définit par `l'arrêté du 29
Juillet 2013 <http://legifrance.gouv.fr/eli/arrete/2013/7/29/BUDE1315492A/jo/texte>`
portant modification des dispositions de l'article A. 47 A-1 du
livre des procédures fiscales.

Cet arrêté prévoit l'obligation pour les sociétés ayant une comptabilité
informatisée de pouvoir fournir à l'administration fiscale un fichier
regroupant l'ensemble des écritures comptables de l'exercice. Le format de ce
fichier, appelé *FEC*, est définit dans l'arrêté.

Le détail du format du FEC est spécifié dans le bulletin officiel des finances publiques `BOI-CF-IOR-60-40-20-20131213 <http://bofip.impots.gouv.fr/bofip/ext/pdf/createPdfWithAnnexePermalien/BOI-CF-IOR-60-40-20-20131213.pdf?doc=9028-PGP&identifiant=BOI-CF-IOR-60-40-20-20131213>` du 13 Décembre 2013. Ce module implémente le fichier
FEC au format texte et non au format XML, car le format texte sera facilement
lisible et vérifiable par le comptable en utilisant un tableur.

La structure du fichier FEC généré par ce module a été vérifiée avec le logiciel
*Test Compta Demat* version 1_00_05 disponible sur
`le site de la direction générale des finances publiques <http://www.economie.gouv.fr/dgfip/outil-test-des-fichiers-des-ecritures-comptables-fec>`
en utilisant une base de donnée Odoo réelle.

Installation
------------

Configuration
-------------

Aucune configuration n'est nécessaire.

Utilisation

Pour générer le *FEC*, allez dans le menu *Accounting > Reporting > French Statements > FEC* qui va démarrer l'assistant de génération du FEC.

Usage
-----

Known issues / Roadmap
----------------------

Bug Tracker
-----------

Credits
-------

### Contributors

* Alexis de Lattre <alexis.delattre@akretion.com>

[//]: # (copyright)

----

**Odoo** is a trademark of [Odoo S.A.](https://www.odoo.com/) (formerly OpenERP, formerly TinyERP)

**OCA**, or the [Odoo Community Association](http://odoo-community.org/), is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

**Odoo Italia Associazione**, or the [Associazione Odoo Italia](https://www.odoo-italia.org/)
is the nonprofit Italian Community Association whose mission
is to support the collaborative development of Odoo designed for Italian law and markeplace.
Since 2017, Odoo Italia Associazione replaces OCA members of Italy are developping code under Odoo Proprietary License.
Odoo Italia Associazione distributes only code under AGPL free license.

[Odoo Italia Associazione](https://www.odoo-italia.org/) è un'Associazione senza fine di lucro
che dal 2017 sostituisce gli sviluppatori italiani di OCA che sviluppano
con Odoo Proprietary License a pagamento.

Odoo Italia Associazione distribuisce il codice esclusivamente con licenza [AGPL](https://www.gnu.org/licenses/agpl-3.0.html) o [LGPL](https://www.gnu.org/licenses/lgpl.html)

[//]: # (end copyright)



[![chat with us](https://www.shs-av.com/wp-content/chat_with_us.gif)](https://tawk.to/85d4f6e06e68dd4e358797643fe5ee67540e408b)
