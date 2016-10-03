#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of Neo4j.
# https://github.com/josl/neo4j-02807

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Jose L. Bellod Cisneros <bellod.cisneros@gmail.com>

from Neo4j import session

'''
The customer with customerID ALFKI has made a number of orders containing some
products. Return orders made by ALFKI that contain at least 2 products.

Also return the products.
'''


def ex3():
    productID = 'ALFKI'
    query = '''
        MATCH (c:Customer)-[:PURCHASED]->(o:Order)-[:ORDERS]->(p:Product) WHERE
            c.customerID = 'ALFKI'
        RETURN o.orderID as Order, p.productName as Product,
               count(p) AS numberOfProducts
    ''' % productID



    result = session.run(query)
    for record in result:
        print(record)


    session.close()
