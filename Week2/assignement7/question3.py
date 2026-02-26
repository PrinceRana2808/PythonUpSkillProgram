def repeat_word(word, times):
    for _ in range(times):
        yield word

for w in repeat_word("hello", 5):
    print(w)