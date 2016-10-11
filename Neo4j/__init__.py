#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of Neo4j.
# https://github.com/josl/neo4j-02807

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Jose L. Bellod Cisneros <bellod.cisneros@gmail.com>

from Neo4j.version import __version__  # NOQA

from neo4j.v1 import GraphDatabase, basic_auth

driver = GraphDatabase.driver(
    "bolt://localhost", auth=basic_auth("neo4j", "neo4j"))
session = driver.session()
