# from django.conf import settings # not used currently but maybe later
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# from rest_framework.decorators import api_view # not used currently but maybe later
from rest_framework.parsers import JSONParser

import logging

from .models import ourUser

logging.basicConfig(level=logging.DEBUG)


def index(request):
    return HttpResponse("hello world whats up")


@csrf_exempt
def createNewUser(request):
    logging.debug(request)
    logging.debug(request.method)
    logging.debug(request.body)
    newUserData = JSONParser().parse(request)
    # test to see if user name and email exist
    array2 = ourUser.objects.filter(userName=newUserData["data"]['email'])
    list_result = [entry for entry in array2]
    if len(list_result) == 0:
        datasave = ourUser(
            userName=newUserData["data"]['email'],  password=newUserData["data"]['password'])
        datasave.save()
        return HttpResponse("user created", status=201, content_type='text/plain')
    if len(list_result) > 0:
        return HttpResponse("that email exists try again", status=406, content_type='text/plain')
