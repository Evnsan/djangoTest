from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Build

# Create your views here.


def index(request):
    latest_build_list = Build.objects.order_by('pub_date')[:5]
    context = {
        'latest_build_list': latest_build_list,
    }
    return render(request, 'imoveis/index.html', context);

def detail(request, build_id):
    build = get_object_or_404(Build, pk=build_id)
    context = {
        'build': build,
    }
    return render(request, 'imoveis/detail.html', context);

def picture(request, build_id):
    return HttpResponse("picture of {}".format(build_id))
