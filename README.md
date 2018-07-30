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



