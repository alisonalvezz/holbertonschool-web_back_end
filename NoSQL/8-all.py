#!/usr/bin/env python3
"""
List all in MongoDB
"""

def list_all(mongo_collection):
    """
    List all
    """
    doc = []
    for _ in mongo_collection.find():
        doc.append(_)
    return doc
