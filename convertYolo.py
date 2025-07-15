import os
from PIL import Image

def corners_to_bbox(corner_points):
    xs = [int(p.split(",")[0]) for p in corner_points]
    ys = [int(p.split(",")[1]) for p in corner_points]
    x_min, x_max = min(xs), max(xs)
    y_min, y_max = min(ys), max(ys)
    return x_min, y_min, x_max, y_max

def normalize_bbox(x_min, y_min, x_max, y_max, img_w, img_h):
    x_center = (x_min + x_max) / 2 / img_w
    y_center = (y_min + y_max) / 2 / img_h
    width = (x_max - x_min) / img_w
    height = (y_max - y_min) / img_h
    return x_center, y_center, width, height

def convert_labels(split, labels_dir, images_dir, output_dir, image_ext=".png"):
    label_input = os.path.join(labels_dir, split)
    image_input = os.path.join(images_dir, split)
    label_output = os.path.join(output_dir, split)
    os.makedirs(label_output, exist_ok=True)

    for file in os.listdir(label_input):
        if not file.endswith(".txt"):
            continue

        txt_path = os.path.join(label_input, file)
        img_path = os.path.join(image_input, file.replace(".txt", image_ext))

        if not os.path.exists(img_path):
            print(f"Imagem não encontrada para {file}, pulando.")
            continue

        with Image.open(img_path) as img:
            img_w, img_h = img.size

        with open(txt_path, "r") as f:
            lines = f.readlines()

        yolo_lines = []

        # Converter a placa (classe 0)
        for line in lines:
            if line.startswith("corners:"):
                corners = line.split(":")[1].strip().split()
                x_min, y_min, x_max, y_max = corners_to_bbox(corners)
                x, y, w, h = normalize_bbox(x_min, y_min, x_max, y_max, img_w, img_h)
                yolo_lines.append(f"0 {x:.6f} {y:.6f} {w:.6f} {h:.6f}")

        # Converter cada caractere (classe 1)
        for line in lines:
            if line.strip().startswith("char"):
                parts = line.split(":")[1].strip().split()
                if len(parts) != 4:
                    continue
                x, y, w, h = map(int, parts)
                x_center = (x + w / 2) / img_w
                y_center = (y + h / 2) / img_h
                w /= img_w
                h /= img_h
                yolo_lines.append(f"1 {x_center:.6f} {y_center:.6f} {w:.6f} {h:.6f}")

        # Salvar no formato YOLO
        with open(os.path.join(label_output, file), "w") as out:
            for line in yolo_lines:
                out.write(line + "\n")

        print(f"[✓] Convertido: {file}")

# Caminhos raiz
labels_dir = "D:/UFPR-ALPR dataset/dataset/labels"
images_dir = "D:/UFPR-ALPR dataset/dataset/images"
output_dir = "D:/UFPR-ALPR dataset/dataset/labels-yolo"

for split in ["train", "val", "test"]:
    convert_labels(split, labels_dir, images_dir, output_dir)
