[![Install](https://github.com/nogibjj/kb545-python-integration-project/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/kb545-python-integration-project/actions/workflows/install.yml)
[![Lint](https://github.com/nogibjj/kb545-python-integration-project/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/kb545-python-integration-project/actions/workflows/lint.yml)
[![Test](https://github.com/nogibjj/kb545-python-integration-project/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/kb545-python-integration-project/actions/workflows/test.yml)
[![Format](https://github.com/nogibjj/kb545-python-integration-project/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/kb545-python-integration-project/actions/workflows/format.yml)
## Continous Integration using GitHub Actions of Python Data Science Project

This is a POC of a full Python Data Science project, that has a fully functioning continuous integration architecture setup, utilizing GitHub Actions. This is for Individual Project 1 for IDS 706 Data Engineering

Tasks Completed Include:

* Adding the proper pandas version to the requirements.txt file, specifically pandas version 2.1.0. Also added matplotlib, Ruff, and nbval plugin
* Added a library folder that holds a lib.py file, which holds a function that accepts a filePath, and returns the descriptive stats of said dataset
* Added a src folder that holds a panda_stat.py file, which passes in the iris.csv (found at https://gist.github.com/netj/8836201). As well, holds a panda_jupyter.ipynb file, which is a jupyter notebook that does the same
* Added two test files. The first, called test_lib.py, which runs an assert on the function in the library to gauge if it is properly working. The second test file, called test_script.py, tests the panda_stat.py file to gauge if it properly works. To test the jupyter notebook, the makefile uses nbval extension from pytest
* Edited MakeFile to properly install everything, test the code using both pytest and nbval, lints using ruff, and formats files in both the src folder and library folder
* Changed this very README to hold Github Actions badges

A video explanation of everything is here

[YouTube Link](https://www.youtube.com/watch?v=dQEtzD4ntZg)