from django.shortcuts import render
from rest_framework.views import APIView
from django.http.response import HttpResponse, HttpResponseRedirect
from discord import upload_server_emojis
from django.conf import settings

def index(request):
    return render(request, 'emojify.html', {})

class RunProfilePicEmojify(APIView):
    def post(self, request):
        upload_server_emojis.upload(settings.GUILD_ID, settings.API_KEY_SECRET)
        return HttpResponseRedirect('/')

class SubmitDoodleEmojify(APIView):
    def post(self, request):
        image = request.POST.get('dataUrl')
        emoji_data = {
            "name" : "doodle",
            "image" : image,
            "roles" : ["559139679388172304"]
        }
        guildId = settings.GUILD_ID
        apiKey = settings.API_KEY_SECRET
        print(upload_server_emojis.delete_server_emoji("doodle", guildId, apiKey))
        upload_server_emojis.upload_server_emoji_raw(emoji_data, guildId, apiKey)
        return HttpResponseRedirect('/')