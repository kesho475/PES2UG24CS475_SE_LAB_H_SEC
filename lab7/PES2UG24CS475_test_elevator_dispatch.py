from hypothesis import given, strategies as st
from elevator_dispatch import parse_request, total_travel, load_percent

@given(st.text() | st.none())
def test_parse_request_no_crash(s):
    try:
        parse_request(s)
    except Exception as e:
        assert False, f"parse_request crashed with: {e}"

@given(st.text() | st.none())
def test_total_travel_no_crash(s):
    try:
        total_travel(s)
    except Exception as e:
        assert False, f"total_travel crashed with: {e}"

@given(st.text() | st.none())
def test_load_percent_no_crash(s):
    try:
        load_percent(s)
    except Exception as e:
        assert False, f"load_percent crashed with: {e}"
