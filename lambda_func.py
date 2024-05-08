def sort_by_len(element):
    return len(element)

sorts = lambda element: len(element)

print(sorts('banana'))

fruits = ["banana", "apple", "carrotsa", "potato"]

longest_word = max(fruits, key=lambda element: len(element))

print(longest_word)
