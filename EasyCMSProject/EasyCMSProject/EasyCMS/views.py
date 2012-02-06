from django.http import HttpRequest
from django.http import HttpResponse
from EasyCMSProject.EasyCMS.models import *
from urlparse import urlparse
from django.template import Context
from django.template.loader import get_template

def home_page(request):
    site=get_site(request)
    return show_page_by_key(site,'home')
def show_page(request,page_key):
    site=get_site(request)
    return show_page_by_key(site,page_key)
def show_page_by_key(site,page_key):
    page=Page.objects.filter(of_site=site,url_key=page_key)[0]
    return show_page_by_page(page)
def show_page_by_page(page):
    template = get_template('page.html')
    contents=page.contents.all()
    variables = Context({
       'page': page,
       'contents': contents
    })
    output = template.render(variables)
    return HttpResponse(output)
def get_site(request):
    domain=get_domain(request)
    return SiteUrl.objects.filter(address=domain)[0].of_site
def get_domain(request):
    return request.META['HTTP_HOST']