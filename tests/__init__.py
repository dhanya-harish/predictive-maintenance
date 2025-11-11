# Tests package

%%writefile tests/test_basic.py
def test_imports():
    """Test that basic imports work"""
    try:
        import numpy
        import pandas
        import streamlit
        assert True
    except ImportError:
        assert False, "Import failed"

def test_basic_math():
    """Basic test to ensure testing works"""
    assert 1 + 1 == 2
