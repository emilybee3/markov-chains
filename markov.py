from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    suess = open(file_path)
    text = suess.read()


    return text



def make_chains(text_string):
    """Takes input text as string; returns dictionary of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """
       #use .split to get a list of all the words

    chains = {}

    #for words in list

    suess_string = text_string.split()
    
    for i in range(len(suess_string) - 2):
        bigram = (suess_string[i], suess_string[i + 1])
        third_word = suess_string[i + 2]
        
        if bigram in chains:
            chains[bigram].append(third_word)
        else: 
            chains[bigram] = [third_word]

    return chains


#         #create bigrams 

#         #make bigrams keys in the dictionary
#         #make the thing after the bigram the value



# file_as_string = open_and_read_file("green-eggs.txt")
# chains = make_chains(file_as_string)

def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = []

    # your code goes here

    next_tup = choice(chains.keys())

    rand_val = choice(chains[next_tup]) 


 
    while next_tup in chains: 

        new_choice = choice(chains[next_tup])
        text.append(new_choice)
        
        next_tup = (next_tup[1], new_choice)
        text.append(next_tup)


    print join(text)


#     return text


open_file = open_and_read_file("green-eggs.txt")
dict_suess = make_chains(open_file)
make_text(dict_suess)


# input_path = "green-eggs.txt"

# # Open the file and turn it into one long string
# input_text = open_and_read_file(input_path)

# # Get a Markov chain
# chains = make_chains(input_text)

# # Produce random text
# random_text = make_text(chains)

# print random_text
