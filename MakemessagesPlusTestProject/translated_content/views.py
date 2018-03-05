from django.utils.translation import gettext as _
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    ''' an index view '''

    template_name = "translated_content/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['python_translated_header'] = _('A translation from python')
        context['python_translated_paragraph'] = _('''A translation from python that is multiline.
                It goes on and an and on, no-one knows when it will end, but it won;t end before the end
                of one line oh no''')
        return context
