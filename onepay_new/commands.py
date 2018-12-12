# -*- coding: utf-8 -*-

from flask import request, redirect, url_for


def redirect_back(html, **kwargs):
    return redirect(url_for(html, **kwargs))