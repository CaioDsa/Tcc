from PIL import Image
import os


def padronizar_tamanho_imagens(
    diretorio_entrada, diretorio_saida, tamanho_padrao=(224, 224)
):
    """
    Redimensiona imagens em um diretório de entrada e salva as imagens redimensionadas em um diretório de saída.

    Parâmetros:
    - diretorio_entrada (str): Caminho do diretório contendo as imagens originais.
    - diretorio_saida (str): Caminho do diretório onde as imagens redimensionadas serão salvas.
    - tamanho_padrao (tuple): Tamanho padrão para redimensionamento (largura, altura).
    """
    if not os.path.exists(diretorio_saida):
        os.makedirs(diretorio_saida)

    for filename in os.listdir(diretorio_entrada):
        if filename.endswith((".jpg", ".jpeg", ".png")):
            path_imagem_entrada = os.path.join(diretorio_entrada, filename)
            path_imagem_saida = os.path.join(diretorio_saida, filename)

            # Abrir a imagem
            img = Image.open(path_imagem_entrada)

            # Redimensionar para o tamanho padrão
            img_resized = img.resize(tamanho_padrao)

            # Salvar a imagem redimensionada
            img_resized.save(path_imagem_saida)


# Exemplo de uso
diretorio_entrada = "C:/Users/Caio/Documents/Tcc/Redimensiona/images"
diretorio_saida = "C:/Users/Caio/Documents/Tcc/Redimensiona/imagem_redimensionada"
tamanho_padrao = (224, 224)

padronizar_tamanho_imagens(diretorio_entrada, diretorio_saida, tamanho_padrao)
