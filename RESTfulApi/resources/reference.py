#!/usr/bin/env python
# encoding: utf-8

"""
    File name: reference.py
    Function Des: ...
    ~~~~~~~~~~
    
    author: Jerry <cuteuy@gmail.com> <http://www.skyduy.com>
    
"""
from flask.ext.restful import Resource, marshal_with
from RESTfulApi.common.fields import books_fields, sales_records_fields
from RESTfulApi.common.parsers import token_parser
from RESTfulApi.handler.reference import get_books_by_type, rm_ref_book2type
from RESTfulApi.handler.reference import get_sales_records_by_account, get_sales_records_by_book, get_sales_records_by_vip


class ReferenceBook2Type(Resource):
    @marshal_with(books_fields)
    def get(self, book_type_id):
        token = token_parser.parse_args().token
        books = get_books_by_type(book_type_id, token=token)
        return {'books': books}

    def delete(self, book_type_id):
        token = token_parser.parse_args().token
        return rm_ref_book2type(book_type_id, token=token)


class ReferenceSaleRecord2Account(Resource):
    @marshal_with(sales_records_fields)
    def get(self, account_id):
        token = token_parser.parse_args().token
        sales_records = get_sales_records_by_account(account_id, token=token)
        return {'sales_records': sales_records}


class ReferenceSaleRecord2Book(Resource):
    @marshal_with(sales_records_fields)
    def get(self, book_id):
        token = token_parser.parse_args().token
        sales_records = get_sales_records_by_book(book_id, token=token)
        return {'sales_records': sales_records}


class ReferenceSale2Vip(Resource):
    @marshal_with(sales_records_fields)
    def get(self, vip_id):
        token = token_parser.parse_args().token
        sales_records = get_sales_records_by_vip(vip_id, token=token)
        return {'sales_records': sales_records}

