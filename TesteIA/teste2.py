import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models
from sklearn.model_selection import train_test_split

# Criar dados de exemplo (substitua por seus próprios dados)
# Aqui, assumiremos que você tem um conjunto de imagens de elevadores e não elevadores
# Certifique-se de ter suas próprias imagens de treinamento e seus rótulos correspondentes
# Neste exemplo, usaremos arrays de números aleatórios como substitutos para as imagens

# Número de exemplos e dimensões das imagens (substitua com suas próprias dimensões)
num_samples = 1000
image_height = 64
image_width = 64
num_channels = 3

# Gere dados de exemplo aleatórios
# 0: não é um elevador, 1: é um elevador
images = np.random.rand(num_samples, image_height, image_width, num_channels)
labels = np.random.randint(2, size=num_samples)

# Dividir os dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(
    images, labels, test_size=0.2, random_state=42
)

# Construir o modelo CNN
model = models.Sequential(
    [
        layers.Conv2D(
            32,
            (3, 3),
            activation="relu",
            input_shape=(image_height, image_width, num_channels),
        ),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation="relu"),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation="relu"),
        layers.Flatten(),
        layers.Dense(64, activation="relu"),
        layers.Dense(1, activation="sigmoid"),  # Saída binária (elevador ou não)
    ]
)

# Compilar o modelo
model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

# Treinar o modelo
model.fit(X_train, y_train, epochs=5, batch_size=32, validation_data=(X_test, y_test))

# Avaliar o modelo
loss, accuracy = model.evaluate(X_test, y_test)
print("Acurácia do modelo:", accuracy)

# Salvando o modelo
model.save("modelo_reconhecimento_elevadores.h5")
