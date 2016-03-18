#!/usr/bin/env python
# encoding: utf-8

"""
    File name: vip.py
    Function Des: ...
    ~~~~~~~~~~
    
    author: Jerry <cuteuy@gmail.com> <http://www.skyduy.com>
    
"""
from flask import abort
from mongoengine import Q
from RESTfulApi.models.shop_db import Vip
from RESTfulApi.common.authority import is_stuff


def get_all_vips(token=None):
    if token is None or not is_stuff(token):
        return abort(403)

    vips = Vip.objects()
    return vips


def create_vip(username, nickname, phone, token=None):
    if token is None or not is_stuff(token):
        return abort(403)

    if phone is None:
        phone = ""
    vip = Vip(
        username=username,
        nickname=nickname,
        phone=phone,
    )
    return vip.save()


def get_vip_by_id(vip_id, token=None):
    if token is None or not is_stuff(token):
        return abort(403)

    vip = Vip.objects(id=vip_id).first()
    return vip


def get_vips(args, token=None):
    if token is None or not is_stuff(token):
        return abort(403)

    if 'name' in args:
        return Vip.objects(Q(name=args['name']))
    return None


def rm_vip(book_id, token=None):
    if token is None or not is_stuff(token):
        return abort(403)

    vip = Vip.objects(id=book_id)
    return vip.delete()


