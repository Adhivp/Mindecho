from django.shortcuts import *


# Create your views here.

from AIS_Dreaming.models import UploadedImage

def upload_and_display(request):
    if request.method == 'POST' and 'image' in request.FILES:
        image = request.FILES['image']
        uploaded_image = UploadedImage(image=image)
        uploaded_image.save()
        return redirect('upload_and_display')

    # Retrieve the latest uploaded image
    latest_image = UploadedImage.objects.last()

    return render(request, 'upload_and_display.html', {'latest_image': latest_image})

