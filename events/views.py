from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.utils import timezone  # 添加这行导入
from .models import Event
from .forms import EventForm

# 前端用户视图
def event_list(request):
    now = timezone.now()
    events = Event.objects.filter(end_date__gte=now)
    past_events = Event.objects.filter(end_date__lt=now)  # 保持查询不变，不转为None
    
    return render(request, 'events/list.html', {
        'events': events,
        'past_events': past_events  # 始终传递QuerySet
    })

# 管理员视图
class AdminEventListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Event
    template_name = 'admin/events.html'
    context_object_name = 'events'
    paginate_by = 10
    
    def test_func(self):
        return self.request.user.is_staff
    
    def get_queryset(self):
        queryset = super().get_queryset().order_by('-created_at')
        search_query = self.request.GET.get('q', '')
        if search_query:
            queryset = queryset.filter(title__icontains=search_query)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['event_management'] = True
        context['search_query'] = self.request.GET.get('q', '')
        return context

class EventCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Event
    form_class = EventForm
    template_name = 'admin/event_form.html'
    success_url = reverse_lazy('admin_events')
    
    def test_func(self):
        return self.request.user.is_staff
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['event_management'] = True
        context['title'] = '创建新活动'
        return context

class EventUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'admin/event_form.html'
    success_url = reverse_lazy('admin_events')
    
    def test_func(self):
        return self.request.user.is_staff
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['event_management'] = True
        context['title'] = '编辑活动'
        return context

class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Event
    template_name = 'admin/event_confirm_delete.html'
    success_url = reverse_lazy('admin_events')
    
    def test_func(self):
        return self.request.user.is_staff
