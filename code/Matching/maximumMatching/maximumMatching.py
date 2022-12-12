import pickle


def getDictionary(path2Dictionary='code/matching/maximumMatching/Dictionary.pkl'):
    list_Words = pickle.load(open(path2Dictionary, 'rb'))
    return list_Words


def maximumMatching(sentence, maxlen=4):

    dictionary = getDictionary()

    my_list = []
    list_Words = sentence.split()
    len_now = len(list_Words)
    i = 0
    maxl = maxlen
    while i < len_now:
        wordCheck = '_'.join(list_Words[i:maxlen + i])

        while wordCheck not in dictionary:
            #  print(wordCheck)
            if maxl > 1:
                wordCheck = '_'.join(list_Words[i:i + maxl])
            elif maxl == 1:
                wordCheck = list_Words[i]
            elif maxl == 0:
                break
            maxl -= 1
        if maxl > 0:
            i += maxl
        i += 1
        #  print('TRUE {} | Len: {}'.format(wordCheck, maxl))
        my_list.append(wordCheck)
        maxl = min(len_now - i, maxlen)

    line = ' '.join(my_list)

    return line


def maximumsMatching(lines, maxlen=4):

    dictionary = getDictionary()

    list_Tokenizer = []
    for line in lines:
        my_list = []
        list_Words = line.split()
        len_now = len(list_Words)
        i = 0
        maxl = maxlen
        while i < len_now:
            wordCheck = '_'.join(list_Words[i:maxlen + i])

            while wordCheck not in dictionary:
                #  print(wordCheck)
                if maxl > 1:
                    wordCheck = '_'.join(list_Words[i:i + maxl])
                elif maxl == 1:
                    wordCheck = list_Words[i]
                elif maxl == 0:
                    break
                maxl -= 1
            if maxl > 0:
                i += maxl
            i += 1
            #  print('TRUE {} | Len: {}'.format(wordCheck, maxl))
            my_list.append(wordCheck)
            maxl = min(len_now - i, maxlen)

        list_Tokenizer.append(' '.join(my_list))

    return list_Tokenizer