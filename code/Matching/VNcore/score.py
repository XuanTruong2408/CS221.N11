import vncore as VC

def testToken(path2Raw='data/root/raw.txt'):

    list_Tokens = []

    list_Tokens = VC.wordsTokenzizer(path2Raw)
    with open('data/output/matching_vncore_test.txt', 'w') as f:
        for line in list_Tokens:
            f.write(line)
            f.write('\n')
    
    with open('data/root/word_separation_1.txt', 'r') as f:
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
