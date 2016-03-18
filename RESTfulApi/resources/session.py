#!/usr/bin/env python
# encoding: utf-8

"""
    File name: session.py
    Function Des: ...
    ~~~~~~~~~~
    
    author: Jerry <cuteuy@gmail.com> <http://www.skyduy.com>
    
"""
from flask.ext.restful import Resource, marshal_with

from RESTfulApi.handler.session import login, logout
from RESTfulApi.common.parsers import login_parser, token_parser
from RESTfulApi.common.fields import token_fields


class Session(Resource):
    @marshal_with(token_fields)
    def post(self):
        login_args = login_parser.parse_args()
        result = login(login_args.username, login_args.password)
        return result

    def delete(self):
        token = token_parser.parse_args().token
        return logout(token)



