#!/usr/bin/env python
# encoding: utf-8

"""
    File name: sales_record.py
    Function Des: ...
    ~~~~~~~~~~
    
    author: Jerry <cuteuy@gmail.com> <http://www.skyduy.com>
    
"""
from flask import abort
from RESTfulApi.models.shop_db import SalesRecord
from RESTfulApi.models.shop_db import Account, Book, Vip
from RESTfulApi.common.authority import is_stuff, is_admin


def get_all_sales_records(token=None):
    if token is None or not is_admin(token):
        return abort(403)
    sales_records = SalesRecord.objects()
    return sales_records


def create_sales_record(count, seller_id, book_id, purchaser_id, token=None):
    if token is None or not is_stuff(token):
        return abort(403)
    book = Book.objects(id=book_id).first()
    if book is None:
        return {'message': 'Missing parameter book'}
    if book.remaining < count:
        return {'message': 'This book is not enough'}
    price = book.price
    seller = Account.objects(id=seller_id).first()
    if seller is None:
        return {'message': 'Missing parameter seller'}
    purchaser = Vip.objects(id=purchaser_id).first()
    if purchaser is not None:
        price *= 0.8
    book.remaining -= count
    book.sales += count
    book.save()
    sales_record = SalesRecord(
        count=count,
        price=price,
        book=book,
        seller=seller,
        purchaser=purchaser,
    )
    return sales_record.save()


def get_sales_record_by_id(sales_record_id, token=None):
    if token is None or not is_admin(token):
        return abort(403)
    sales_record = SalesRecord.objects(id=sales_record_id).first()
    return sales_record



