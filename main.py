# import sys
#
#
# if __name__ == '__main__':
#     try:
#         with open("pan_tadeusz.txt", "r", encoding="UTF-8") as f:
#             text = f.read()
#     except:
#         print('There is a problem with file')
#         sys.exit()
#
#     threw_words = ["w", "i", "o", "na", "to", "po", "te", "ale", "nie", "się", "aby", "żeby", ".", ",", ";", ":", "\n",
#                    "?", "!"]
#     clear_text = ""
#
#     for lit in text:
#         if lit.isalpha() or lit == " ":
#             clear_text += lit
#
#     words = [t.lower() for t in clear_text.split() if t not in threw_words]
#
#     counted = {}
#     for word in words:
#         if word in counted:
#             counted[word] += 1
#         else:
#             counted[word] = 1
#
#     min = 1
#     for word in counted:
#         if counted[word] > min:
#             print(f'Słowo {word} wystepuje w tekscie {counted} razy.')


# import re
# from collections import Counter
#
# if __name__ == '__main__':
#     words = re.findall('r', open("pan_tadeusz.txt", encoding="UTF-8").read().lower())
#     count = Counter(words).most_common(5)
#     print(count)


# if __name__ == '__main__':
#     count = 0
#     word = 0
#     maxcount = 0
#     words = []
#
#     with open("pan_tadeusz.txt", "r", encoding="UTF-8") as file:
#         for line in file:
#             string = line.lower().replace(","," ").replace(","," ").split(" ")
#             for s in string:
#                 words.append(s)
#         for i in range(0, len(words)):
#             count = 1
#             for j in range(i+1, len(words)):
#                 if(words[i] == words[j]):
#                     count += 1
#             if(count > maxcount):
#                 maxcount = count
#                 word = words[i]
#         print(f'Most frequent word is {word}')




def sort(dict_list):
    count = 0
    for k, w in dict_list[:20]:
        count += 1
        print(count, ":::", k, ":::", w, "razy")
        print("----------------------------------------")

if __name__ == '__main__':
    dictionary = {}
    words = open('pan_tadeusz.txt', 'r', encoding="UTF-8")
    for t in words:
        t = t.strip('\n').lower()
        word_list = t.split()
        for w in word_list:
            w = w.strip(',.;:?!')
            if len(w) > 5:
                dictionary.setdefault(w, 0)
                dictionary[w] += 1
    words.close()

    dictionary_list = dictionary.items()
    sort_dictionary_list = sorted(dictionary_list, key=lambda p: p[1], reverse=True)
    print("\n20 najczesciej wystepujacych slow to: ")
    sort(sort_dictionary_list)