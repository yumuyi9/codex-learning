from bank import value


def test_hello_prefix():
    assert value("hello") == 0
    assert value("HELLO, Alice") == 0


def test_other_h_prefix():
    assert value("hi") == 20
    assert value("How are you?") == 20


def test_other_greetings():
    # 单词出现在中间时，不符合前缀规则。
    assert value("Well, hello") == 100
    assert value("Good morning") == 100
    assert value("") == 100
