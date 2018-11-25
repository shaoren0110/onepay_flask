# -*- coding: utf-8 -*-

from flask import request, redirect, url_for


def redirect_back(default='login', **kwargs):
    return redirect(url_for(default, **kwargs))