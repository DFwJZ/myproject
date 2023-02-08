from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # return a success response
            return JsonResponse({'success': True})
        else:
            # return an error response
            return JsonResponse({'error': 'Invalid login credentials'})
    return JsonResponse({'error': 'Invalid request method'})


"""
curl -X POST http://localhost:8000/api/login -H "Content-Type: application/json" -H "X-CSRFToken: {{ csrf_token }}" -d '{"username": "user1", "password": "password1"}'
"""