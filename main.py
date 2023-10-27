import json
import os
import shutil
import cv2

def recorteImagem(imagePath: str, x1: int, x2: int, y1: int, y2: int) -> None:
    global error_files

    try:
        img = cv2.imread(imagePath)

        img_cropped = img[y1:y2, x1:x2]

        cv2.imwrite(os.path.join('./images_recorts', imagePath.split('\\')[4]), img_cropped)
    except:
        error_files[imagePath.split('\\')[0]] = 0

if __name__ == "__main__":

    # shutil.copy2('./ata.txt', './new_dataset')
    # Para copiar e colar

    error_files = {}
    
    with open('./new_dataset.json', 'r') as file:
        dataset = json.load(file)
    
    for infos in dataset:
        #if infos['network_id'] == "62e96c3b77aa054ad7af6f23":

        imagePath = '.\images'

        infor = ['network_id', 'created', 'leaflet_id']
        
        for _ in infor:
            if _ in infos:
                if _ == 'created':
                    imagePath = os.path.join(imagePath, str(infos[_])[:7])
                else:
                    imagePath = os.path.join(imagePath, str(infos[_]))

        imagePath += f"_page{infos['page']}.jpg"

        x1, x2 = infos['x1'], infos['x2']
        y1, y2 = infos['y1'], infos['y2']

        recorteImagem(imagePath, x1, x2, y1, y2)
            #break
    
        '''
        if infos['network_id'] == '58d3db8b268c327930aca282':
            for _ in infos:
                if _ == 'created':
                    print(_, infos[_][:7])
                else:
                    print(_, infos[_])
            break
        '''

    #json.dump(error_files, open('ata.json', 'w'))