string = ' '.join(input("Enter some words: ").split())
listt = string.split()
for i in set(listt):
    print(i, 'Occurs:',listt.count(i), 'Times')
