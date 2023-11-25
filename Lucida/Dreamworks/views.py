
# views.py
from django.shortcuts import render
from django.core.files.base import ContentFile
import base64
import requests
from .models import GeneratedImage

def dreamworks(request):
    image_url = None
    error_message = None

    if request.method == 'POST':
        prompt = request.POST.get('prompt')
        prompt = "DREAM"
        url = "https://api.getimg.ai/v1/stable-diffusion/text-to-image"

        payload = {
            "prompt": prompt,
            "output_format": "jpeg"
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "authorization": "Bearer key-f70qlzh3rCKboUxxflPgRvfXPK2wqjHopkWeJ8w9DzB71bKu3zkQ4Wk4BnF7WSKUAnlQgJvchkOhFZNMKJiLMT3YEeo2Fco"
        }

        try:
            response = requests.post(url, json=payload, headers=headers)
            response.raise_for_status()
            image_data = response.content

            # Save the image to the database
            generated_image = GeneratedImage()
            generated_image.image.save('generated_image.jpeg', ContentFile(image_data), save=True)

            # Get the URL of the saved image
            image_url = generated_image.image.url

        except requests.RequestException as e:
            error_message = f"Error: {e}"

    return render(request, 'main.html', {'image_url': image_url, 'error_message': error_message})
