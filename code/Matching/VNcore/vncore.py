from vncorenlp import VnCoreNLP

rdrsegmenter = VnCoreNLP("code\Matching\VNcore\VnCoreNLP\VnCoreNLP-1.1.1.jar",
                         annotators="wseg, pos",
                         max_heap_size='-Xmx1g')


def wordTokenzizer(sentence):
    token = [i for j in rdrsegmenter.tokenize(sentence) for i in j]
    return ' '.join(token)


def wordsTokenzizer(path2Raw):
    list_LinesTokens = []
    with open(path2Raw, 'r') as f:
        data = f.read()

        list_Lines = data.split('\n')
        for line in list_Lines:
            token = [i for j in rdrsegmenter.tokenize(line) for i in j]
            list_LinesTokens.append(' '.join(token))

    return list_LinesTokens
