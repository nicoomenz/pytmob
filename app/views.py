from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseServerError
from django.views.decorators.http import require_http_methods
from .helper import get_url
import json

# Create your views here.
@require_http_methods(["GET"])
def redirect_view(request, key):
    try:
        url = get_url(key)
        if url:
            data = {"key": key, "url": url }
            return HttpResponse(json.dumps(data),content_type='application/json',status=200)
        return HttpResponseBadRequest('Not exist url for this key')
    except:
        return HttpResponseServerError('Internal server error, try again')

