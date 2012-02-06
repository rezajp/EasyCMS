from django.db import models
from django.db.models.fields.related import ManyToManyField

class SiteInstance(models.Model):
    name=models.CharField(max_length=50,null=False,unique=True)

class SiteUrl(models.Model):
    address=models.CharField(null=False,unique=True,max_length=100)
    of_site=models.ForeignKey('SiteInstance',null=False,related_name='urls')

class Page(models.Model):
    title=models.CharField(max_length=100,null=False)
    url_key=models.CharField(max_length=30,null=False,unique=True)
    styles=ManyToManyField('ElementStyle')
    of_site=models.ForeignKey('SiteInstance',null=False,related_name='pages')

class PageContent(models.Model):
    in_page=models.ForeignKey('Page',null=False,related_name='contents')
    of_content=models.ForeignKey('Content')
    styles=ManyToManyField('ElementStyle')

class Content(models.Model):
    title=models.CharField(max_length=100)

class TextContent(Content):
    text_value=models.TextField(null=False)
    
class LinkContent(Content):
    to_url=models.CharField(max_length=255,null=False)
    
#class ImageContent(Content):
#    image=models.ImageField(null=False)
    
class ElementStyle(models.Model):
    style_key=models.CharField(null=False,max_length=50)
    style_value=models.CharField(null=False,max_length=50)
    
    
    
    
    
    