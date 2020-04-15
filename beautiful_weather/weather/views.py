from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic.edit import BaseCreateView

from .models import Request


class IndexView(TemplateView):
    template_name = 'index.html'


class ResultView(BaseCreateView):
    model = Request
    fields = ('city',)
    http_method_names = ['post']

    def form_invalid(self, form):
        return HttpResponse(form.errors, status=400)

    def form_valid(self, form):
        super().form_valid(form)
        self.object.check_weather()
        return HttpResponse(content=self.object.result)

    def get_success_url(self):
        return None
