import maximumMatching as MM

list_sentences = []

with open('data/root/vncore_matching.txt', 'r') as f:
    data = f.read()
    sentences = data.split('\n')
    list_sentences = MM.maximumsMatching(sentences)
    
with open('data/output/maximum_matching_test_labeling.txt', 'w') as f:
    for s in list_sentences:
        f.write(s)
        f.write('\n')
