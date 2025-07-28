import subprocess
import os
import shutil

def detect_plate(image_path):
    
    image_name = os.path.splitext(os.path.basename(image_path))[0]
    
    detections_dir = "src/detections"

    if os.path.exists(detections_dir):
        shutil.rmtree(detections_dir)

    os.makedirs(detections_dir)
    command = [
        "python", "yolov5/detect.py", 
        "--weights", "yolov5/runs/train/placas_char_model2/weights/best.pt",
        "--img", "640", 
        "--source", image_path,
        "--save-txt", 
        "--project", "src/detections",
        "--name", image_name,
        "--view-img"
    ]
    
    subprocess.run(command)

    print(f"Detecção concluída para: {image_path}")
