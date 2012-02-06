from EasyCMSProject.EasyCMS import views
from django.template.loader import get_template
from django.template.context import Context
from django.http import HttpResponse

def index(request):
    site=views.get_site(request)
    template = get_template('admin/index.html')
    pages=site.pages.all()
    variables = Context({
       'pages': pages
    })
    output = template.render(variables)
    return HttpResponse(output)