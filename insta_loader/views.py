import json
import requests

from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views import View


# Json response data mixin
class JsonResponseDataMixin:
    def get_response_data(self, request):
        api_url = "https://instagram120.p.rapidapi.com/api/instagram/links"
        headers = {
            "Content-Type": "application/json",
            "X-RapidAPI-Key": "14099712b6msha8ec14aa083c8a5p1de149jsn28196a726227",
            "X-RapidAPI-Host": "instagram120.p.rapidapi.com"
        }
        payload = json.dumps(
            {"url": request.POST.get("instagram_url"), }
        )

        response = requests.post(api_url, headers=headers, data=payload)
        return response.json()


class VideoView(View, JsonResponseDataMixin):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(
            request,
            'pages/video.html'
        )

    def post(self, request: HttpRequest) -> HttpResponse:
        data = self.get_response_data(request)
        video_url = None

        if isinstance(data, list):
            for item in data:
                for video in item.get("urls", []):
                    if video.get("extension") == "mp4":
                        video_url = video["url"]
                        break
                if video_url:
                    break

        return render(
            request, "pages/video.html", {
                "video_url": video_url,
                "error": data.get(
                    "message", "Unknown error"
                ) if not video_url else None
            }
        )


class PhotoView(View, JsonResponseDataMixin):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(
            request,
            'pages/photo.html'
        )

    def post(self, request: HttpRequest) -> HttpResponse:
        data = self.get_response_data(request)
        photo_url = data[0]["urls"][0]["url"].replace("&dl=1", "")

        return render(
            request, "pages/photo.html", {
                "photo_url": photo_url,
                "error": data.get(
                    "message", "Unknown error"
                ) if not photo_url else None
            }
        )


class ReelsView(View, JsonResponseDataMixin):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(
            request,
            'pages/reels.html'
        )

    def post(self, request: HttpRequest) -> HttpResponse:
        data = self.get_response_data(request)

        video_url = None
        if isinstance(data, list):
            for item in data:
                for video in item.get("urls", []):
                    if video.get("extension") == "mp4":
                        video_url = video["url"]
                        break
                if video_url:
                    break

        return render(
            request, "pages/reels.html", {
                "video_url": video_url,
                "error": data.get(
                    "message", "Unknown error"
                ) if not video_url else None
            }
        )


class StoryView(View, JsonResponseDataMixin):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(
            request,
            'pages/story.html'
        )

    def post(self, request: HttpRequest) -> HttpResponse:
        data = self.get_response_data(request)

        video_url = None
        photo_url = None

        if data["result"][0].get('video_versions'):
            video_url = data["result"][0]['video_versions'][0]["url"]
        else:
            photo_url = \
                data["result"][0]["image_versions2"]['candidates'][1][
                    "url"]

        return render(
            request, "pages/story.html", {
                "video_url": video_url,
                "photo_url": photo_url,
                "error": data.get(
                    "message", "Unknown error"
                )
            }
        )
