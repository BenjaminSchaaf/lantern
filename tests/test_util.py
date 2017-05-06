"""Test utility functions"""

import pytest

import string

from lantern.util import (
    remove, split_columns, combine_columns
)


def test_remove_with_punctuation():
    """Test punctuation removed"""
    plaintext = "Don't worry my friends."
    assert remove(
        plaintext, string.punctuation
    ) == "Dont worry my friends"


def test_remove_with_whitespace():
    """Test whitespace removed"""
    plaintext = "Don't worry my friends."
    assert remove(
        plaintext, string.whitespace
    ) == "Don'tworrymyfriends."


def test_columns_same_length():
    """testing split and combine where n = len(text)"""
    text = "example"
    split = split_columns(text, len(text))
    assert split == list(text)
    assert combine_columns(split) == text


def test_columns_lower_length():
    """Testing split and combine columns where num columns is less than the lenght of text"""
    text = "example"

    split = split_columns(text, 1)
    assert split == ['example']
    assert combine_columns(split) == 'example'

    split = split_columns(text, 2)
    assert split == ['eape', 'xml']
    assert combine_columns(split) ==  'example'

    split = split_columns(text, 3)
    assert split == ['eme', 'xp', 'al']
    assert combine_columns(split) ==  'example'

    split = split_columns(text, 4)
    assert split == ['ep', 'xl', 'ae', 'm']
    assert combine_columns(split) ==  'example'

    split = split_columns(text, 5)
    assert split == ['el', 'xe', 'a', 'm', 'p']
    assert combine_columns(split) ==  'example'

    split = split_columns(text, 6)
    assert split == ['ee', 'x', 'a', 'm', 'p', 'l']
    assert combine_columns(split) ==  'example'


def test_split_columns_invalid_values():
    """Testing split columns with invalid lengths to check for ValueErrors"""
    text = "example"
    with pytest.raises(ValueError) as e_info:
        split_columns(text, -1)

    with pytest.raises(ValueError) as e_info:
        split_columns(text, -200)

    with pytest.raises(ValueError) as e_info:
        split_columns(text, 0)

    with pytest.raises(ValueError) as e_info:
        split_columns(text, 200)
