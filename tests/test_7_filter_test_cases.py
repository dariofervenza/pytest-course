# we may have thousands or millions of tests --> we are interested in running small subsets or it will take hours


# run only one module
# python -m pytest tests/test_1.py


# run many modules  
# python -m pytest tests/test_1.py tests/test2.py


# run only one test
# python -m pytest tests/test_1.py::test_one_plus_one


# run tests that have one word on its name
# this runs test like def test_with_one()
# python -m pytest -k one


# it also supports AND / OR logic
# python -m pytest -k "one and not accum"



# FILTER WITH MARKERS
# markers are tags that we manually add --> then we could say: run all test with "gay marker"
# first add the gay marker to pytest.ini

import pytest

@pytest.mark.gay
def test_im_a_test():
    assert 1 == 1


# here there can be many markers and also parametrization decorators
@pytest.mark.gay
@pytest.mark.gay2
def test_im_a_test2():
    assert 1 == 1


# run with:
# python -m pytest -m gay
# python -m pytest -m "gay and not gay2"

# DEFAULT MARKERS: skip (test wont run), skipif (wont run if..), xfail (allowed to fail), parametrize (we have already seen it)
