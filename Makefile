.PHONY: install deps develop test lint coverage clean docs stats
default: develop

PACKAGE_NAME = juce
TEST_DIRECTORY = tests
EXAMPLES_DIRECTORY = example
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
	@pylint --disable=fixme $(PACKAGE_NAME) $(TEST_DIRECTORY)

coverage:
	@pytest --cov=$(PACKAGE_NAME) $(TEST_DIRECTORY)

clean:
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
	@cloc  $(EXAMPLES_DIRECTORY)/getting_started/getting_started.py \
		$(EXAMPLES_DIRECTORY)/build_variations/build_variations.py \
		$(EXAMPLES_DIRECTORY)/multi_project_consistency/multi_project_consistency.py \
		$(EXAMPLES_DIRECTORY)/projucer_automation/projucer_automation.py