.PHONY: deps develop test coverage stats
default: develop

PACKAGE_NAME = juce
TEST_DIRECTORY = tests

deps:
	@pip install -r requirements-dev.txt

develop:
	@pip install -e .

test:
	@pytest $(TEST_DIRECTORY)

coverage:
	@pytest --cov=$(PACKAGE_NAME) $(TEST_DIRECTORY) 

stats:
	@cloc $(PACKAGE_NAME) $(TEST_DIRECTORY)
	