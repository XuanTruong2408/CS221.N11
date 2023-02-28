label_true = ['N', 'V', 'V', 'M', 'N', 'N', 'A', 'V', 'A', 'N', 'N', 'CH', 'N', 'FL', 'FL', 'N', 'R', 'V', 'E', 'N', 'V', 'N', 'A', 'Cc', 'A', 'CH', 'D', 'N', 'N', 'R', 'V', 'V', 'CH', 'V', 'C', 'V', 'N', 'CH', 'E', 'N', 'N', 'CH', 'V', 'E', 'M', 'N', 'N', 'M', 'Nu', 'CH', 'N', 'V', 'Nc', 'N', 'Ni', 'Np', 'R', 'V', 'N', 'N', 'V', 'CH']
label_pred = []

with open('data/root/vncore_labeling_test_pred.txt', 'r') as f:
    data = f.read()
    data = data.replace('\n','')
    label_pred = data.split('\t')
    label_pred = label_pred[1:]
print(label_pred)
print(label_true)

from sklearn.metrics import classification_report
def report(pred, gold):
        
    print(classification_report(pred, gold))
    print('y_pred:', pred)
    print('y_true:', gold)
print(len(label_pred), len(label_true))
print('Kết quả của mô hình vncore:\n')
report(label_pred, label_true)