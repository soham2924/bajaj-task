import easyocr
from PIL import Image
import numpy as np

reader = easyocr.Reader(['en'], gpu=False)

def process_image(image_file) -> str:
    image = Image.open(image_file).convert("RGB")
    img_np = np.array(image)
    result = reader.readtext(img_np, detail=0)
    return "\n".join(result)
