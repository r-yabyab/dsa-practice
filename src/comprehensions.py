def main():
    pass

def list_comprehension():
    list_comp = [x for x in range(1, 5)]
    print(list_comp)

def dict_comprehension():
    data = {
        "a": 5,
        "b": 12,
        "c": 20
    }
    words = ["apple", "cat", "tree", "water"]
    print(data.items())
    
    data_filtered = {k : v for k,v in data.items() if v>10}
    print(data_filtered)
    word_index = {word:i for i, word in enumerate(words)}
    print(word_index)


dict_comprehension()