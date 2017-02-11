# Sifer Aseph

from .models import Image
#from .forms import ImageForm

from .forms import ImageFormset

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def page(request):
    """This does most of the work."""
    allImages = Image.objects.all() # All the images loaded are here.

    # https://docs.djangoproject.com/en/1.10/topics/pagination/#using-paginator-in-a-view
    current_page_number = request.GET.get("page")
    pagePaginator = Paginator(allImages, 10)
    try:
        currentPage = pagePaginator.page(current_page_number)
    except PageNotAnInteger: # For absurd page numbers.
        currentPage = pagePaginator.page(1)
    except EmptyPage: # For out of range pages.
        currentPage = pagePaginator.page(pagePaginator.num_pages)

    #form = ImageForm()
    formset = ImageFormset()
    if request.method == "POST": # The only way to do this. https://docs.djangoproject.com/en/1.10/ref/request-response/#django.http.HttpRequest.method
        #form = ImageForm(request.POST, request.FILES) # https://docs.djangoproject.com/en/1.10/topics/http/file-uploads/
        formset = ImageFormset(request.POST, request.FILES)
        if formset.is_valid(): # https://docs.djangoproject.com/en/1.10/ref/forms/api/#django.forms.Form.is_valid
            #newImage = Image(image_file = request.FILES['image_file'])
            #newImage.save() # https://docs.djangoproject.com/en/1.10/topics/http/file-uploads/#handling-uploaded-files-with-a-model
            for form in formset:
                form.save()
            return HttpResponseRedirect(reverse('page'))
        #else:
            #form = ImageForm()
        #    formset = ImageFormset()

    #return render(request, 'page.html', {'allImages': allImages, 'form': form}) # https://docs.djangoproject.com/en/1.10/topics/http/shortcuts/
    return render(request, 'page.html', {'currentPage': currentPage, 'formset': formset})
