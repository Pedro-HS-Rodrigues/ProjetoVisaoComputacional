import cv2
import easyocr

def extract(image_path):
    
    reader = easyocr.Reader(['en'])

    
    img = cv2.imread(image_path)

    
    window_name = "Imagem Original"
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window_name, 400, 200)
    cv2.imshow(window_name, img)
    cv2.waitKey(3000)
    cv2.destroyAllWindows()

    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    
    window_name = "Escala de Cinza"
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window_name, 400, 200)
    cv2.imshow(window_name, gray)
    cv2.waitKey(3000)
    cv2.destroyAllWindows()

    
    result = reader.readtext(gray)

    
    valid_texts = []

    for detection in result:
        texto = detection[1].replace(" ", "") 
        texto = texto.replace("(", "").replace(")", "").replace("!", "").replace("/", "").replace("|", "").replace(":", "")
        if len(texto) == 7: 
            valid_texts.append(texto)

    return valid_texts 
