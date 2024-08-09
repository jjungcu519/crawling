import codecs

positive = []
negative = []
posneg = []

pos = codecs.open("data/posi.txt", 'rb', encoding='UTF-8')

while True:
    line = pos.readline()
    line = line.replace('\n', '')
    positive.append(line)
    posneg.append(line)

    if not line: break        
pos.close()


neg = codecs.open("data/nega.txt", 'rb', encoding='UTF-8')

while True:
    line = neg.readline()
    line = line.replace('\n', '')
    negative.append(line)
    posneg.append(line)
    
    if not line: break
neg.close()