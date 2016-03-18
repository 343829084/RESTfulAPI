#!/usr/bin/env python
# encoding: utf-8

"""
    File name: session.py
    Function Des: ...
    ~~~~~~~~~~
    
    author: Jerry <cuteuy@gmail.com> <http://www.skyduy.com>
    
"""
from RESTfulApi.models.shop_db import Account
from RESTfulApi.models.token_db import Token
from RESTfulApi.common.authority import create_token


def login(username, password):
    account = Account.objects(username=username).first()
    if account is None:
        return {'message': 'this account does not exist'}
    if Account.check_password(account, password):
        token = Token.objects(user_id=str(account.id))
        new_token = create_token()
        token.update(token=new_token)
        return {'token': new_token}


def logout(token):
    token = Token.objects(token=token).first()
    if token is None:
        return 0
    token.update(token='')
    return 1
