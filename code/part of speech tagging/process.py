from collections import defaultdict

import sys
sys.path.insert(1, 'code/lexicon')
from vocab import getVocabDict
from read_data import preprocess

#-----training-----------------------------------
def seperate_word_tag(word_tag, vocabs_dict): 
    if not word_tag.split():
        word = '--n--'
        tag = '--s--'
    else:
        word, tag = word_tag.split()
        if word not in vocabs_dict: word = '--unk--'
    return word, tag

def create_dictionaries(train_gold, vocab):
    emission_counts = defaultdict(int)
    transition_counts = defaultdict(int)
    tag_counts = defaultdict(int)
    
    prev_tag = '--s--' 
    for word_tag in train_gold:
        word, tag = seperate_word_tag(word_tag, vocab) 
        
        transition_counts[(prev_tag, tag)] += 1
        emission_counts[(tag, word)] += 1
        tag_counts[tag] += 1
        prev_tag = tag
    return transition_counts, emission_counts, tag_counts
vocabDict = getVocabDict()
gold = open('data/root/vncore_labeling.txt', encoding='utf-8').readlines()
transition_counts, emission_counts, tag_counts = create_dictionaries(gold, vocabDict)
states = sorted(tag_counts.keys())
print('Số nhãn:', len(states))
print(states)
#--------testing-----------------------------------------
def predict_pos(words, gold, emission_counts, vocabs_dict, states):
    num_correct = 0
    all_words = set(emission_counts.keys())
    
    for word, gold_tuple in zip(words, gold): 
        gold_tuple_list = gold_tuple.split()
        if len(gold_tuple_list) != 2: 
            continue
        else: 
            true_label = gold_tuple_list[1]
    
        count_final = 0
        pos_final = ''
        if word not in vocabs_dict: 
            continue
        for pos in states:
            if (pos, word) not in emission_counts: continue
            count = emission_counts[(pos, word)]
            
            if count > count_final:
                count_final = count
                pos_final = pos
                    
        if pos_final == true_label: 
            num_correct += 1
    accuracy = num_correct / len(gold)
    return accuracy
vocabs_dict = getVocabDict()
train_words = preprocess(vocabs_dict, 'data/root/word_separation.txt')
accuracy = predict_pos(train_words, gold, emission_counts, vocabs_dict, states)
print('Độ chính xác trên bộ dữ liệu:', accuracy)