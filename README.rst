Generate requirements.txt:
pip3 freeze > requirements.txt

build and upload to pypi test:
python setup.py bdist_wheel
twine upload --repository-url https://test.pypi.org/legacy/ dist/*

install on other projects:
pip install -i https://test.pypi.org/simple bchennu

Testing:
python -m bchennu args - to run from module invokes __main__.py file
python bchennu-runner.py args - direct cli

Unit-tests:
pytest -v bchennu/tests/test_bchennu.py

account:
TestPyPI repo- https://test.pypi.org/manage/project/bchennu/

github project : https://github.com/bharanic4040/bchennu/tree/master/bchennu
