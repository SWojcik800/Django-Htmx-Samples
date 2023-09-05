from datetime import datetime
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from flights.models.url_shortcut import UrlShortcut

class UrlShortcutsIndex(TemplateView):
    template_name='url_shortcuts/index.html'

class UrlShortcutsRows(View):
    template_name='url_shortcuts/url_shortcut_rows.html'

    def get(self, request):
        now = datetime.now()
        page_index = int(request.GET.get('page_index', '1'))
        page_size = 10
        offset = (page_index-1) * page_size
        limit = page_size
        items = UrlShortcut.objects.filter(valid_to__gte = now).order_by('-valid_to')[offset:offset+limit]

        return render(request, 'url_shortcuts/url_shortcut_rows.html' , {
            "items": items,
            "next_page": page_index+1
        })
    