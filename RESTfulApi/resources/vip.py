#!/usr/bin/env python
# encoding: utf-8

"""
    File name: vip.py
    Function Des: ...
    ~~~~~~~~~~
    
    author: Jerry <cuteuy@gmail.com> <http://www.skyduy.com>
    
"""
from flask.ext.restful import Resource, request, marshal_with

from RESTfulApi.handler.vip import get_all_vips, create_vip
from RESTfulApi.handler.vip import get_vip_by_id, get_vips, rm_vip
from RESTfulApi.common.parsers import vip_parser, token_parser
from RESTfulApi.common.fields import vip_fields, vips_fields


class Vips(Resource):
    @marshal_with(vips_fields)
    def get(self):
        token = token_parser.parse_args().token
        args = request.args
        if args:
            vips = get_vips(args, token=token)
        else:
            vips = get_all_vips(token=token)
        return {'vips': vips}

    @marshal_with(vip_fields)
    def post(self):
        token = token_parser.parse_args().token
        vip_args = vip_parser.parse_args()
        vip = create_vip(vip_args.username, vip_args.nickname, vip_args.phone, token=token)
        return vip


class Vip(Resource):
    @marshal_with(vip_fields)
    def get(self, vip_id):
        token = token_parser.parse_args().token
        return get_vip_by_id(vip_id, token=token)

    def delete(self, vip_id):
        """
        :param vip_id:
        :return: 0失败， 1 成功
        """
        token = token_parser.parse_args().token
        return rm_vip(vip_id, token=token)

