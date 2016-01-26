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

If an item is **active** it will appear on the site.

If an item is not maked as **sold** it will be available for purchase.

From the [pieces](https://www.marchorowitz.net/admin/project/piece/) overview page, you also have the ability to change the order in which the pieces appear on the site by clicking on the up and down arrows in the order column.

##### Piece Categories

Each piece requires an assigned category. Cateogies are represented by color and determine where the item shows up on the site (i.e. [blue](https://www.marchorowitz.net/pieces/blue/) or [grey](https://www.marchorowitz.net/pieces/grey/)).

To view all of the categories, visit the [piece categorys](https://www.marchorowitz.net/admin/project/piececategory/) page (Djano auto-appends an "s" to the page name, hense the funny spelling). From here, you can add and edit categories. Each category has a name, a Hex Color Value (the color that will show up in the site navigation), and a top and bottom hex color used to determine the gradient for the background of that category.

##### Purchase Flow

* Logged in user adds item to their cart
* If user has sufficient hCoin, they will be presented with a checkout button. If not they will be prompted to buy more hCoin
* When a user clicks "CHECKOUT", they will be asked for their shipping address
* The user will then enter their info and click "SUBMIT"
* hCoin will then be transfered from that user back to the main account (marc.horowitz)
* Upon success, the user and marc.horowitz will receive emails confirming the transaction

**NOTE:** An item is NOT marked sold automatically. This was done upon request so that Marc could verify the purchase himself. The item needs to be manaully marked as sold (check the "sold" box).
