__ALL__ = ['getVocabDict', 'checkVocab']


def getVocabDict():
    vocabs = open('code/lexicon/vocab.txt', encoding='utf-8').read().split('\n')
    vocabs_dict = {}
    index = 0

    for word in sorted(vocabs): 
        if word not in vocabs_dict: 
            vocabs_dict[word] = index  
            index += 1
    print('Số lượng từ vựng:', len(vocabs_dict.keys()))
    return vocabs_dict

def checkVocab():
    count = 0
    vocabs_dict = getVocabDict()
    for key, value in vocabs_dict.items():
        print(f'{key}: {value}')
        count += 1
        if count > 20: break