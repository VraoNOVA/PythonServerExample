import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

MESSAGES = {}
NEXT_ID = 1


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


@csrf_exempt
@require_http_methods(["GET", "POST"])
def messages_list(request):
    global NEXT_ID

    if request.method == "GET":
        return JsonResponse({"messages": list(MESSAGES.values())})

    # POST
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    msg = {
        "id": NEXT_ID,
        "text": data.get("text", ""),
        "author": data.get("author", "anonymous"),
    }
    MESSAGES[NEXT_ID] = msg
    NEXT_ID += 1
    return JsonResponse(msg, status=201)


@csrf_exempt
@require_http_methods(["GET", "PUT", "DELETE"])
def message_detail(request, message_id):
    if message_id not in MESSAGES:
        return JsonResponse({"error": "Not found"}, status=404)

    if request.method == "GET":
        return JsonResponse(MESSAGES[message_id])

    if request.method == "PUT":
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
        MESSAGES[message_id]["text"] = data.get("text", MESSAGES[message_id]["text"])
        MESSAGES[message_id]["author"] = data.get("author", MESSAGES[message_id]["author"])
        return JsonResponse(MESSAGES[message_id])

    # DELETE
    deleted = MESSAGES.pop(message_id)
    return JsonResponse({"deleted": deleted})
