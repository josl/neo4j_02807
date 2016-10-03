# WEEK 06: GRAPH DATABASES

Exercise 6 of 02807 Computational Tools for Big Data at DTU

## Content:

This week will be about Graph Databases which is a database model particularly suited for storing and working with network/relational/graph-data. We will introduce the graph database Neo4j and the query language Cypher.

## Learning objectives:

After this week, you are supposed to know:

- What a graph database is
- How to set up and use Neo4j
- How to query Neo4j using the Cypher query language

## Resources:

- Watch Emil Eifrem (Founder of Neo4j) give a quick explanation of Neo4j: https://www.youtube.com/watch?v=Sjjcm93N6gU
- Reading: The Neo4j manual has a good description of Graph Database Concepts and the specifics of Neo4j. The included tutorials give a good understanding on how to modify and search in a graph.

## Exercises:

For each of the exercises 6.2 to 6.7: Show both the result (either as a graph or as a number if relevant) and give the Cypher query/queries to answer it.

### Exercise 6.1:

Go to GraphStory.com and make a new account (you get 14 days for free). Create a graph database. Go to the Neo4j Web UI for your new graph. Log in with the autogenerated username and password from Graph Story.

Start by removing all the data by running the following Cypher query:

MATCH (n)-[r]-() WHERE ID(n)>=0 DELETE n;

Now load the data into the database using the code given here: http://pastebin.com/raw.php?i=4VFY4a2b (this should be done in multiple commands, a new one every time there is a double line break).

If you don’t want to use GraphStory.com, you can install Neo4j on your own machine or use a different service.

### Exercise 6.2:

The customer with customerID ALFKI has made a number of orders containing some products. Return all the orders made by ALFKI and the products they contain.

### Exercise 6.3:

The customer with customerID ALFKI has made a number of orders containing some products. Return orders made by ALFKI that contain at least 2 products. Also return the products.

### Exercise 6.4:

Determine how many and who has ordered “Uncle Bob’s Organic Dried Pears” (productID 7).

### Exercise 6.5:

How many different and which products have been ordered by customers who have also ordered “Uncle Bob’s Organic Dried Pears”?
## Install

It's recommended to create a virtual environment (conda env preffered)
``` bash
make setup
```
## Usage



# Unit test
``` bash
make unit
```


## License
MIT © [Jose Luis Bellod Cisneros](http://josl.github.io)
