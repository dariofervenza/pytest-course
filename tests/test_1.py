# pytest is a core test framework: allows you to write test cases as functions
# it also executes the tests and reports results
# unit test go in the same project they test

# however, end-to-end tests may have its own repository if the application they cover is splitted in many repositories

# in python unittest, tests are classes, in pytest they are functions


# FIRST TEST: both the module and the function names have to start with "test_"
# by default, any module and function that starts with test_ will be auto detected by pytest: it will execute them
# there can be non test functions in a test module, no problemo


def test_one_plus_one():
    assert 1 + 1 == 2


# RUN WITH: pytest command in the root of the repo


# FAILED TEST:

def test_one_plus_two():
    a = 1
    b = 2
    c = 0
    assert a + b == c

# ASSERTION INTROSPECTION: when this fails it appears: assert a + b == c but also assert 1 + 2 == 0 (it shows the values in the error message + the type of error (AssertionError or other))
# therefore, you have to check if the test failed due to an Exception or due to an assertion