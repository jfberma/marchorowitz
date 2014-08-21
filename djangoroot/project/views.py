from django.http import HttpResponse
from django.template import loader, RequestContext
from django.views.generic import TemplateView
import logging


logger = logging.getLogger(__name__)


class TestView(TemplateView):
    print("Cdascdascdsa")
    logger.debug("log?")
    template_name = "test.html"

def test(request):
    print("cdascdas")
    logger.debug("test")
    template = loader.get_template('test.html')
    context = RequestContext(request, {
        'latest_question_list': "cdscdsa",
    })
    return HttpResponse(template.render(context))