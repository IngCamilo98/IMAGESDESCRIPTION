from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
from pathlib import Path
import torch

def describe_image(image_path: str) -> str:
    # Cargar modelo y preprocesador
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

    # Abrir imagen
    raw_image = Image.open(image_path).convert('RGB')

    # Procesar y generar descripción
    inputs = processor(raw_image, return_tensors="pt")
    out = model.generate(**inputs)
    description = processor.decode(out[0], skip_special_tokens=True)

    return description

# Ruta a la imagen
image_file = Path(__file__).parent.parent / "DATA" / "IMAGES" / "IMG-0001.jpg"
print(f"Imagen cargada: {image_file.name}")

# Describir
description = describe_image(str(image_file))
print("Descripción generada:")
print(description)
