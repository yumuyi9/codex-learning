from plates import is_valid


def test_length_boundaries():
    assert is_valid("AB") is True
    assert is_valid("ABCDEF") is True
    assert is_valid("A") is False
    assert is_valid("ABCDEFG") is False


def test_starts_with_two_letters():
    assert is_valid("A123") is False
    assert is_valid("12AB") is False


def test_digits_at_end():
    assert is_valid("CS50") is True
    assert is_valid("CS50P") is False
    assert is_valid("AB1C2") is False


def test_first_digit():
    # 用一对只改数字排列的样例区分首位零和末尾零。
    assert is_valid("AB01") is False
    assert is_valid("AB10") is True


def test_only_letters_and_digits():
    assert is_valid("PI3.14") is False
    assert is_valid("AB C") is False
    assert is_valid("AB!C") is False
