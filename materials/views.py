from django.views import generic
from .models import Category,Resource
from django.shortcuts import render
from .forms import SearchForm

class IndexView(generic.ListView):
    template_name = 'materials/index.html'
    context_object_name = 'all_categories'

    def get_queryset(self):
        return Category.objects.all()

def DetailView(request,name):
    resource = Resource.objects.get(material_name=name)
    return render(request, 'materials/detail.html', {'resource':resource})

#def Search(request):
 #form = SearchForm(request.GET)

  #  resource = Resource.objects.get(material_name=form.search)

   # return render(request, 'materials/detail.html',{'resource':resource})

