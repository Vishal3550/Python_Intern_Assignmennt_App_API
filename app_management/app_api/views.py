from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
import json
from .models import AppDetails

@csrf_exempt
def add_app(request):
    if request.method == "POST":
        data = json.loads(request.body)
        app = AppDetails.objects.create(
            app_name=data.get("app_name"),
            version=data.get("version"),
            description=data.get("description")
        )
        return JsonResponse({"message": "App added successfully!", "id": app.id})

def get_app(request, id):
    app = get_object_or_404(AppDetails, id=id)
    return JsonResponse({
        "app_name": app.app_name,
        "version": app.version,
        "description": app.description
    })

@csrf_exempt
def delete_app(request, id):
    if request.method == "DELETE":
        app = get_object_or_404(AppDetails, id=id)
        app.delete()
        return JsonResponse({"message": "App deleted successfully!"})
