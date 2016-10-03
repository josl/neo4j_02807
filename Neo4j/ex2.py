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
products. Return all the orders made by ALFKI and the products they contain.
'''


def ex2():
    productID = 'ALFKI'
    query = '''
        MATCH (c:Customer)-[:PURCHASED]->(o:Order)-[:ORDERS]->(p:Product) WHERE
            c.customerID = 'ALFKI'
        RETURN collect(o.orderID) as Order, p.productName as Product
    ''' % productID

    # ╒═════╤══════════════════════════════╕
    # │Order│Product                       │
    # ╞═════╪══════════════════════════════╡
    # │11011│Escargots de Bourgogne        │
    # ├─────┼──────────────────────────────┤
    # │11011│Flotemysost                   │
    # ├─────┼──────────────────────────────┤
    # │10952│Grandma's Boysenberry Spread  │
    # ├─────┼──────────────────────────────┤
    # │10952│Rössle Sauerkraut             │
    # ├─────┼──────────────────────────────┤
    # │10835│Raclette Courdavault          │
    # ├─────┼──────────────────────────────┤
    # │10835│Original Frankfurter grüne Soß│
    # │     │e                             │
    # ├─────┼──────────────────────────────┤
    # │10702│Aniseed Syrup                 │
    # ├─────┼──────────────────────────────┤
    # │10702│Lakkalikööri                  │
    # ├─────┼──────────────────────────────┤
    # │10692│Vegie-spread                  │
    # ├─────┼──────────────────────────────┤
    # │10643│Chartreuse verte              │
    # ├─────┼──────────────────────────────┤
    # │10643│Spegesild                     │
    # ├─────┼──────────────────────────────┤
    # │10643│Rössle Sauerkraut             │
    # └─────┴──────────────────────────────┘

    result = session.run(query)
    for record in result:
        print(record)

    # <Record Order='11011' Product='Escargots de Bourgogne'>
    # <Record Order='11011' Product='Flotemysost'>
    # <Record Order='10952' Product="Grandma's Boysenberry Spread">
    # <Record Order='10952' Product='Rössle Sauerkraut'>
    # <Record Order='10835' Product='Raclette Courdavault'>
    # <Record Order='10835' Product='Original Frankfurter grüne Soße'>
    # <Record Order='10702' Product='Aniseed Syrup'>
    # <Record Order='10702' Product='Lakkalikööri'>
    # <Record Order='10692' Product='Vegie-spread'>
    # <Record Order='10643' Product='Chartreuse verte'>
    # <Record Order='10643' Product='Spegesild'>
    # <Record Order='10643' Product='Rössle Sauerkraut'>

    session.close()
