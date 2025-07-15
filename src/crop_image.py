import cv2
import os
import shutil

def crop_and_save_plate(image_path, plate_box):
    # Caminho para salvar a imagem recortada
    cropped_dir = "src/cropped"
     # Limpar o conteúdo da pasta 'cropped' se já existir
    if os.path.exists(cropped_dir):
        # Remover todos os arquivos e pastas dentro de 'cropped'
        shutil.rmtree(cropped_dir)
    
    # Criar a pasta novamente
    os.makedirs(cropped_dir)

    # Carregar a imagem
    img = cv2.imread(image_path)
    h, w, _ = img.shape
    padding = 25

    # Calcular as coordenadas absolutas da caixa da placa
    x_center, y_center, width, height = plate_box
    x1 = int((x_center - width / 2) * w) - padding  # Adicionando padding
    y1 = int((y_center - height / 2) * h)  
    x2 = int((x_center + width / 2) * w) + padding  # Adicionando padding
    y2 = int((y_center + height / 2) * h)

    # Recortar a imagem da placagit
    cropped_img = img[y1:y2, x1:x2]

    # Salvar a imagem recortada
    output_path = os.path.join(cropped_dir, f"{os.path.basename(image_path)}")
    cv2.imwrite(output_path, cropped_img)
    print(f"Imagem recortada salva em: {output_path}")
