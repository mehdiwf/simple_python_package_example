python_ex = python

i:
	$(python_ex) -m pip install -e .
u:
	$(python_ex) -m pip uninstall example_package_mifz
t:
	$(python_ex) ./tests/test_script.py
# ua:
# 	python -m pip uninstall  example_package_mifz
# 	python3 -m pip uninstall example_package_mifz
