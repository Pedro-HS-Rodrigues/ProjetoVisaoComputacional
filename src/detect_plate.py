import subprocess
import os
import shutil

def detect_plate(image_path):
    # Extrair o nome da imagem sem a extensão
    image_name = os.path.splitext(os.path.basename(image_path))[0]
    
    # Caminho para a pasta de deteções
    detections_dir = "src/detections"

    # Limpar o conteúdo da pasta 'detections' se já existir
    if os.path.exists(detections_dir):
        # Remover todos os arquivos e pastas dentro de 'detections'
        shutil.rmtree(detections_dir)

    os.makedirs(detections_dir)
    # Rodar o YOLOv5 para detectar a placa e gerar o arquivo .txt
    command = [
        "python", "yolov5/detect.py", 
        "--weights", "yolov5/runs/train/placas_char_model2/weights/best.pt",  # Caminho para o peso treinado
        "--img", "640", 
        "--source", image_path,
        "--save-txt",  # Garante que o arquivo .txt será gerado
        "--project", "src/detections",  # Diretório principal de saída
        "--name", image_name  # Usar o nome da imagem para a subpasta sem criar pastas extras
    ]
    
    # Executa o comando YOLOv5
    subprocess.run(command)

    print(f"Detecção concluída para: {image_path}")
