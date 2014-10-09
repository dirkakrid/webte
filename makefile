python ?= python3.4
package = webte

all: $(package).egg-info

$(package).egg-info: bin/pip setup.py $(package)/
	rm -rf $(package).egg-info && bin/pip install --editable .

bin/pip: bin/python get-pip.py
	bin/python get-pip.py

bin/python:
	$(python) -m venv --without-pip .

get-pip.py:
	$(python) -c "import urllib.request; urllib.request.urlretrieve(\
  'https://bootstrap.pypa.io/get-pip.py', 'get-pip.py')"

test: coverage flake8 check

coverage: bin/coverage all
	bin/coverage run --branch --source=$(package)/ -m unittest discover -vfs $(package)
	bin/coverage html -d htmlcov; bin/coverage report --fail-under=100 -m

flake8: bin/flake8 all
	bin/flake8 setup.py $(package)/

check: all
	bin/python setup.py check

bin/coverage: bin/pip
	bin/pip install coverage

bin/flake8: bin/pip
	bin/pip install flake8

clean:
	rm -rf *.egg-info $(shell find $(package) -name "__pycache__" -type d)
	rm -rf *.egg build bin lib include share pyvenv.cfg get-pip.py
	rm -rf htmlcov .coverage
