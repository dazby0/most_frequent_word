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