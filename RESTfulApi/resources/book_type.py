#!/usr/bin/env python
# encoding: utf-8

"""
    File name: book_type.py
    Function Des: ...
    ~~~~~~~~~~
    
    author: Jerry <cuteuy@gmail.com> <http://www.skyduy.com>
    
"""

from flask.ext.restful import Resource, request, marshal_with

from RESTfulApi.handler.book_type import get_all_types, create_book_type
from RESTfulApi.handler.book_type import get_book_type_by_id, get_book_types, rm_book_type
from RESTfulApi.common.parsers import book_type_parser, token_parser
from RESTfulApi.common.fields import book_type_fields, book_types_fields


class BookTypes(Resource):
    @marshal_with(book_types_fields)
    def get(self):
        token = token_parser.parse_args().token
        args = request.args
        if args:
            books_types = get_book_types(args, token=token)
        else:
            books_types = get_all_types(token=token)
        return {'books_types': books_types}

    @marshal_with(book_type_fields)
    def post(self):
        token = token_parser.parse_args().token
        book_args = book_type_parser.parse_args()
        book_type = create_book_type(book_args.name, token=token)
        return book_type


class BookType(Resource):
    @marshal_with(book_type_fields)
    def get(self, book_type_id):
        token = token_parser.parse_args().token
        return get_book_type_by_id(book_type_id, token=token)

    def delete(self, book_type_id):
        """
        :param book_type_id:
        :return: 0失败， 1 成功
        """
        token = token_parser.parse_args().token
        return rm_book_type(book_type_id, token=token)


