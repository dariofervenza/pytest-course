# lets write some unit test for a class

# UNIT TESTS: small tests that directly cover functions and methods --> they cover "units of work"


# tests folder can not contain __init__.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from stuff.accum import Accumulator


def test_accumulator_init():
    accum = Accumulator()
    assert accum.count == 0

def test_accumulator_add_one():
    # test that the method add indeed adds 1 to the count
    accum = Accumulator()
    accum.add()
    assert accum.count == 1

def test_accumulator_add_three():
    accum = Accumulator()
    accum.add(3)
    assert accum.count == 3

def test_accumulator_add_twice():
    # test that the method add can be applied many times
    accum = Accumulator()
    accum.add()
    accum.add()
    assert accum.count == 2

def test_accumulator_cannot_set_count_directly():
    accum = Accumulator()
    with pytest.raises(AttributeError, match=r"property 'count' of 'Accumulator' object has no setter") as e:
        accum.count = 10

# WHY ALL THESE TESTS? they follow the pattern ARRANGE-ACT-ASSERT

# pattern is like: every test instanciate an object (arrange), make calls to the object methods (act) and verify the result is the one expected (assert)

# ARRANGE: instanciate objects, define variables etc

# ACT: do the thing that needs to be tested

# ASSERT: check that the expected value is obtained

# GOLD RULE: after the assert, there is no more code --> INDEPENDENT & ATOMIC tests