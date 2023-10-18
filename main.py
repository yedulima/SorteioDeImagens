import json
import os
import shutil
import cv2

def recorteImagem(imagePath: str, x1: int, x2: int, y1: int, y2: int) -> None:
    img = cv2.imread(imagePath)

    img_cropped = img[y1:y2, x1:x2]

    cv2.imshow('image', img)
    cv2.imshow('image cropped', img_cropped)

    cv2.waitKey(0)

    

if __name__ == "__main__":

    # shutil.copy2('./ata.txt', './new_dataset')
    # Para copiar e colar
    
    with open('./new_dataset.json', 'r') as file:
        dataset = json.load(file)
    
    for infos in dataset:
        if infos['network_id'] == "62e96c3b77aa054ad7af6f23":
            
            # Caminho da imagem será o caminho dela mais a data e a página
            imagePath = os.path.join(f"./{infos['network_id']}", infos['created'], f"{'_'.join([infos['leaflet_id'], 'page' + str(infos['page'])])}.jpg")
            x1, x2 = infos['x1'], infos['x2']
            y1, y2 = infos['y1'], infos['y2']

            recorteImagem(imagePath, x1, x2, y1, y2)
            break