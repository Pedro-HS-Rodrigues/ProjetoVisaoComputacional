import cv2
import pytesseract
import matplotlib.pyplot as plt

# Carregar a imagem da placa de carro
image_path = 'src/cropped/image1.jpg'
image = cv2.imread(image_path)

# Converter para escala de cinza
imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Aplicar OCR usando Tesseract
# Lembre-se de configurar o caminho para o Tesseract se necessário
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Caminho do Tesseract no seu sistema

# Realizar OCR
text = pytesseract.image_to_string(imageGray)

# Mostrar o texto extraído
print("Texto extraído:")
print(text)
