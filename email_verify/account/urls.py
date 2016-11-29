#! /usr/bin/env python
# coding:utf-8


from django.conf.urls import patterns, include, url

"""
Created on: 2016-11-29 17:24 
@author: guolt
"""

urlpatterns = patterns('account.views',
    url(r'^register/$', 'register', name='account.views.register'),
    url(r'^do_verificatin/$', 'do_verificatin', name='account.views.do_verificatin'),
    url(r'^success/$', 'success', name='account.views.success'),
    url(r'^fail/$', 'fail', name='account.views.fail'),
    url(r'^wait_verifyed/$', 'wait_verifyed', name='account.views.wait_verifyed'),
    url(r'^error/$', 'error', name='account.views.error'),

)
