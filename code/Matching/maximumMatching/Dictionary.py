import pickle

def createDict(path2Data='data/root/word_separation.txt'):

    with open(path2Data,'r') as f:
        data = f.read()
        list_Words = data.replace('\n', ' ').split()

        list_Words = list(set(list_Words))

    return list_Words


list_Words = createDict()

#Print Dictionary
print(list_Words)
pickle.dump(list_Words, open('code/Matching/Dictionary.pkl','wb'))