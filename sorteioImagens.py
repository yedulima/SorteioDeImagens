from random import sample
import json

def serachImages(file: str, image_num: int) -> dict:
    return sample(json.load(open(file, 'r')), image_num)

def createDataset(sortedImages: dict) -> None:
    json.dump(sortedImages, open('new_dataset.json', 'w'))

if __name__ == "__main__":
    image_num = 3000
    file = './dataset.json' # Coloca o nome do json aqui

    sortedImages = serachImages(file, image_num)
    createDataset(sortedImages)