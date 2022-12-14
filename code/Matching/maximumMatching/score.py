import maximumMatching as MM

def testToken(path2Raw='data/root/raw.txt'):

    sentences =[]
    with open(path2Raw, 'r', encoding= 'utf-8') as f:
        data = f.read()
        sentences = data.split('\n')

    list_Tokens = MM.maximumsMatching(sentences)
    with open('data/output/matching_mm_test.txt', 'w', encoding= 'utf-8') as f:
        for line in list_Tokens:
            f.write(line)
            f.write('\n')

    with open('data/root/word_separation.txt', 'r', encoding= 'utf-8') as f:
        data_gold = f.read()
        list_Golds = data_gold.split('\n')

    ave = 0
    for idx in range(len(list_Tokens)):
        num_words = len(list_Golds[idx].split())
        num_gold = list_Golds[idx].count('_')
        num_token = list_Tokens[idx].count('_')

        sub = abs(num_gold - num_token)
        ave += (num_words - 2*sub)/num_words
        print(idx + 1, (num_words - 2*sub)/num_words)

    ave /= len(list_Tokens)
    return ave

print(testToken())
