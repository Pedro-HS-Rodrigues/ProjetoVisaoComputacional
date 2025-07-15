import easyocr

# Inicializar o leitor EasyOCR
reader = easyocr.Reader(['en'])

# Carregar a imagem da placa de carro (já recortada)
image_path = 'src/cropped/image6.jpg'

# Realizar OCR
result = reader.readtext(image_path)

# Exibir o texto extraído
for detection in result:
    print(f"Texto detectado: {detection[1]}")
