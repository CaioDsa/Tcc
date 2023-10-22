import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import (
    VGG16,
    preprocess_input,
    decode_predictions,
)
import numpy as np

# Carregando o modelo VGG16 pré-treinado
model = VGG16(weights="imagenet")


def is_elevator(image_path):
    img = image.load_img(image_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    preds = model.predict(x)
    decoded_preds = decode_predictions(preds, top=1)[0]

    # Verificando se a previsão é para uma categoria relacionada a elevadores
    for _, label, _ in decoded_preds:
        if "elevator" in label.lower():
            return True

    return False


# Exemplo de uso
image_path = "C:/Users/Caio/Documents/Tcc/Redimensiona/imagem_redimensionada/foto2.png"
is_elevator_image = is_elevator(image_path)
print(
    "É uma imagem de elevador?"
    if is_elevator_image
    else "Não é uma imagem de elevador."
)
