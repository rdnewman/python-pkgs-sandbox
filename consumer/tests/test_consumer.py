import pytest
import basicmath
from basicmath import operations

def test_consumer():
    assert operations.add_stuff(1, 1) == 2
