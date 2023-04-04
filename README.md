# Usage & Connection
## Connection:
IP address of the app: https://e-commerce-y2q1.onrender.com
## Usage:
There is exists 3 type usage type which depend user type.
#### Anonymous user
The anonymous user is not login the site. Thus, the user only reach:
* /												: The main page contains all items and a category filter
* /login										: The login page for log in with credentials.
* /item?name=<item_name>	: The item page contains information of related item and its comments.

#### Regular user
The regular user is log in the site without admin permissions. Therefore, the user only capable with rating and reviewing any item, reach itself profile page, display its all reviews and ratings and be able to delete and overwrite them. The regular user can reach all pages are reached by anonymous user and additionally:
* /profile									: The logged in user can display itself name, average rating and all ratings and reviews were given by itself. Also the user can delete ratings/reviews or navigate related item with click a comment.
* /logout									:  Logs out and redirect main page
##### List of regular users: 
| name | password |
|--|--|
| Cringe User | cloud495 |
| Shopping Freak | cloud495 |
| Unknown | cloud495 |
| Flora | cloud495 |

#### Admin user
The admin user can The admin user can reach all pages are reached by regular user and additionally:
* /panel										:  The panel is core component of the app. Any regular users and any items can be created and deleted via panel.  The user creation is straight-forward, the admin clicks + (plus) button and gives credentials. Then save it. The item creation depends category selection. The admin should select a category and should fill all fields. There is not exists any validation for simplicity nor password encryption for sake of simplicity. The only criteria is 'name' field which is used as primary key in all application. The admin can delete an item or an user, also.
##### List of admin users: 
| name | password |
|--|--|
| Admin | cloud495 |



# Design Choices
## App sctructure
In this homework, a basic stack was chosen for construct the e-commerce app for sake of simplicity. The stack consists of Flask, Mongo, Python and pure HTML-CSS-JS. 

## Database structure
The MongoDB is a NoSQL database system. Its structure depents documents, collections and databases. In the assignment, there is exists 3 collections for:
* Users
* Items
* Comments

The aim about database structure is grouping similar objects in same collections.

### Other design decisions:
* The password is stored in clear text format for simplicity.
* The `name` field is used as primary key in collection Users and Items.
* The `item` field in Comments collection implies `name` field in Items collection.
* The `user` field in Comments collection implies `name` field in Users collection

