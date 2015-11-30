from django.db import models
from django.contrib.auth.models import User
#from django.contrib import auth
#from django.template import RequestContext

from django.shortcuts import render
#from fileupload.models import Document
#from fileupload.forms import DocumentForm 
from django.contrib import auth
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your models here.


class Document(models.Model):
    owner = models.ForeignKey(User)
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
    delete = models.IntegerField(default=0)
    filename = models.CharField(max_length=255, null=True)
    md_value = models.CharField(max_length=255, null=True)
