from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Build
from .forms import UploadPictureForm, ObservationForm, OwnerForm, \
                   PhoneNumberForm


# Create your views here.


def index(request):
    latest_build_list = Build.objects.order_by('pub_date')[:5]
    context = {
        'build_list': latest_build_list,
    }
    return render(request, 'imoveis/index.html', context);

def detail(request, build_id):
    build = get_object_or_404(Build, pk=build_id)
    context = {
        'build': build,
    }
    return render(request, 'imoveis/detail.html', context);

def add_observation(request):
    return add_form_mixin(request, ObservationForm, 'imoveis/picture.html');

def add_picture(request):
    return add_form_mixin(request, UploadPictureForm, 'imoveis/picture.html');

def add_owner(request):
    return add_form_mixin(request, OwnerForm, 'imoveis/owner.html');

def add_phonenumber(request):
    return add_form_mixin(request, PhoneNumberForm, 'imoveis/phonenumber.html');

def picture(request, build_id):
    return HttpResponse("picture of {}".format(build_id))

def add_form_mixin(request, form_class, template):
    if request.method == 'POST':
        form = form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/imoveis')
    else:
        form = form_class()
        context = {
            'form': form,
        }
    return render(request, template, context)

def search(request):
    if request.method == 'POST':
        query = request.POST['query']
        build_list = Build.objects.filter(address__icontains=query)
    else:
        query=''
        build_list = Build.objects.order_by('pub_date')[:5]
    context = {
        'build_list': build_list,
        'query': query,
    }
    return render(request, 'imoveis/search.html', context);

class BuildList(ListView):
    model = Build
    paginate_by = 10
    template_name = 'imoveis/index.html'
    context_object_name = 'build_list'

class BuildDetail(DetailView):
    model = Build
    template_name = 'imoveis/detail.html'
    context_object_name = 'build'
