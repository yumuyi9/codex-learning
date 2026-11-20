import pytest

from fuel import convert, gauge


def test_convert_valid_fractions():
    assert convert("0/4") == 0
    assert convert("1/4") == 25
    assert convert("2/3") == 67
    assert convert("4/4") == 100
    assert type(convert("1/2")) is int


def test_convert_invalid_fractions():
    # pytest.raises 会在没有抛出指定异常时让测试失败。
    for fraction in ("5/4", "1.5/4", "1/cat", "-1/4", "1/-4", "3"):
        with pytest.raises(ValueError):
            convert(fraction)


def test_convert_zero_denominator():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_gauge_boundaries():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(2) == "2%"
    assert gauge(50) == "50%"
    assert gauge(98) == "98%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
