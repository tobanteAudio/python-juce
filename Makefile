.PHONY: install deps develop test lint coverage docs stats
default: develop

PACKAGE_NAME = juce
TEST_DIRECTORY = tests
EXAMPLES_DIRECTORY = examples
DOC_DIRECTORY = docs

install:
	@pip install .

deps:
	@pip install -r requirements-dev.txt

develop:
	@pip install -e .

test:
	@pytest $(TEST_DIRECTORY)

lint:
	@flake8 $(PACKAGE_NAME) $(TEST_DIRECTORY) $(EXAMPLES_DIRECTORY)
	@pylint $(PACKAGE_NAME) $(TEST_DIRECTORY)

coverage:
	@pytest --cov=$(PACKAGE_NAME) $(TEST_DIRECTORY) 

docs:
	# @cp README.md $(DOC_DIRECTORY)/README.md
	@cd $(DOC_DIRECTORY) && make html
	
stats:
	@echo "CODE:"
	@cloc $(PACKAGE_NAME)
	@echo "TESTS:"
	@cloc $(TEST_DIRECTORY)