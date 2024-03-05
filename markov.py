"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    file_name = open(file_path).read()
   
    return file_name
   

def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    
    words = text_string.split() # [word, word, word]
    for i in range(len(words)-2): 
        current_word = words[i] 
        next_word = words[i + 1]
        chain = (current_word, next_word) #dictionary[key]
        if chain in chains:
            chains[chain].append(words[i + 2])
        else:
            chains[chain]= [words[i + 2]]


    return chains


def make_text(chains):
    """Return text from chains."""

    chains_keys = list(chains.keys())
    link = choice(chains_keys)
    random_word = choice(chains[link])
    words = [link[0], link[1], random_word]
    if (link[1], random_word) in chains:
        random_word = choice(chains[(link[1], random_word)])
        words.append(random_word)

    print(words)
    # return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)
print(chains)

# Produce random text
random_text = make_text(chains)

print(random_text)
