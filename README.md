# Grey Scale
---

# Processamento de Imagens com OpenCV

Este projeto realiza operações básicas de processamento de imagem usando a biblioteca [OpenCV](https://opencv.org/). Ele lê uma imagem, converte para tons de cinza e aplica uma binarização utilizando o método de Otsu.

## Requisitos

* Python 3.x
* OpenCV (`cv2`)

Você pode instalar o OpenCV com:

```bash
pip install opencv-python
```

## Imagem de entrada

Certifique-se de que o arquivo `gatito.jpg` esteja no mesmo diretório do script Python, ou ajuste o caminho no código para apontar corretamente para a imagem desejada.

## Como executar

Execute o script com:

```bash
python nome_do_arquivo.py
```

## Etapas do processamento

1. **Leitura da imagem**
   Carrega a imagem `gatito.jpg`.

2. **Exibição da imagem original**
   Abre uma janela com a imagem original.

3. **Conversão para escala de cinza**
   Converte a imagem para tons de cinza usando `cv2.cvtColor`.

4. **Binarização com Otsu**
   Aplica a binarização automática com o método de Otsu via `cv2.threshold`.

5. **Exibição das imagens processadas**
   Exibe janelas com:

   * Imagem original
   * Imagem em tons de cinza
   * Imagem binarizada

6. **Finalização**
   Aguarda pressionamento de tecla para encerrar todas as janelas com `cv2.destroyAllWindows`.

## Exemplo de uso

```python
img = cv2.imread('gatito.jpg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, binary_img = cv2.threshold(gray_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
```
---
