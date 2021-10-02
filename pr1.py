#frequency count
text = input("enter text\n")
my_dict = {}
word_list = text.split()
for words in word_list:
    if (words[-1] == '.' or words[-1] == ','):
        words = words[0:len(words) - 1]
    if words in my_dict:
        my_dict[words] += 1
    else:
        my_dict.update({words: 1})

#Print the dictionary
for key, value in my_dict.items():
    print('Frequency of', key, ':', value)
