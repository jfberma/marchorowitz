marchorowitz.net
================

The psuedo-crypto-currency-based art store of Marc Horowitz

## Background

marchorowitz.net is a Django 1.6 app that is managed by Supervisor and configured to be served by nginx. The site features a custom psuedo-crypto-currency called hCoin. The site contains a store (django_shop app) that is customized to accept hCoin as payment instead of dollars. The value of hCoin is determined by Marc's mood.

marchorowitz.net is hosted on TODO

## Operation

Pretty much every aspect of marchorowitz.net can be managed via the [admin](https://www.marchorowitz.net/admin/)

#### The Store

##### Pieces

To add/remove/edit items that are on sale, navigate to [Pieces](https://www.marchorowitz.net/admin/project/piece/) section of the admin. Here you can edit/remove any of the existing peices, or add a new one. When adding, you will have to enter all of the appropriate details such as title, price in hCoin and an image. 

From the [pieces](https://www.marchorowitz.net/admin/project/piece/) overview page, you also have the ability to change the order in which the pieces appear on the site by clicking on the up and down arrows in the order column.

##### Piece Categories

Each piece requires an assigned category. Cateogies are represented by color and determine where the item shows up on the site (i.e. [blue](https://www.marchorowitz.net/pieces/blue/) or [grey](https://www.marchorowitz.net/pieces/grey/)).

To view all of the categories, visit the [piece categorys](https://www.marchorowitz.net/admin/project/piececategory/) page (Djano auto-appends an "s" to the page name, hense the funny spelling). From here, you can add and edit categories. Each category has a name, a Hex Color Value (the color that will show up in the site navigation), and a top and bottom hex color used to determine the gradient for the background of that category.

