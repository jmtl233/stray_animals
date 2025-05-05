from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Announcement
from .forms import AnnouncementForm

class AdminAnnouncementListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    template_name = 'admin/announcements.html'
    context_object_name = 'announcements'
    model = Announcement
    paginate_by = 10
    
    def test_func(self):
        return self.request.user.is_staff
    
    def get_queryset(self):
        queryset = super().get_queryset().order_by('-publish_date')
        search_query = self.request.GET.get('q', '')
        if search_query:
            queryset = queryset.filter(title__icontains=search_query)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['announcement_management'] = True
        context['search_query'] = self.request.GET.get('q', '')
        return context

# 修改AnnouncementCreateView、AnnouncementUpdateView和AnnouncementDeleteView中的success_url
class AnnouncementCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Announcement
    form_class = AnnouncementForm
    template_name = 'admin/announcement_form.html'
    success_url = reverse_lazy('admin_announcements')  # 修改这里
    
    def test_func(self):
        return self.request.user.is_staff
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['announcement_management'] = True
        context['title'] = '发布新公告'
        return context

class AnnouncementUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Announcement
    form_class = AnnouncementForm
    template_name = 'admin/announcement_form.html'
    success_url = reverse_lazy('admin_announcements')  # 修改这里
    
    def test_func(self):
        return self.request.user.is_staff
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['announcement_management'] = True
        context['title'] = '编辑公告'
        return context

class AnnouncementDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = 'admin/announcement_confirm_delete.html'
    model = Announcement
    # 修改为完整的命名空间路径
    success_url = reverse_lazy('admin_announcements')  # 或者使用 reverse_lazy('announcements:admin_list')
    
    def test_func(self):
        return self.request.user.is_staff
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['announcement_management'] = True
        return context
        
    # 添加一个get_success_url方法来动态生成成功URL
    def get_success_url(self):
        from django.urls import reverse
        return reverse('admin_announcements')
