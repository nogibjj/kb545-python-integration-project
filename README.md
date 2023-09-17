[![Install](https://github.com/nogibjj/python-integration-project/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/python-integration-project/actions/workflows/install.yml)
[![Lint](https://github.com/nogibjj/python-integration-project/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/python-integration-project/actions/workflows/lint.yml)
[![Test](https://github.com/nogibjj/python-integration-project/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/python-integration-project/actions/workflows/test.yml)
[![Format](https://github.com/nogibjj/python-integration-project/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/python-integration-project/actions/workflows/format.yml)
## Continous Integration using GitHub Actions of Python Data Science Project

This is a POC of a full Python Data Science project, that has a fully functioning continuous integration architecture setup, utilizing GitHub Actions. This is for Individual Project 1 for IDS 706 Data Engineering

Tasks Completed Include:

* Adding the proper pandas version to the requirements.txt file, specifically pandas version 2.1.0. Also added matplotlib
* Added a src folder that held the created script function, which reads the iris.csv (found at https://gist.github.com/netj/8836201), and returns descriptive stats on sepal_length
* Added a function that creates a graph of the average sepal length of 3 different species of Iris, and saves it as a photo. The graph is shown below
* Added a test function called test_stat.py, which runs an assert on the function to gauge if it properly works. It compares the descriptive stats values with what they should be, and verifies that an image has been created
* Edited MakeFile to properly install everything, test the code, format everything proerply, and run a linter

![answer](https://github.com/nogibjj/kb545-pandas-stat-script/assets/55768636/ec4e21d0-e605-4b18-adb1-aac7b97a8f58)
