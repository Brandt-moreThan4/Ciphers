
# Frequency distribution of english letters as they appear in the wild.
english_letter_Freq = {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I':
6.97, 'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C':
2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97, 'P':
1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10, 'Z':
0.07}

# String version of letter freq
ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def get_letter_count(message):
    """Returns a dictionary with each english letter and its count in the message"""
    letter_counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0,
                   'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0,
                   'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}

    for letter in message:
        if letter in LETTERS:
            letter_counts[letter] += 1

    return letter_counts


def get_item_at_index_zero(x):
    return x[0]


def get_frequency_order(message):
    """Returns a string of ther alphabet letters arranged in order of most frequently occurring in message"""

    letter_counts = get_letter_count(message)

    freq_to_letter = {}
    for letter in LETTERS:
        if letter_counts[letter] not in freq_to_letter:
            freq_to_letter[letter_counts[letter]] = [letter]
        else:
            freq_to_letter[letter_counts[letter]].append(letter)

    for freq in freq_to_letter:
        freq_to_letter[freq].sort(key=ETAOIN.find, reverse=True)
        freq_to_letter[freq] = ''.join(freq_to_letter[freq])

    freq_pairs = list(freq_to_letter.items())
    freq_pairs.sort(key=get_item_at_index_zero, reverse=True)

    freq_order = []
    for freq_pair in freq_pairs:
        freq_order.append(freq_pair[1])

    return ''.join(freq_order)


def english_freq_match_score(message):
    """Return score from 0-12 with 12 being a string that has a fequency most similar to english as a whole"""

    freq_order = get_frequency_order(message)

    match_score = 0

    for common_letter in ETAOIN[:6]:
        if common_letter in freq_order[:6]:
            match_score += 1

    for uncommon_letter in ETAOIN[-6:]:
        if uncommon_letter in freq_order[-6:]:
            match_score += 1

    return match_score