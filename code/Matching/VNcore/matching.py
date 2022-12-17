import vncore as VC

list_sentences = []

list_sentences = VC.wordsTokenzizer('data/root/raw.txt')    
with open('data/root/vncore_matching.txt', 'w') as f:
    for s in list_sentences:
        f.write(s)
        f.write('\n')
