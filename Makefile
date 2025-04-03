chunk ?= 4
repeat ?= 3

help:
	@echo 'Makefile for test task                                                                '
	@echo '                                                                                      '
	@echo 'Usage:                                                                                '
	@echo ' make install_lin      install all dependencies on macOS/Linux                        '
	@echo ' make install_win      install all dependencies on Windows                            '
	@echo ' make example          run chunker example  (`chunk` and `repeat` args are available) '
	@echo ' make pytest           run pytest                                                     '
	@echo ' make lint             run Python linter                                              '
	@echo '                                                                                      '

install_lin:
	@python -m venv venv
	@source venv/bin/activate
	@pip install -r requirements.txt

install_win:
	@python -m venv venv
	@venv\Scripts\activate
	@pip install -r requirements.txt

.PHONY: pytest

pytest:
	@pytest

lint:
	@flake8 . --count --show-source --statistics

example:
	@python -m main -e -c $(chunk) -r $(repeat)