#!/usr/bin/env python
# encoding: utf-8

"""
    File name: common.py
    Function Des: post/delete/put响应内容
    ~~~~~~~~~~
    
    author: Jerry <cuteuy@gmail.com> <http://www.skyduy.com>
    
"""
from flask.ext.restful import fields

# after post/put with return id
pt_fields = {
    'id': fields.String,
    'success': fields.Integer(default=0),
    'message': fields.String(default='No message'),
}

# after post/put with return token
pt_fields_with_token = {
    'id': fields.String,
    'token': fields.String,
    'success': fields.Integer(default=0),
    'message': fields.String(default='No message'),
}

# after delete
deleted_fields = {
    'success': fields.Integer(default=0),
    'message': fields.String(default='No message'),
}
