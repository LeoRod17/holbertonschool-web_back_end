#!/usr/bin/env python3
"""a Python function that returns all students sorted by average score:"""


def top_students(mongo_collection):
    """The average score must be part of each item returns with key
    = averageScore"""
    collection = mongo_collection.find({})
    