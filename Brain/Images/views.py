from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.core.files import File
import os, sys

import numpy as np
from skimage import io

from .models import Image

def str_to_img_then_save(string_img, row_dim, column_dim):
    string_img_list = string_img.split(',')[:-1]
    array_img = np.array(string_img_list, dtype=np.uint8)
    stacked_img = np.reshape(array_img, (row_dim, column_dim, 3))
    io.imsave("tmp.jpg", stacked_img)

# Create your views here.

def image_list(request):
    latest_image_list = Image.objects.all()
    context = { 'latest_image_list' : latest_image_list, }
    return render(request, 'Images/index.html', context)

@csrf_exempt
def post_image(request):
    if request.method == "POST":
        # If there's an image of same name, then do nothing
        image_list = Image.objects.all()
        for image in image_list:
            if image.file_name == request.POST['file_name']:
                return render(request, 'Images/index.html')
        
        str_to_img_then_save(request.POST['image'], int(request.POST['row_dim']), int(request.POST['column_dim']))
        reopen = open('tmp.jpg', 'rb')
        django_file = File(reopen)

        new_image = Image()
        new_image.file_name = request.POST['file_name']
        new_image.content = request.POST['content']
        new_image.image.save(request.POST['file_name'], django_file)
        new_image.save()
        return render(request, 'Images/index.html')

@csrf_exempt
def post_speech(request):
    if request.method == "OPTIONS":
        # If there's an image of same name, then do nothing
        print(sys.getsizeof(request.body))
        speech_file = open('speech_tmp.ogg', 'w+b')
        speech_file.write(request.body)
        speech_file.close()
        return HttpResponse("Speech.")
        #return render(request, 'Images/index.html')
    return HttpResponse("Speech.")

def detail(request, question_id):
    return HttpResponse(str(question_id) + " image.")

