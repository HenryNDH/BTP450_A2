def wordCount(t):
    word_dict = {}
    line_num = 1
    with open(t, 'r') as file:
        for line in file:
            words = line.strip().split()
            for word in words:
                if word in word_dict:
                    if line_num not in word_dict[word]:
                        word_dict[word].append(line_num)
                else:
                    word_dict[word] = [line_num]
            line_num += 1
    return word_dict

print(wordCount('wordCount.txt'))
