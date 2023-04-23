import re
import json
import os
from django.http import HttpResponse, JsonResponse
from concurrent.futures import ThreadPoolExecutor
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def get_story_from_premise(request):
    """
    This function takes a premise and returns a story.
    """
    
    input_string = json.loads(request.body.decode("utf-8"))["input_string"]
    if input_string is None:
        return HttpResponse("No input string provided")    
    
    premise = input_string["premise"]