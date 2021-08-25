from django.shortcuts import render, redirect
from django.http import HttpResponse, response

from pytube import YouTube
from pytube.streams import Stream
import requests
 
# Create your views here.
def index(request):
    default_thumbnail = 'https://camo.githubusercontent.com/1062c33f73289b4766688c67773f321b959a0ec9c8a62a506c925db066097391/68747470733a2f2f6d61726b6574696e676465636f6e746575646f2e636f6d2f77702d636f6e74656e742f75706c6f6164732f323031372f30362f7468756d626e61696c2e706e67'
    return render(request, 'index.html', {'thumbnail_url': default_thumbnail})

def generate(request):
    video_url = request.POST['video_url']
    yt = YouTube(video_url)
    thumb_url = yt.thumbnail_url
    video_title = yt.title
    return render(request, 'index.html', {'thumbnail_url': thumb_url, 'search_url': video_url, 'video_name': video_title})

def download144p(request):
    video_url = request.GET['144p']
    yt = YouTube(video_url)
    stream = yt.streams.get_by_itag(17)
    stream.download()
    return HttpResponse('Video Downloaded')