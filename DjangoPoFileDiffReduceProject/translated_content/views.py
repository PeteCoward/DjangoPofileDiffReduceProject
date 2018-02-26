from django.utils.translation import gettext as _
from django.views.generic.base import TemplateView


class IndexView(TemplateView):

    template_name = "translated_content/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['python_translated_content'] = _('A translation from python')
        return context
