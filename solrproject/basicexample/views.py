from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response


class JSONResponse(HttpResponse):

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@api_view(['GET'])
def introduction(request):
    return Response({"message": "Working..."}, status=status.HTTP_200_OK)