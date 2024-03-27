import os
import io
import requests
from PIL import Image
from sample import returner

image_urls = returner()
print(image_urls)

k = 0
filepath = os.path.join(os.getcwd(),"Downloads")
os.makedirs(filepath, exist_ok=True)  # Create directory if it doesn't exist

for i in image_urls:
    url = i
    try:
        response = requests.get(url, stream=True, timeout=5)
        response.raise_for_status()  # Raise an exception for non-200 status codes

        img = Image.open(io.BytesIO(response.content))
        img = img.convert('RGB')  # Convert to RGB if needed (e.g., for JPEG format)
        img.save(os.path.join(filepath, f"{k}.jpg"))

        print(f"Image {k} downloaded successfully: {url}")
        k += 1

    except requests.exceptions.RequestException as e:
        print(f"Error downloading image {i}: {e}")
    except OSError as e:
        print(f"Error saving image {i}: {e}")

print("\nImage download complete. Downloaded images are in:", filepath)
