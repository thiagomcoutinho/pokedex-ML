# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import redirect

from myproject.myapp.models import Document
from myproject.myapp.forms import DocumentForm
import os

## Importing custom functions to modify uploaded data and predict class
from myproject.myapp.prepareDataBase import prepareDataBase
from myproject.myapp.predictClass import predictClass
from myproject.myapp.cleanDataBase import cleanDataBase

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()

            prepareDataBase(dname)
            predicted = predictClass(dname)
            cleanDataBase(dname)
            if( predicted == 0.0 ): ## Pikachu
                return redirect("http://www.pokemon.com/br/pokedex/pikachu")
            elif( predicted == 1.0 ): ## Charmander
                return redirect("http://www.pokemon.com/br/pokedex/charmander")
            elif( predicted == 2.0 ): ## Squirtle
                return redirect("http://www.pokemon.com/br/pokedex/squirtle")
            elif( predicted == 3.0 ): ## Bulbasaur
                return redirect("http://www.pokemon.com/br/pokedex/bulbasaur")
            elif( predicted == 4.0 ): ## Lugia
                return redirect("http://www.pokemon.com/br/pokedex/lugia")
            elif( predicted == 5.0 ): ## Gengar
                return redirect("http://www.pokemon.com/br/pokedex/gengar")
            elif( predicted == 6.0 ): ## Unknwon pokemon
                return render_to_response('unknown.html')

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('myproject.myapp.views.list'))
    else:
        form = DocumentForm()  # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'list.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )
