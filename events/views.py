from django.shortcuts import render

# Create your views here.

def event_list(request):
    # 临时视图，实际开发时应替换为真实数据
    return render(request, 'events/list.html', {'events': []})
