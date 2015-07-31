# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from imageproject.myapp.models import image
from imageproject.myapp.forms import imageForm

def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = imageForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = image(imagefile = request.FILES['imagefile'], caption = request.POST['caption'], short_desc = request.POST['short_desc'])
            newdoc.save()

            # Redirect to the image list after POST
            return HttpResponseRedirect(reverse('imageproject.myapp.views.list'))
    else:
        form = imageForm() # A empty, unbound form

    # Load images for the list page
    images = image.objects.all()

    # Render list page with the images and the form
    return render_to_response(
        'myapp/list.html',
        {'images': images, 'form': form},
        context_instance=RequestContext(request)
    )
def show(request):
    image_pk = request.GET.get('image_pk')
    try: 
        getImage = image.objects.get(pk=image_pk)
    except image.DoesNotExist:
        return HttpResponseRedirect(reverse('imageproject.myapp.views.list'))
       
    return render_to_response(
        'myapp/show.html',
        {'image': getImage},
        context_instance=RequestContext(request)
    )
