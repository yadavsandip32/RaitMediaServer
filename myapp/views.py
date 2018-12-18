from django.shortcuts import render

from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.urls import reverse
from myapp.models import Document
from myapp.forms import DocumentForm
from myapp.models import Document
import subprocess


def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('list'))
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()


    # Render list page with the documents and the form
    return render(request, 'index.html', {'documents': documents, 'form': form})


def play(request, ID):
    Id = ID
    print(Id)
    obj = Document.objects.get(pk=Id)

    return render(request, 'playVid.html', {'obj':obj})

# subprocess.call("ffmpeg -ss 00:0:01 -i "+ uploaded_filename +" -frames:v 1 "+ thumbnail_name ,shell=True)