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

            MATCH (c:Customer)-[:PURCHASED]->(o:Order)-[:ORDERS]->(p:Product)
            WHERE c.customerID = 'ALFKI'
            WITH o.orderID as OrderID, collect(p.productName) as Products
            WHERE Products >= 2
            RETURN *
            RETURN ALFKI_Order, Products
    ''' % productID

    # ╒═════╤══════════════════════════════╕
    # │Order│Products                      │
    # ╞═════╪══════════════════════════════╡
    # │10952│[Grandma's Boysenberry Spread,│
    # │     │ Rössle Sauerkraut]           │
    # ├─────┼──────────────────────────────┤
    # │10643│[Chartreuse verte, Spegesild, │
    # │     │Rössle Sauerkraut]            │
    # ├─────┼──────────────────────────────┤
    # │10835│[Raclette Courdavault, Origina│
    # │     │l Frankfurter grüne Soße]     │
    # ├─────┼──────────────────────────────┤
    # │11011│[Escargots de Bourgogne, Flote│
    # │     │mysost]                       │
    # ├─────┼──────────────────────────────┤
    # │10692│[Vegie-spread]                │
    # ├─────┼──────────────────────────────┤
    # │10702│[Aniseed Syrup, Lakkalikööri] │
    # └─────┴──────────────────────────────┘

    query = '''
        MATCH (c:Customer {customerID: 'ALFKI'}),
              (c:Customer)-[:PURCHASED]->(o:Order)-[:ORDERS]->(p:Product)
        RETURN o.orderID as Order, count(p) as nProducts
    '''

    result = session.run(query)
    for record in result:
        print(record)

    session.close()
