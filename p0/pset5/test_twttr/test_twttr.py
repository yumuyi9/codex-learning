from twttr import shorten


def test_removes_lowercase_vowels():
    assert shorten("education") == "dctn"


def test_removes_uppercase_vowels():
    assert shorten("AEIOU") == ""
    assert shorten("TwIttEr") == "Twttr"


def test_keeps_other_characters():
    # 保留辅音大小写、数字、空格和标点。
    assert shorten("CS50, Wow!") == "CS50, Ww!"
    assert shorten("Rhythm") == "Rhythm"
    assert shorten("") == ""
