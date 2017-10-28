from django.views import generic
from .models import Category,Resource

class IndexView(generic.ListView):
    template_name = 'materials/index.html'
    context_object_name = 'all_categories'

    def get_queryset(self):
        return Category.objects.all()

class DetailView(generic.DetailView):
    model = Resource
    template_name = 'materials/detail.html'

