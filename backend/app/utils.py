import numpy as np


def get_word_freq(word_list, text):
    word_freq = []
    total_words = len(text.split())
    text = text.lower()
    for word in word_list:
        word_freq.append((text.count(word) / total_words) * 100)
    return word_freq


def get_character_freq(character_list, text):
    character_freq = []
    total_characters = len(text)
    text = text.lower()
    for character in character_list:
        character_freq.append((text.count(character) / total_characters) * 100)

    return character_freq


def get_capital_sequences(text):
    capital_sequences = []
    for word in text.split():
        if word.isupper():
            capital_sequences.append(word)
    return capital_sequences


def get_word_lengths(word_list):
    word_lengths = []
    for word in word_list:
        word_lengths.append(len(word))
    return word_lengths


def get_email_features(text, word_list, character_list):
    attributes = []
    attributes.extend(get_word_freq(word_list, text))
    attributes.extend(get_character_freq(character_list, text))
    capital_sequences = get_capital_sequences(text)
    capital_sequences_lengths = get_word_lengths(capital_sequences)
    if not capital_sequences_lengths:
        attributes.extend([0, 0, 0])
    else:
        attributes.append(np.mean(capital_sequences_lengths))
        attributes.append(np.max(capital_sequences_lengths))
        attributes.append(np.sum(capital_sequences_lengths))

    return np.array(attributes)


def get_words_characters(names):
    words = [name[10:] for name in names if name.startswith('word_freq')]
    characters = [name[10:] for name in names if name.startswith('char_freq')]

    return words, characters
