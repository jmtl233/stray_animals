from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

class AdminAnnouncementListView(LoginRequiredMixin, ListView):
    template_name = 'admin/announcements.html'
    context_object_name = 'announcements'
    
    def get_queryset(self):
        # 临时返回空数据，实际开发时应替换为真实数据
        return [] 