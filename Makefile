.PHONY: install deps develop test lint coverage docs stats
default: develop

PACKAGE_NAME = juce
TEST_DIRECTORY = tests
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
	@pylint $(PACKAGE_NAME)

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