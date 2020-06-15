define USAGE
-> build system ⚙️

Commands:

	@echo "    make init       # Install Flask-app dependencies with virtualenv"
	@echo "    make serve      # Starts a Flask development server locally."
	@echo "    make test       # Tests entire application with pytest."

endef

export USAGE

help:
	@echo "$$USAGE"

init:
	virtualenv -p python3 venv
	source ./venv/bin/activate
	pip install -r requirements.txt

test:
	export environment=testing
	python tests.py

serve:
	source ./venv/bin/activate
	export FLASK_APP=manage.py
	flask run

all: init test serve
