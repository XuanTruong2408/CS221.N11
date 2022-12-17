from vncorenlp import VnCoreNLP
rdrsegmenter = VnCoreNLP("code\Matching\VNcore\VnCoreNLP\VnCoreNLP-1.1.1.jar",
                         annotators="wseg,pos",
                         max_heap_size='-Xmx1g')


path = 'data/root/vncore_matching.txt'


def Hand(path):
    list_Tokens = []
    with open(path, 'r', encoding="utf-8") as f:
        data = f.read()
        lines = data.split('\n')

    tokens = []
    for i in lines:
        token = i.split()
        tokens.append(token)

    for i in tokens:
        list_Tokens.extend(i)
    return list_Tokens


manual_tokens = Hand(path)

with open('data/output/vncore_labeling.txt', 'w', encoding='utf-8') as f:
    for word in manual_tokens:
        word = word.replace('\n', '')

        if '_' not in word:
            tag = rdrsegmenter.pos_tag(word)
        else:
            tag = rdrsegmenter.pos_tag(word.replace('_', ' '))

        if tag == []:
            f.write('\n')
        else:
            f.write(f'{word}\t{tag[0][0][1]}\n')
    f.write('\n')
