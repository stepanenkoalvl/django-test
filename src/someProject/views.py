from django.shortcuts import render, get_object_or_404
from datetime import datetime
# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.template import loader
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.auth.decorators import login_required


def index(request):
    return HttpResponseRedirect(reverse('test1:index'))