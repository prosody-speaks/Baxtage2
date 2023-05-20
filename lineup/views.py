from django.views.generic import DetailView, ListView

from producer.models import Performance




class PerformanceListView(ListView):
    model = Performance
    context_object_name = 'performances'
    template_name = 'lineup/performance_list.html'  # Update this with the correct template name


class PerformanceDetailView(DetailView):
    model = Performance
    context_object_name = 'performance'
    template_name = 'lineup/performance_detail.html'  # Update this with the correct template name
