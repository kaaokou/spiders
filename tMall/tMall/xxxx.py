#! /usr/local/bin/python2# -*- coding: utf-8 -*-# Author   : Douglas# @Time    : 2018/8/8 下午4:06# @Email   : 304061178@qq.com# @Software: PyCharma= [[{u'status': 2, u'postageFree': False, u'canBuyCouponNum': 0, u'extraPromType': 0,   u'promText': u'\u767b\u5f55\u540e\u786e\u8ba4\u662f\u5426\u4eab\u6709\u6b64\u4f18\u60e0',   u'tfCartSupport': False, u'unLogBrandMember': False, u'promType': u'normal', u'amountRestriction': u'',   u'amountPromLimit': 0, u'start': False, u'unLogTbvip': False, u'basePriceType': u'IcPrice', u'extraPromTextType': 0,   u'startTime': 1522231240000, u'tmallCartSupport': False, u'endTime': 4102416000000, u'type': u'\u5e97\u94favip',   u'unLogShopVip': False, u'limitProm': False}], [     {u'status': 2, u'postageFree': False, u'canBuyCouponNum': 0, u'extraPromType': 0,      u'promText': u'\u767b\u5f55\u540e\u786e\u8ba4\u662f\u5426\u4eab\u6709\u6b64\u4f18\u60e0', u'price': u'588.00',      u'tfCartSupport': False, u'unLogBrandMember': False, u'promType': u'normal', u'amountRestriction': u'',      u'amountPromLimit': 0, u'start': False, u'unLogTbvip': False, u'basePriceType': u'IcPrice',      u'extraPromTextType': 0, u'startTime': 1522231240000, u'tmallCartSupport': False, u'endTime': 4102416000000,      u'type': u'\u5e97\u94favip', u'unLogShopVip': False, u'limitProm': False}], [     {u'status': 2, u'postageFree': False, u'canBuyCouponNum': 0, u'extraPromType': 0,      u'promText': u'\u767b\u5f55\u540e\u786e\u8ba4\u662f\u5426\u4eab\u6709\u6b64\u4f18\u60e0', u'price': u'588.00',      u'tfCartSupport': False, u'unLogBrandMember': False, u'promType': u'normal', u'amountRestriction': u'',      u'amountPromLimit': 0, u'start': False, u'unLogTbvip': False, u'basePriceType': u'IcPrice',      u'extraPromTextType': 0, u'startTime': 1522231240000, u'tmallCartSupport': False, u'endTime': 4102416000000,      u'type': u'\u5e97\u94favip', u'unLogShopVip': False, u'limitProm': False}], [     {u'status': 2, u'postageFree': False, u'canBuyCouponNum': 0, u'extraPromType': 0,      u'promText': u'\u767b\u5f55\u540e\u786e\u8ba4\u662f\u5426\u4eab\u6709\u6b64\u4f18\u60e0',      u'tfCartSupport': False, u'unLogBrandMember': False, u'promType': u'normal', u'amountRestriction': u'',      u'amountPromLimit': 0, u'start': False, u'unLogTbvip': False, u'basePriceType': u'IcPrice',      u'extraPromTextType': 0, u'startTime': 1522231240000, u'tmallCartSupport': False, u'endTime': 4102416000000,      u'type': u'\u5e97\u94favip', u'unLogShopVip': False, u'limitProm': False}]]price_list = [ i[0].get("price") for i in a]for price in price_list:    if price is None:        price_list.remove(price)print(price_list)