from django.http import JsonResponse


def home(request):
    return JsonResponse({
        "message": "Welcome to the Django Server!",
        "status": "running",
    })


def hello(request):
    name = request.GET.get("name", "World")
    return JsonResponse({
        "message": f"Hello, {name}!",
    })


def health(request):
    return JsonResponse({
        "status": "ok",
    })
