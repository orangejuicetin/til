# done with Nolen on 11/8/23, 1:19PM

# secret word: TREES
# you guess: SPOKE
# YNNNY
# you guess: TRUST
# GGNYN
# you guess: SWIMS
# NNNNG

# secret word: AABCB
# you guess: AABBA
# reponse: GGGNN
#
# our next guess that we find:
# dictionary = { "AAAAA", "ABABB", .... }

#

# S, we get back G: eliminate 10, 50% of the time
# S, we get back N: "" -> EV is 10, worst is 10
# B:

# 10 of our words end in the letter S 100%
# 2 of our words end in C
# 5 words end in A
# 3 words end in B , compl = 17 -> worst = min(B_count, compl)


# AAB[^B][^A]
# given:
def submit_guess(guess) -> str:  # guess is a string of As and Bs, returns "GGNNG"
    pass


def satisfies_guess(guessed_word, response, candidate) -> bool:
    # if response has a G at position i, what should be true about guess[i] and cand[i]
    # if response has an N at position i...
    for i, char in enumerate(response):
        if char == "G":
            if guessed_word[i] != candidate[i]:
                return False
        if char == "N":
            if candidate[i] == guessed_word[i]:
                return False

    return True


# please implement:
# GNNNG
# N ->
def determine_secret_word(dictionary):  # returns a string of As and Bs
    while len(dictionary) > 1:
        guess = dictionary.pop()
        result = submit_guess(guess)
        if "N" in result:
            for word in dictionary:
                if not satisfies_guess(guess, result, word):
                    dictionary.remove(word)
        else:
            return guess

    return dictionary.pop()
