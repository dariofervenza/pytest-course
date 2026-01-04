# by itself, pytest only discovers tests by looking in the files and executes them
# you can extend that with plugins: a package that adds new capabilities to the framework


# PLUGIN: pytest-html  -> save to report file in html format
# pip install pytest-html
# python -m pytest --html=report.html



# PLUGIN: pytest-cov --> compute code coverage
# pytest-cov is a pytest integration for coverage.py
# pip install pytest-cov
# python -m pytest --cov

# only coverage for one folder
# python -m pytest --cov=stuff

# only coverage for two folders (tests shgould not be included in coverage)
# python -m pytest --cov=stuff --cov=tests


# coverage report in html
# python -m pytest --cov=stuff --cov-report html


# coverage taking into considerantion conditionals (branches) --> he RECOMMENDS using this by default
# python -m pytest --cov=stuff --cov-branch


# PLUGIN: pytest-xdist -> run test in parallel (accelerates execution)
# pip install pytest-xdist
# add -n num_of_threads
# python -m pytest -n 5

# it also allows distributing test execution across many machines using ssh


# PLUGIN: pytest-bdd --> behavior-driven-development  --> in GIVEN-WHEN-THEN format
# you need to take a bdd course ON YOUR OWN (the same test automation university has a course)


# NOTE: many frameworks like django have their own plugins


# WRITE YOUR OWN PLUGIN: you can do it but its complex