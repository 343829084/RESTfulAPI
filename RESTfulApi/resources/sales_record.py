#!/usr/bin/env python
# encoding: utf-8

"""
    File name: sales_record.py
    Function Des: ...
    ~~~~~~~~~~

    author: Jerry <cuteuy@gmail.com> <http://www.skyduy.com>

"""
from flask.ext.restful import Resource, marshal_with

from RESTfulApi.handler.sales_record import get_all_sales_records
from RESTfulApi.handler.sales_record import get_sales_record_by_id, create_sales_record
from RESTfulApi.common.parsers import sales_record_parser, token_parser
from RESTfulApi.common.fields import sales_record_fields, sales_records_fields


class SalesRecords(Resource):
    @marshal_with(sales_records_fields)
    def get(self):
        token = token_parser.parse_args().token
        sales_records = get_all_sales_records(token=token)
        return {'sales_records': sales_records}

    @marshal_with(sales_record_fields)
    def post(self):
        token = token_parser.parse_args().token
        sales_args = sales_record_parser.parse_args()
        sales_record = create_sales_record(sales_args.count, sales_args.seller_id,
                                           sales_args.book_id, sales_args.purchaser_id, token=token)
        return sales_record


class SalesRecord(Resource):
    @marshal_with(sales_record_fields)
    def get(self, sales_record_id):
        token = token_parser.parse_args().token
        return get_sales_record_by_id(sales_record_id, token=token)

