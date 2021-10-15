from flask import Flask, Response, request
import database_services.RDBService as d_service
from flask_cors import CORS
import json

import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()
logger.setLevel(logging.INFO)

from application_services.orders import OrderResource
from application_services.UsersResource.user_service import UserResource

app = Flask(__name__)
CORS(app)

@app.route('/')
def initial_page():
    return '<u>Micro Service for Orders!</u>'

@app.route('/orders')
def get_users():
    res = OrderResource.get_by_template(None)
    rsp = Response(json.dumps(res, default=str), status=200, content_type="application/json")
    return rsp

@app.route('/orders/<prefix>', methods = ['POST', 'GET','DELETE','UPDATE'])
def order_id(prefix):
    if request.method == 'GET':
        res = OrderResource.get_by_order_id(prefix)
        rsp = Response(json.dumps(res), status=200, content_type="application/json")
        return rsp
    elif request.method == 'POST':
        generate_row = OrderResource.create_by_order_id(prefix)
        res = OrderResource.get_by_order_id(prefix)
        rsp = Response(json.dumps(res), status=200, content_type="application/json")
        return rsp


@app.route('/<db_schema>/<table_name>/<column_name>/<prefix>')
def get_by_prefix(db_schema, table_name, column_name, prefix):
    res = d_service.get_by_prefix(db_schema, table_name, column_name, prefix)
    rsp = Response(json.dumps(res, default=str), status=200, content_type="application/json")
    return rsp


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
