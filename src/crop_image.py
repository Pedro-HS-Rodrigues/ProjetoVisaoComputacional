import cv2
import os
import shutil

def crop_and_save_plate(image_path, plate_box):
    cropped_dir = "src/cropped"
    if os.path.exists(cropped_dir):
        shutil.rmtree(cropped_dir)
    
    os.makedirs(cropped_dir)

    img = cv2.imread(image_path)
    h, w, _ = img.shape
    padding = 25

    x_center, y_center, width, height = plate_box
    x1 = int((x_center - width / 2) * w) - padding
    y1 = int((y_center - height / 2) * h)  
    x2 = int((x_center + width / 2) * w) + padding
    y2 = int((y_center + height / 2) * h)

    cropped_img = img[y1:y2, x1:x2]

    output_path = os.path.join(cropped_dir, f"cropped.jpg")
    cv2.imwrite(output_path, cropped_img)
    print(f"Imagem recortada salva em: {output_path}")
