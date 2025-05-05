from announcements.models import Announcement

def latest_announcement(request):
    """
    获取最新的已发布公告，并添加到模板上下文中
    """
    latest = Announcement.objects.filter(is_published=True).order_by('-publish_date').first()
    return {
        'latest_announcement': latest
    }