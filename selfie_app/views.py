from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import base64
from django.core.files.base import ContentFile
import uuid
from .models import Selfie

def selfie_view(request):
    return render(request, 'pages/selfie.html')

@csrf_exempt
def upload_selfie(request):
    if request.method == 'POST':
        image_data = request.POST.get('image')
        if image_data:
            format, imgstr = image_data.split(';base64,')
            ext = format.split('/')[-1]
            file_name = f"{uuid.uuid4()}.{ext}"
            data = ContentFile(base64.b64decode(imgstr), name=file_name)

            selfie = Selfie()
            selfie.image.save(file_name, data)
            selfie.save()

            return JsonResponse({'status': 'success', 'file_url': selfie.image.url})
    return JsonResponse({'status': 'error'})
