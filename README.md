marchorowitz.net
================

The psuedo-crypto-currency-based art store of Marc Horowitz

## Background

marchorowitz.net is a Django 1.6 app that is managed by Supervisor and configured to be served by nginx. The site features a custom psuedo-crypto-currency called hCoin. The site contains a store (django_shop app) that is customized to accept hCoin as payment instead of dollars. The value of hCoin is determined by Marc's mood.

## Contents
* [Operation](#operation)
    [The Store](#the-store)

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

##### Orders

You can view all of the orders by visiting the [orders](https://www.marchorowitz.net/admin/shop/order/) page. Click on an order to view it's details (user, address, date, etc.). You can also change the order's status (to "shipped" for example).

#### hCoin

##### Coins

* There are 3,000,000 hCoin. 
* Each coin has one owner. 
* Each coin was originally owned by marc.horowitz
* When a purchase is made, hCoins are transfered from a user back to marc.horowitz
* There are two main ways for a user to acquire hCoin: Mining and buying

##### Mining hCoin

A user can "mine" for hCoin by clicking on the pick icon in the site nav. By doing so, they will be presented with a game of snake. The user will be awarded with an hCoin once they reach a certain amount of points.

The amount of points per hCoin is configurable through [Coin Settings](https://www.marchorowitz.net/admin/coin/coinsettings/) page. To change the points-per-coin, simply edit the **Points per Coin** column in the existing row.

##### Buying hCoin

A user can also purhcase hCoin. When a user purchases hCoin the dollar amount is calculated based on the current value of hCoin and taken through the [Stripe](https://stripe.com/) checkout procedure. Marc can monitor these purchases via the Stripe dashboard.

##### Transaction

Everytime a coin changes owner (eg. during a purchase or while mining) a Transaction is recorded. A list of every transaction can be found on the [Transactions](https://www.marchorowitz.net/admin/coin/transaction/) page. 

Ad hoc transactions can be made on this page by on this page by clickin the "Add transaction" button.

##### hCoin Value

The value of a single hCoin is effected by three different "influencers":

* Mood
* Productivity
* Sales

hCoin value is calculated by looking at the day-over-day difference of the influencers and multiplying those values by a "weight" which is set in [Coin Settings](https://www.marchorowitz.net/admin/coin/coinsettings/):

```
hCoinValueToday = hCoinValueYesterday + (((MoodToday - MoodYesterday) * MoodWeight) + ((ProdToday - ProdYesterday) * ProdWeight) + ((SalesToday - SalesYesterday) * SalesWeight))
```

Changing an influencers weight will change how much effect that influencer has over the price of hCoin.

Influencers were designed to be updated everyday, but if a day is missed a cron job will automatically apply yesterday's values to today.

To enter new influencer, go to the [Coin stats](https://www.marchorowitz.net/admin/coin/coinstat/) page in the admin and click **Add coin stat**. Enter your influencer values. You can also add a description. Hit save and return to the Coin stats page. You can see the new value of hCoin here. Likewise, you can visit the [about](https://www.marchorowitz.net/about/) section of the site to see the current version of hCoin.

#### Deep Web Site

The deep web portion of the marchorowitz project is a light-weight, basic gallery. Because of the nature (and speed) of the deep web, we have kept this area as optimized and simple as possible. Thus, there is no real backend. To update this page, simply upload a JPG via FTP to the designated directory (details below)

* Open your favorite FTP client (such as Cyberduck on OSX).
* Connect to server **54.175.58.254** with the username **marc** and password **\*H0r0w1tz***
* If you have issues connecting, make sure the **Connect Mode** is set to **Active (PORT)**
* Once inside, go into the site directory, and then into the pieces directory.
* Any image uploaded to this folder will display on the site (NOTE: MUST BE JPG)
* The images will appear on the site in ascending alphabetical order based on the file name. (ie. Simcor-Horowitz-January2014-001.jpg will appear before Simcor-Horowitz-January2014-002.jpg)

## Development

marchorowitz.net is... 
* A [Django](https://www.djangoproject.com/) app with a [postgresql](http://www.postgresql.org/) database
* Serverd by [nginx](https://www.nginx.com/resources/wiki/), using [wsgi](http://wsgi.readthedocs.org/en/latest/).
* Hosted on 2 EC2 micro instances (one for main site, one for deep web) at [AWS](https://aws.amazon.com)





