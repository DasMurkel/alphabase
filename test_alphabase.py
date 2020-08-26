# Copyright (c) 2020 DasMurkel

import pytest
from alphabase import alphabase

HEX_ALPHABET = "0123456789abcdef"
WINDOWS_1252_ALPHABET = "0123456789!\"#$%&'()*+,-./:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"


@pytest.mark.parametrize("test_input,expected", [(1, "1"), (10, "a"), (15, "f"), (255, "ff")])
def test_alphabase_encoder_hex(test_input, expected):
    ab = alphabase(HEX_ALPHABET)
    assert ab.to_alphabet(test_input) == expected


@pytest.mark.parametrize("test_input,expected", [(0, "0"), (1, "1"), (12345, "1F@"), (830584, "1000")])
def test_alphabase_encoder_ascii(test_input, expected):
    ab = alphabase(WINDOWS_1252_ALPHABET)
    assert ab.to_alphabet(test_input) == expected


@pytest.mark.parametrize("test_input,expected", [("0", 0), ("1", 1), ("~~~", 830583)])
def test_alphabase_decoder_ascii(test_input, expected):
    ab = alphabase(WINDOWS_1252_ALPHABET)
    assert ab.to_int(test_input) == expected


@pytest.mark.parametrize("test_input", [0, 1, 12345])
def test_reversal(test_input):
    ab = alphabase(WINDOWS_1252_ALPHABET)
    string = ab.to_alphabet(test_input)
    assert test_input == ab.to_int(string)


@pytest.mark.parametrize("test_input,expected", [(0, 0), (1, 93), (3, 830583)])
def test_max_value(test_input, expected):
    ab = alphabase(WINDOWS_1252_ALPHABET)
    assert ab.max_value(test_input) == expected
