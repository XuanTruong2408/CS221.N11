import maximumMatching as MM

list_sentences = []

with open('data/root/raw.txt', 'r') as f:
    data = f.read()
    sentences = data.split('\n')
    list_sentences = MM.maximumsMatching(sentences)
    
with open('data/output/matching.txt', 'w') as f:
    for s in list_sentences:
        f.write(s)
        f.write('\n')
