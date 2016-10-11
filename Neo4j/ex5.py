#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of Neo4j.
# https://github.com/josl/neo4j-02807

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Jose L. Bellod Cisneros <bellod.cisneros@gmail.com>

from Neo4j import session

'''
How many different and which products have been ordered by customers who have
also ordered "Uncle Bob’s Organic Dried Pears"?
'''


def ex3():
    productID = 7
    query = '''
            MATCH (p:Product)<-[:ORDERS]-(o:Order)<-[:PURCHASED]-(c:Customer)
            WHERE p.productID = '7'
            WITH DISTINCT c.customerID as Customers_7
            MATCH (c:Customer)-[:PURCHASED]->(o:Order)-[:ORDERS]->(p:Product)
            WHERE c.customerID in Customers_7
            RETURN DISTINCT p.productName as Product
    ''' % productID

    result = session.run(query)
    for record in result:
        print(record)

    session.close()

    # ╒══════════════════════════════╕
    # │Product                       │
    # ╞══════════════════════════════╡
    # │Grandma's Boysenberry Spread  │
    # ├──────────────────────────────┤
    # │Chef Anton's Cajun Seasoning  │
    # ├──────────────────────────────┤
    # │Northwoods Cranberry Sauce    │
    # ├──────────────────────────────┤
    # │Uncle Bob's Organic Dried Pear│
    # │s                             │
    # ├──────────────────────────────┤
    # │Aniseed Syrup                 │
    # ├──────────────────────────────┤
    # │Chang                         │
    # ├──────────────────────────────┤
    # │Pavlova                       │
    # ├──────────────────────────────┤
    # │Sir Rodney's Marmalade        │
    # ├──────────────────────────────┤
    # │Tunnbröd                      │
    # ├──────────────────────────────┤
    # │Mascarpone Fabioli            │
    # ├──────────────────────────────┤
    # │Ikura                         │
    # ├──────────────────────────────┤
    # │Queso Manchego La Pastora     │
    # ├──────────────────────────────┤
    # │Konbu                         │
    # ├──────────────────────────────┤
    # │Tofu                          │
    # ├──────────────────────────────┤
    # │Pâté chinois                  │
    # ├──────────────────────────────┤
    # │Camembert Pierrot             │
    # ├──────────────────────────────┤
    # │Wimmers gute Semmelknödel     │
    # ├──────────────────────────────┤
    # │Louisiana Hot Spiced Okra     │
    # ├──────────────────────────────┤
    # │Chartreuse verte              │
    # ├──────────────────────────────┤
    # │Jack's New England Clam Chowde│
    # │r                             │
    # ├──────────────────────────────┤
    # │Spegesild                     │
    # ├──────────────────────────────┤
    # │Filo Mix                      │
    # ├──────────────────────────────┤
    # │Original Frankfurter grüne Soß│
    # │e                             │
    # ├──────────────────────────────┤
    # │Rhönbräu Klosterbier          │
    # ├──────────────────────────────┤
    # │Röd Kaviar                    │
    # ├──────────────────────────────┤
    # │Gnocchi di nonna Alice        │
    # ├──────────────────────────────┤
    # │Chef Anton's Gumbo Mix        │
    # ├──────────────────────────────┤
    # │Tarte au sucre                │
    # ├──────────────────────────────┤
    # │Guaraná Fantástica            │
    # ├──────────────────────────────┤
    # │Queso Cabrales                │
    # ├──────────────────────────────┤
    # │Côte de Blaye                 │
    # ├──────────────────────────────┤
    # │Alice Mutton                  │
    # ├──────────────────────────────┤
    # │NuNuCa Nuß-Nougat-Creme       │
    # ├──────────────────────────────┤
    # │Schoggi Schokolade            │
    # ├──────────────────────────────┤
    # │Flotemysost                   │
    # ├──────────────────────────────┤
    # │Gorgonzola Telino             │
    # ├──────────────────────────────┤
    # │Lakkalikööri                  │
    # ├──────────────────────────────┤
    # │Perth Pasties                 │
    # ├──────────────────────────────┤
    # │Raclette Courdavault          │
    # ├──────────────────────────────┤
    # │Louisiana Fiery Hot Pepper Sau│
    # │ce                            │
    # ├──────────────────────────────┤
    # │Nord-Ost Matjeshering         │
    # ├──────────────────────────────┤
    # │Escargots de Bourgogne        │
    # ├──────────────────────────────┤
    # │Chai                          │
    # ├──────────────────────────────┤
    # │Ipoh Coffee                   │
    # ├──────────────────────────────┤
    # │Mozzarella di Giovanni        │
    # ├──────────────────────────────┤
    # │Tourtière                     │
    # ├──────────────────────────────┤
    # │Ravioli Angelo                │
    # ├──────────────────────────────┤
    # │Outback Lager                 │
    # ├──────────────────────────────┤
    # │Maxilaku                      │
    # ├──────────────────────────────┤
    # │Rössle Sauerkraut             │
    # ├──────────────────────────────┤
    # │Sir Rodney's Scones           │
    # ├──────────────────────────────┤
    # │Longlife Tofu                 │
    # ├──────────────────────────────┤
    # │Gumbär Gummibärchen           │
    # ├──────────────────────────────┤
    # │Gudbrandsdalsost              │
    # ├──────────────────────────────┤
    # │Teatime Chocolate Biscuits    │
    # ├──────────────────────────────┤
    # │Genen Shouyu                  │
    # ├──────────────────────────────┤
    # │Geitost                       │
    # ├──────────────────────────────┤
    # │Steeleye Stout                │
    # ├──────────────────────────────┤
    # │Thüringer Rostbratwurst       │
    # ├──────────────────────────────┤
    # │Manjimup Dried Apples         │
    # ├──────────────────────────────┤
    # │Vegie-spread                  │
    # ├──────────────────────────────┤
    # │Zaanse koeken                 │
    # ├──────────────────────────────┤
    # │Gustaf's Knäckebröd           │
    # ├──────────────────────────────┤
    # │Sirop d'érable                │
    # ├──────────────────────────────┤
    # │Gula Malacca                  │
    # ├──────────────────────────────┤
    # │Scottish Longbreads           │
    # ├──────────────────────────────┤
    # │Singaporean Hokkien Fried Mee │
    # ├──────────────────────────────┤
    # │Carnarvon Tigers              │
    # ├──────────────────────────────┤
    # │Boston Crab Meat              │
    # ├──────────────────────────────┤
    # │Rogede sild                   │
    # ├──────────────────────────────┤
    # │Mishi Kobe Niku               │
    # ├──────────────────────────────┤
    # │Inlagd Sill                   │
    # ├──────────────────────────────┤
    # │Valkoinen suklaa              │
    # ├──────────────────────────────┤
    # │Sasquatch Ale                 │
    # ├──────────────────────────────┤
    # │Chocolade                     │
    # ├──────────────────────────────┤
    # │Gravad lax                    │
    # └──────────────────────────────┘
