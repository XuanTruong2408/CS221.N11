import A_transition
import B_emission
import Viterbi
from collections import defaultdict
import pandas as pd
import numpy as np
import sys
sys.path.insert(1, 'code/lexicon')

from vocab import getVocabDict
from read_data import preprocess

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


vocabs_dict = getVocabDict()
gold = open('data/root/word_POStagging.txt', encoding='utf-8').readlines()
transition_counts, emission_counts, tag_counts = create_dictionaries(gold, vocabs_dict)
states = sorted(tag_counts.keys())

train_words = preprocess(vocabs_dict, 'data/root/word_separation.txt')

alpha = 0.001
for i in range(len(states)): tag_counts.pop(i, None)
    
A = A_transition.create_transition_matrix(alpha, tag_counts, transition_counts)
df = pd.DataFrame(
    A[5:10, 5:10], 
    index = states[5:10], 
    columns = states[5:10]
)
print(df.head())

cidx  = ['tuần', 'trưởng_thành', 'than_ôi', 'đảng_uỷ', 'thống_nhất']
rvals = ['N', 'V', 'CH', 'Cc', 'E', 'A']
cols = [vocabs_dict[word] for word in cidx]
rows = [states.index(tag) for tag in rvals]
print(states)

for i in range(len(states)): tag_counts.pop(i, None)
B = B_emission.create_emission_matrix(alpha, tag_counts, emission_counts, list(vocabs_dict))

df = pd.DataFrame(B[np.ix_(rows, cols)], index=rvals, columns=cidx)
print(df.head())

A = np.array([sublist[1:].tolist() for sublist in A])
B = B[1:]

best_probs_train, best_paths_train = Viterbi.viterbi_initialize(states, tag_counts, A, B, train_words, vocabs_dict)
print('best_probs_train[0, 0]:', best_probs_train[0, 0]) 
print('best_paths_train[2, 3]:', best_paths_train[2, 3])

best_probs_train, best_paths_train = Viterbi.viterbi_forward(A, B, train_words, best_probs_train, best_paths_train, vocabs_dict)
print('best_probs_train[0, 1]:', best_probs_train[0, 1]) 
print('best_paths_train[0, 4]:', best_paths_train[0, 4])

train_pred = Viterbi.viterbi_backward(best_probs_train, best_paths_train, train_words, states)
m = len(train_pred)

print(f'Dự đoán cho train_pred[-7:{m - 1}]:')
print(train_words[-7:m-1])
print(train_pred[-7:m-1])

print('Dự đoán cho train_pred[0:7]:')
print(train_words[0:7])
print(train_pred[0:7])

for word, tag in zip(train_words, train_pred):
    if word == '--n--': print()
    else: print(f'{word}/{tag}', end=' ')
    
from sklearn.metrics import classification_report
def report(pred, gold):
    y_pred = []
    y_true = []

    for prediction, word_tag in zip(pred, gold):
        word_tag_tuple = word_tag.split()
        if len(word_tag_tuple) != 2: continue 

        word, tag = word_tag_tuple
        y_pred.append(prediction)
        y_true.append(tag)
        
    print(classification_report(y_pred, y_true))
    print('y_pred:', y_pred)
    print('y_true:', y_true)
    return y_pred, y_true

print('Kết quả của mô hình Hidden Markov kết hợp thuật toán Viterbi trên tập train:\n')
y_pred, y_true_train = report(train_pred, gold)