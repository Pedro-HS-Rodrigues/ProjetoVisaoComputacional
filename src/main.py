import os
from detect_plate import detect_plate
from crop_image import crop_and_save_plate
from extract import extract
from display_image import display_images
import cv2


def process_image(image_path):
    img = cv2.imread(image_path)
    cv2.imshow("Imagem Original", img)
    cv2.waitKey(3000)
    cv2.destroyAllWindows()
    image_name = os.path.splitext(os.path.basename(image_path))[0]

    detect_plate(image_path)

    txt_path = f"src/detections/{image_name}/labels/{image_name}.txt"
    with open(txt_path, "r") as f:
        lines = f.readlines()

    plate_box = [line.strip().split()[1:] for line in lines if line.startswith("0")][0]
    plate_box = list(map(float, plate_box))

    crop_and_save_plate(image_path, plate_box)

    detection_img_path = f"src/detections/{image_name}/{image_name}.jpg"
    detection_img = cv2.imread(detection_img_path)

    if detection_img is None:
        print(f"Erro ao carregar a imagem de detecção: {detection_img_path}")
        return

    cropped_img = cv2.imread("src/cropped/cropped.jpg")
    if cropped_img is None:
        print(f"Erro ao carregar a imagem cortada.")
        return

    valid_texts = extract("src/cropped/cropped.jpg")
    if len(valid_texts) == 0:
        print("Texto não encontrado")
        return

    valid_texts = (valid_texts[0]).upper()

    display_images(img, detection_img, cropped_img, valid_texts)



def main():
    images_folder = "src/images"
    image_files = [f for f in os.listdir(images_folder) if f.endswith(('.jpg', '.png'))] 

    for image_file in image_files:
        image_path = os.path.join(images_folder, image_file)
        process_image(image_path)


if __name__ == "__main__":
    main()
