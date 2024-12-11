#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for counting the words in a string.
This is part of the debugging exercise series focusing on buggy implementations.

Module contents:
    - count_words: Counts the number of words in a string

Created on 2024-12-06
Author: Claude AI
"""


def count_words(text: str) -> int:
    """Counts the number of words in a string.
    Words are separated by spaces.

    Parameters:
        text: str, the input string

    Returns -> int: number of words in the text

    >>> count_words("hello world")
    2
    >>> count_words("one")
    1
    >>> count_words("")
    0
    """
    assert isinstance(text, str), "input must be a string"
    # assign a list with the words in text splitted by space
    words_in_text = text.split(" ")
    # create a list to add the words in it filtering unwanted whitespaces
    filtered_words = []

    for word in words_in_text:
        # if the word in the list is not a whitespace and not empty, append it to the list
        if word.isspace() is False and word != "":
            filtered_words.append(word)

    # return the length of the filtered words list
    return len(filtered_words)
