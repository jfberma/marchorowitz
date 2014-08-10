import json

from django.views.decorators.csrf import csrf_exempt

from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.renderers import JSONRenderer
from rest_framework.exceptions import ParseError


class GitHubHookView(GenericAPIView):
    renderer_classes = [JSONRenderer]

    @csrf_exempt
    def post(self, request, *args, **kwargs):

        # Explicit hook name
        name = kwargs.get('name', None)

        # Git repo information from post-receive payload
        if request.content_type == "application/json":
            payload = request.DATA
        else:
            # Probably application/x-www-form-urlencoded
            payload = json.loads(request.DATA.get("payload", "{}"))

        info = payload.get('repository', {})
        repo = info.get('name', None)

        # GitHub: repository['owner'] = {'name': name, 'email': email}
        # BitBucket: repository['owner'] = name
        user = info.get('owner', {})
        if isinstance(user, dict):
            user = user.get('name', None)

        if not name and not repo and not user:
            raise ParseError(
                "No JSON data or URL argument : cannot identify hook"
            )

        return {}