#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of Neo4j.
# https://github.com/josl/neo4j-02807

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Jose L. Bellod Cisneros <bellod.cisneros@gmail.com>

from Neo4j import session

'''
Determine how many and who has ordered "Uncle Bob’s Organic Dried Pears"
(productID 7).
'''


def ex3():
    productID = 7
    query = '''
            MATCH (p:Product {productID: '7'}),
                  (p:Product)<-[:ORDERS]-(o:Order)<-[:PURCHASED]-(c:Customer)
            RETURN DISTINCT c.contactName as Customer, count(c)
    ''' % productID

    query = '''
              MATCH
                (p:Product {productID: '7'}),
                (p)<-[:ORDERS]-(o:Order)<-[:PURCHASED]-(c:Customer)
              RETURN DISTINCT c.contactName as Customer
        UNION
              MATCH
                (p:Product {productID: '7'}),
                (p)<-[:ORDERS]-(o:Order)<-[:PURCHASED]-(c:Customer)
              WITH DISTINCT c.customerID as number_number
              RETURN count(number_number) as Customer
    '''
    #
    # ╒═══════════════════╕
    # │Customer           │
    # ╞═══════════════════╡
    # │Paula Wilson       │
    # ├───────────────────┤
    # │Carlos González    │
    # ├───────────────────┤
    # │Ann Devon          │
    # ├───────────────────┤
    # │Maria Larsson      │
    # ├───────────────────┤
    # │Horst Kloss        │
    # ├───────────────────┤
    # │Yvonne Moncada     │
    # ├───────────────────┤
    # │Elizabeth Lincoln  │
    # ├───────────────────┤
    # │Roland Mendel      │
    # ├───────────────────┤
    # │Maurizio Moroni    │
    # ├───────────────────┤
    # │Victoria Ashworth  │
    # ├───────────────────┤
    # │Daniel Tonini      │
    # ├───────────────────┤
    # │Laurence Lebihan   │
    # ├───────────────────┤
    # │Jonas Bergulfsen   │
    # ├───────────────────┤
    # │André Fonseca      │
    # ├───────────────────┤
    # │Henriette Pfalzheim│
    # ├───────────────────┤
    # │Jose Pavarotti     │
    # ├───────────────────┤
    # │Martine Rancé      │
    # ├───────────────────┤
    # │Palle Ibsen        │
    # ├───────────────────┤
    # │Mary Saveley       │
    # ├───────────────────┤
    # │Art Braunschweiger │
    # └───────────────────┘

    result = session.run(query)
    for record in result:
        print(record)

    session.close()
