import pytest

from app.misc import RequestValue, BaseDispatcher, Custom1Dispatcher, Custom2Dispatcher


@pytest.mark.parametrize(
    "a,b,c,d,e,f,expected_variant", [
        (True, True, False, 1, 1, 1, "M"),  # any dangerous math operation
        (True, True, True, 1, 1, 1, "P"),  # if there will be a need to parametrize for future
        (False, True, True, 1, 1, 1, "T"),
    ])
def test_base_case(a, b, c, d, e, f, expected_variant):
    value = RequestValue(a, b, c, d, e, f)
    variant, result = BaseDispatcher(value).dispatch()
    assert variant == expected_variant


@pytest.mark.parametrize(
    "a,b,c,d,e,f,expected_variant", [
        (True, True, False, 1, 1, 1, "M"),
        (True, True, True, 1, 1, 1, "P"),
        (False, True, True, 1, 1, 1, "T"),
    ])
def test_custom1_case(a, b, c, d, e, f, expected_variant):
    value = RequestValue(a, b, c, d, e, f)
    variant, result = Custom1Dispatcher(value).dispatch()
    assert variant == expected_variant


@pytest.mark.parametrize(
    "a,b,c,d,e,f,expected_variant", [
        (True, True, False, 1, 1, 1, "T"),
        (True, True, True, 1, 1, 1, "P"),
        (False, True, True, 1, 1, 1, "T"),
        (True, False, True, 1, 1, 1, "M"),
    ])
def test_custom2_case(a, b, c, d, e, f, expected_variant):
    value = RequestValue(a, b, c, d, e, f)
    variant, result = Custom2Dispatcher(value).dispatch()
    assert variant == expected_variant
