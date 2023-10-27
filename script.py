import json
from random import sample

def getJson(path: str) -> list:
    '''
    Pega Json
    '''
    return json.load(open(path, 'r'))

def getRandom(file: list, n: int) -> list:
    '''
    Pega itens aleatórios do json com base
    na quantidade fornecida
    '''
    return sample(file, n)

def writeFile(netWork: list, fileName: str) -> None:
    '''
    Cria arquivo com os dados aleatoriamente
    pegues
    '''
    with open(f'./{fileName}.json', 'w') as file:
        json.dump(netWork, file)

if __name__ == '__main__':
    
    path = './recortes.json'
    qtd = 7000
    filename = 'new_dataset'

    writeFile(getRandom(getJson(path), qtd), filename)