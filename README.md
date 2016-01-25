marchorowitz.net
================

The psuedo-crypto-currency-based art store of Marc Horowitz

## Background

marchorowitz.net is a Django 1.6 app that is managed by Supervisor and configured to be served by nginx. The site features a custom psuedo-crypto-currency called hCoin. The site contains a store (django_shop app) that is customized to accept hCoin as payment instead of dollars. The value of hCoin is determined by Marc's mood.

marchorowitz.net is hosted on TODO

## Operation

Pretty much every aspect of marchorowitz.net can be managed via the [admin](https://www.marchorowitz.net/admin/)

#### The Store

To add/remove/edit items that are on sale, navigate to [Pieces](https://www.marchorowitz.net/admin/project/piece/) section of the admin. Here you can edit/remove and of the existing peices, or add a new one. 
