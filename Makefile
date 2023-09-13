install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test: install
	python -m pytest -vv --cov=src --cov=library test_*.py
	pytest --nbval src/*.ipynb

format:
	black src/*.py 
	black library/*.py

lint:
	#Whenever a lint check needs to occur, either have a mylib folder, or change mylib to the respective folder name
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py src/*.py library/*.py

refactor: format lint

deploy:
	#deploy goes here
		
all: install lint test format deploy
