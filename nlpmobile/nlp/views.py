# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import HttpResponse


# Create your views here.
def Index(request):
	return render(
		request,
		"nlp/home.html",
	)