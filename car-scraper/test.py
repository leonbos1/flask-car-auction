import requests
from PIL import Image
from io import BytesIO

def blob_to_image(blob):
    return Image.open(BytesIO(blob))

k = requests.get("https://prod.pictures.autoscout24.net/listing-images/3b8893c4-84f2-4595-9d93-28da91936095_d213f504-58c8-4dbf-b0ae-a9ed28d6277c.jpg/360x270.jpg")
print(k.content)
img = blob_to_image(k.content)
img.show()

