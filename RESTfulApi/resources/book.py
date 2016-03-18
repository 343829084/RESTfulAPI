#!/usr/bin/env python
# encoding: utf-8

"""
    File name: book.py
    Function Des: ...
    ~~~~~~~~~~
    
    author: Jerry <cuteuy@gmail.com> <http://www.skyduy.com>
    
"""
from flask.ext.restful import Resource, request, marshal_with

from RESTfulApi.handler.book import get_all_books, create_book
from RESTfulApi.handler.book import get_book_by_id, get_books, rm_book, update_book
from RESTfulApi.common.parsers import book_parser, book_update_parser, token_parser
from RESTfulApi.common.fields import book_fields, books_fields


class Books(Resource):
    @marshal_with(books_fields)
    def get(self):
        token = token_parser.parse_args().token
        args = request.args
        if args:
            books = get_books(args, token=token)
        else:
            books = get_all_books(token=token)
        return {'books': books}

    @marshal_with(book_fields)
    def post(self):
        token = token_parser.parse_args().token
        book_args = book_parser.parse_args(token=token)
        book = create_book(book_args.name, book_args.price, book_args.count, book_args.des, token=token)
        return book


class Book(Resource):
    @marshal_with(book_fields)
    def get(self, book_id):
        token = token_parser.parse_args().token
        return get_book_by_id(book_id, token=token)

    @marshal_with(book_fields)
    def put(self, book_id):
        token = token_parser.parse_args().token
        book_args = book_update_parser.parse_args(token=token)
        book = update_book(book_id, book_args.delta, book_args.price, book_args.des, book_args.types, token=token)
        return book

    def delete(self, book_id):
        """
        :param book_id:
        :return: 0失败， 1 成功
        """
        token = token_parser.parse_args().token
        return rm_book(book_id, token=token)
