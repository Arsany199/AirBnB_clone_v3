#!/usr/bin/python3
"""Index module"""
from api.v1.views import app_views
from flask import jsonify
from models import storage

@app_views.route('/api/v1/stats', methods=['GET'])
def get_stats():
    """ Retrieves the number of objects"""
    stats = {
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User")
    }
    return jsonify(stats)
