def find_min(items:list):
    m=items[0]
    for i in items:
        if i<m:
            m=i
    return m

def odd_increment_even_decrement_no_modify(items) -> list:
    result=[]
    for i in items:
        result.append(i+1 if i%2!=0 else i-1)
    return result

def odd_square_even_double_modify(items)-> list:
    for i in items:
        items[i]= i**2 if i%2!=0 else i*2 
    return items

def more_than_two_unique_vowels(sentence):

    vowels = set("aeiou")
    words = set()
    for word in sentence.split(","):
        if len(set(word) & vowels)>2:
            words.add(word)
    return words

def sum_of_list_of_lists(lol):

    total = 0
    for row in lol:
        for n in row:
            total+=n
    return total

def flatten(lol):

    flat = []
    for row in lol:
        for item in row:
            flat.append(item)
    return flat

def all_common(strings):

    common_chars = set(strings[0])
    for string in strings[1:]:
        common_chars &= set(string)
    return ''.join(sorted(common_chars))

def vocabulary(sentences):

    vocab = set()
    for sentence in sentences:
        for word in sentence.split(" "):
            vocab.add(word.lower())
    return vocab
