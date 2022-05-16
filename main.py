import re
import json

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

# keeps only alpha words of length <= 20 characters
def preprocess(path, out, MAX_LEN=20):

    with open(path) as f1:
        data = f1.read()

        with open(out, 'w') as f2:
            for item in data.splitlines():
                [word, freq] = item.split(' ')
                
                if re.match('^[a-z]+$', word) and len(word) <= MAX_LEN:
                    f2.write(item + '\n')

    print('done')

# converts preprocessed word + frequencies into dictionary
def text2dict(path):
    out = {}
    with open(path) as f:
        data = f.read()
        for item in data.splitlines():
            [word, freq] = item.split(' ')
            out[word] = int(freq)

    return out

# word_list is a list of (word, freq) tuples
# computes total frequencies of a given word list
def total_freq(word_list):
    return sum([ freq for w, freq in word_list ])

# writes computed probabilities
def write_json(path, probs):
    with open(path, 'w') as outfile:
        json.dump(probs, outfile)


# word_list is a list of (word, freq) tuples
# recursively creates datastructure of probabilities
def compute_probs(word_list):

    total = total_freq(word_list)
    words = [ w for w, _ in word_list ]
    
    # BASE CASE
    # if len(word_list) == 0: 
    #     return 1, {}

    # INDUCTIVE CASE
    # generate unique keys
    keys = list(set([ w[0] for w in words ]))
    probs = []
    values = []

    for key in keys:
        
        val = [ (w[1:], f) for w, f in word_list if w[0] == key ]
        freq = total_freq(val)
        prob = freq / total

        probs.append(prob)
        values.append(val)

    out = list(zip(keys, probs, values))
    print(out[0])

    # out = { keys[i]: compute_probs(values[i]) for i}


if __name__ == "__main__":
    
    PATH_1 = 'enwiki-20210820-words-frequency.txt'
    PATH_2 = 'processed-word-freq.txt'
    PATH_3 = 'letter-probabilities.json'

    # preprocess(PATH_1, PATH_2, 3)
    word_dict = text2dict(PATH_2)

    words = sorted(list(word_dict.keys()))
    words = [ (w, word_dict[w]) for w in words ]
    compute_probs(words)