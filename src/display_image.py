import cv2
import matplotlib.pyplot as plt

def display_images(original_img, detection_img, cropped_img, extracted_text):
    
    fig, axes = plt.subplots(1, 4, figsize=(20, 5))
    axes[0].imshow(cv2.cvtColor(original_img, cv2.COLOR_BGR2RGB))
    axes[0].set_title('Imagem Original')
    axes[0].axis('off')

    axes[1].imshow(cv2.cvtColor(detection_img, cv2.COLOR_BGR2RGB))
    axes[1].set_title('Imagem de Detecção')
    axes[1].axis('off')

    axes[2].imshow(cv2.cvtColor(cropped_img, cv2.COLOR_BGR2RGB))
    axes[2].set_title('Imagem Cortada')
    axes[2].axis('off')

    axes[3].text(0.5, 0.5, extracted_text, ha='center', va='center', fontsize=12)
    axes[3].set_title('Texto Extraído')
    axes[3].axis('off')

    plt.show(block=False)
    plt.pause(3) 
    plt.close() 
