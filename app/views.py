
from django.shortcuts import render_to_response,get_object_or_404, render
from django.template.context import RequestContext


def home(request):
    template = "index.html"
    return render(request, template,{})





