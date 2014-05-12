from django.shortcuts import render
from django.template import RequestContext


def index(request):
    context = {}

    return render(request, "core/index.html", context, context_instance=RequestContext(request))
