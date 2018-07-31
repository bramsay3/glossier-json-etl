# Glossier-JSON-ETL

This was a homework assignment to take order information in the form of JSON messages and put them into a postgreSQL database so that it would be availbe to be querried. Additional information was extracted from the order information to provide summary metrics that business analysts would find useful.


# Methodology

## Formatting the data

There are two main ways of storing this informaiton in a PostgreSQL database. Either parse the JSON input and create tables that are linked with primary key forign key pairs, or store the data in JSON format.

In the JSON format each order apears to come wholisticly meaning that the data for each order is self contained needing minimal addition contexual information.Additionally, much of the information in each order serves as logistical information needed to make sure that the customer's order is fufilled. Once the order is completed, many of the fields, with the exception of a select few, will no longer be relavent to future operations minimizes the need for robust queries.

This pushes a document store mentality where the orders are all stored in JSON format where important fields are indexed and extracted for use in other capacities.

## PostgreSQL JSON

Storing data using RDBMS grants great querying capabilites but PostreSQL has devolped a robust set of commands to interface with JSON data allowing for comparable queriying capabilies and performance.

### JSON vs JSONB

JSON format files may be represented in either an text form(JSON) or a binary form(JSONB). Each form has tradeoffs. JSON is slightly fast for insertions than JSONB since JSONB has the overhead of needing to be converted from text to binary. However JSONB is faster for querying and comes with some added functionality to check subsets that pure text JSON doesn't have.

The time to insert the data is not as important as the ability to query quicky considering that the inserts would happen daily where queries might be needed in real time. This pushed twoards using JSONB format.

## User Data

As instructed we were to queary the orders for summary metrics that business analysts would find usful. I settled on calculating the following for every user:
*total products bought
*total purchases made
*amount of money spent
*products bought per purchase
*money spent per purchase

These fields were stored along with the user_ID so that they may be joined with any user information contained in on ther relational tables involving user_ID

## Running Daily

This code could be easily be used to take the orders from the day and enter them into the database granted that they extracted in a similar manner to how they were given to us here. Should other queries be desired to support a BI team then those could be written to run everyday as well.







