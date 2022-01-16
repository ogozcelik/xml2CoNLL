import re

sentences, connl = [], []

with open('read.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        if line not in ['<doc>', '</doc>']:
            sentences.append(line)

for sentence in sentences:
    tag1 = re.findall(r'<tag1>(.+?)</tag1>', sentence)
    tag2 = re.findall(r'<tag2>(.+?)</tag2>', sentence)
    tag3 = re.findall(r'<tag3>(.+?)</tag3>', sentence)
    splitted = re.split('<tag1>|</tag1>|<tag2>|</tag2>|<tag3>|</tag3>', sentence)  # splitted considering tags
    if tag1 or tag2 or tag3:  # if any tag in sentence
        for split in splitted:  # search each index
            if split in tag1:
                counter = 0
                for token in split.split():
                    if counter > 0:
                        connl.append(token + ' I-TAG1')
                    else:
                        connl.append(token + ' B-TAG1')
                    counter += 1

            elif split in tag2:
                counter = 0
                for token in split.split():
                    if counter > 0:
                        connl.append(token + ' I-TAG2')
                    else:
                        connl.append(token + ' B-TAG2')
                    counter += 1

            elif split in tag3:
                counter = 0
                for token in split.split():
                    if counter > 0:
                        connl.append(token + ' I-TAG3')
                    else:
                        connl.append(token + ' B-TAG3')
                    counter += 1

            else:  # current word is not an entity
                for token in split.split():
                    connl.append(token + ' O')

    else:  # if no entity in sentence
        for word in sentence.split():
            connl.append(word + ' O')

    connl.append('')

with open('output.txt', 'w', encoding='utf-8') as output:
    for element in connl:
        output.write(element + "\n")