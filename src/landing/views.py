from django.shortcuts import render
from django.views.generic import TemplateView

from .models import PortfolioItem


def index(request):
    # return render(request, 'base.html')
    # data = PortfolioItem.objects.all()
    data = {
        'portfolio_items': PortfolioItem.objects.all(),
    }
    return render(request, 'landing/index.html', context=data)

class MainPageView(TemplateView):
    template_name = 'landing/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['portfolio_items'] = PortfolioItem.objects.all()
