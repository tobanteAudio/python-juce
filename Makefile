.PHONY: install deps develop test lint integration examples clean docs stats

default: develop

PACKAGE_NAME = juce
TEST_DIRECTORY = tests
DOC_DIRECTORY = docs

EXAMPLES_DIRECTORY = example
EXAMPLE_BUILD_VARIANT = $(EXAMPLES_DIRECTORY)/build_variations/build_variations.py
EXAMPLE_GETTING_STARTED = $(EXAMPLES_DIRECTORY)/getting_started/getting_started.py
EXAMPLE_PROJECT_CONSISTENCY = $(EXAMPLES_DIRECTORY)/multi_project_consistency/multi_project_consistency.py
EXAMPLE_PROJUCER_AUTOMATION = $(EXAMPLES_DIRECTORY)/projucer_automation/projucer_automation.py

install:
	@pip install .

deps:
	@pip install -r requirements-dev.txt

develop:
	@pip install -e .

test:
	@pytest -v --cov=$(PACKAGE_NAME) $(TEST_DIRECTORY) -m "not integration_test"

integration:
	@pytest -v --cov=$(PACKAGE_NAME) $(TEST_DIRECTORY)

examples:
	@python $(EXAMPLE_BUILD_VARIANT)
	@python $(EXAMPLE_GETTING_STARTED)
	@python $(EXAMPLE_PROJECT_CONSISTENCY)
	@python $(EXAMPLE_PROJUCER_AUTOMATION)

lint:
	@flake8 $(PACKAGE_NAME) $(TEST_DIRECTORY) $(EXAMPLES_DIRECTORY)
	@pylint --disable=fixme $(PACKAGE_NAME) $(TEST_DIRECTORY)


clean:
	rm -rf $(DOC_DIRECTORY)/_build
	rm -rf $(PACKAGE_NAME)/__pycache__
	rm -rf $(PACKAGE_NAME)/projucer/__pycache__
	rm -rf $(TEST_DIRECTORY)/output
	rm -rf $(TEST_DIRECTORY)/__pycache__
	rm -rf $(TEST_DIRECTORY)/projucer/__pycache__
	rm -rf .pytest_cache
	rm -rf .coverage

docs:
	@cd $(DOC_DIRECTORY) && make html

stats:
	@echo "CODE:"
	@cloc $(PACKAGE_NAME)
	@echo "TESTS:"
	@cloc $(TEST_DIRECTORY)
	@echo "EXAMPLES:"
	@cloc $(EXAMPLE_BUILD_VARIANT) $(EXAMPLE_GETTING_STARTED) $(EXAMPLE_PROJECT_CONSISTENCY) $(EXAMPLE_PROJUCER_AUTOMATION)