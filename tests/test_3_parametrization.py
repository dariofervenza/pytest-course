# some tests may have different and outputs + some specific boundary cases should be tested

# solution: parameterize the test --> cover all the different combinations of inputs and outputs


# MULTIPLICATION IDEAS:

# two positive integers
# multiply by 1
# multiply by 0
# multiply a positive by a negative
# multiply negative by negative
# multiply floats

# each idea must be tested --> a good test suite should cover all possibilities but it should not have repeated cases

# eg: to test multiply by one we could use 1 times 99, if we include that but also 1 and 100 we have introduced an unneccesary test (avoid, it adds time and cost)


# we could test these 6 cases with 6 functions
# however, we can do it with one using PYTEST.MARK.PARAMETRIZE --> it will run the test with many inputs

# in british english is parameterize but in american is parametrize  (use american)

import pytest

inputs = [
    (2, 3, 6),
    (1, 99, 99),
    (0, 99, 0),
    (3, -4, -12),
    (-5, -5, 25),
    (2.5, 6.7, 16.75),
]

# each tuple in inputs has to have the same number of elements (3 in this case) as we indicate in the string "a, b, product"
@pytest.mark.parametrize("a, b, product", inputs)
def test_multiplication(a, b, product):
    assert a * b == product

# remember that you can use any type of python object as parameters

# you could also store data in external storage such as csv and read them in the test

# NEXT STEP: Hypothesis library (research it) --> allows you to randomly choose inputs and integrates with pytest

# example: add to this test a list of integers or floats --> will autogenerate it rnadomly
# therefore, allows you avoid hardcoding input values