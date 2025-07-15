import os
import subprocess
from detect_plate import detect_plate
from crop_image import crop_and_save_plate

def main():
    # Caminho para a imagem a ser processada
    image_path = "src/images/image6.jpg"  # Altere para o caminho correto
    image_name = os.path.splitext(os.path.basename(image_path))[0]

    # Chamar o YOLOv5 para detectar a placa e gerar o arquivo .txt
    detect_plate(image_path)

    # Lendo as coordenadas da placa do arquivo .txt
    txt_path = "src/detections/{}/labels/{}.txt".format(image_name,image_name)  # Assumindo que o nome da imagem e do .txt são iguais
    with open(txt_path, 'r') as f:
        lines = f.readlines()
    
    # Extraímos a linha da placa (classe 0)
    plate_box = [line.strip().split()[1:] for line in lines if line.startswith('0')][0]
    plate_box = list(map(float, plate_box))  # Convertendo as coordenadas para float
    
    # Chamar o recorte da imagem da placa e salvar na pasta cropped
    crop_and_save_plate(image_path, plate_box)

if __name__ == "__main__":
    main()
