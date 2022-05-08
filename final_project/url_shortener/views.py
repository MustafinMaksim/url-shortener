from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.views import generic
from . import utils
from .models import ShortURL

# Create your views here.


# view for rendering home page
def index(request):
    return render(request=request, template_name='url_shortener/index.html')


# view for rendering all links page
def all_links(request):
    return render(request=request, template_name='url_shortener/all_links.html')


# view for creating new short urls
def create_short_url(request):

    # get input full url from user's request
    full_url = request.POST['input-url']
    
    # check if user input has url format
    if utils.is_valid_url(full_url):

        # try to get a short_url model that already exists
        try:
            # trying to get model of short_url from db with input full_url
            short_url_model = ShortURL.objects.get(full_url=full_url)

            # form short url for user
            short_url = utils.form_short_url(request, short_url_model.hashed_url)

            # return render of index page with short url that already exists
            return render(request=request, template_name='url_shortener/index.html', 
                context={'short_url': short_url, 'href_short_url' : "http://" + short_url})

        # except that a model of short url does not exist
        except ShortURL.DoesNotExist:

            print("Exception!!!")

            # create hash with salt of full url
            hash_url = utils.hash_url(full_url)

            # add new record to database
            ShortURL.objects.create(hashed_url=hash_url, full_url=full_url, number_of_uses=0)

            # form short url for user
            short_url = utils.form_short_url(request, hash_url)

            # return render of index page with short url
            return render(request=request, template_name='url_shortener/index.html', 
                context={'short_url': short_url, 'href_short_url' : "http://" + short_url})

    else:

        # form error_message for user
        error_message = 'Input full URL`s format is wrong. Please try again...'

        # return render of index page with error_message
        return render(request=request, template_name='url_shortener/index.html', 
            context={'error_message': error_message})