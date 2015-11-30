from django.shortcuts import render
from fileupload.models import Document
from fileupload.forms import DocumentForm
from django.contrib import auth
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import os 
import subprocess
import tempfile
import hashlib
from functools import partial
import pdb
# Create your views here.

def loggedin(request):
    # Handle file upload
    #user = request.user 
    #name=""
    #gname="hi"
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            newdoc = Document(docfile = request.FILES['docfile'], owner=user)
            newdoc.save()

            #pdb.set_trace()
            dir="/home/saurabh/Projects/filepanda"+newdoc.docfile.url
            name=""
            for k in range(len(dir)):
                if(dir[-1*k-1]!='/'):
                    name=dir[-1*k-1]+name
                else:
                    break
            name=name+".zip"

            # !hashing here!
            with open(dir, mode='rb') as f:
                d = hashlib.md5()
                for buf in iter(partial(f.read, 128), b''):
                    d.update(buf)
            hashed = d.hexdigest()
            print(hashed)
            # !hashed
            # newdoc2 = Document.objects.get(id=newdoc.id)
            newdoc.filename = name
            newdoc.md_value = hashed
            newdoc.save()

            with tempfile.TemporaryFile() as tempf: 
                os.system("zip -j /home/saurabh/Projects/filepanda/media/zipped/"+ name +" " + dir)

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('fileupload.views.loggedin'))
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form

    return render_to_response(
        'loggedin.html',
        {'documents': documents, 'form': form, 'full_name': request.user.username },
        context_instance=RequestContext(request)
    )

def delete_article(request, document_id):
    if document_id:
        a = Document.objects.get(id=document_id)
        a.delete = 1
        #a.docfile = File(file('/home/saurabh/Projects/filepanda/media/expiry.txt'))
        os.system("rm /home/saurabh/Projects/filepanda/"+a.docfile.url)
        os.system("rm /home/saurabh/Projects/filepanda/media/zipped/"+a.filename)
        a.save()

    return HttpResponseRedirect('/accounts/loggedin/')

def download_file(request, document_id):
    if document_id:
        a = Document.objects.get(id=document_id)

    return HttpResponseRedirect(a.docfile.url)
