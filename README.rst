
build and upload to pypi test:
python setup.py bdist_wheel
twine upload --repository-url https://test.pypi.org/legacy/ dist/*

install on other projects:
pip install -i https://test.pypi.org/simple bchennu

Testing:
python -m bchennu args - to run from module invokes __main__.py file
python bchennu-runner.py args - direct cli

account:
TestPyPI repo- https://test.pypi.org/manage/project/bchennu/