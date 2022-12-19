with open('data/root/vncore_labeling.txt', 'r') as f:
    data = f.read()
    data = data.replace('.\tCH', '.\tCH\n')
print(data)
with open(r"data/root/vncore_labeling.txt", 'w') as f:
    f.write(data)