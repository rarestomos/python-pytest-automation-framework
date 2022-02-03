# python-pytest-automation-quickstart
Python + pytest automation framework quickstart

# Description
This aims to be a quick-start for Python and pytest automation framework. It should have everything in place to just start writing your own tests with Python.

# How to use it
* if you just need the structure of a framework, to start writing your own tests or to learn test automation with Python and pytest, just create a branch from master and start using the framework
* if you want to see an example of how tests can be written and how the framework works, change to the feature/python-testing-demo-library-app branch

# About the framework
* it is currently setup for Rest Api testing, database testing and UI testing
* it is configured to run on a couple of different environments controlled through the config.ini files but adding a new one is very simple:
    * add a new config file and name it as you want while setting up all the values from an existing one specific for this new env
    * add a new env config file in the /configuration folder keeping the naming convention \<env\>_configuration.py
    * based on the env environment variable the correct configuration will be used

# Libs used
* for api testing the builtin _requests_ lib is used
* to map the models it is recommended to use the _namedtuple_ data structure
* for the UI testing the _Elementium_ lib has been integrated 
* for working with the database the _sqlalchemy_ lib has been added

# Specific virtual environment
* cli _python -m venv venv_ inside your project folder ("python -m venv name_of_venv_folder")

# Reporting
* to execute a specific test suite based on marker name, following command should be used at tests runtime:
* E.g. For "backend" tests: _pytest -m backend --template=html1/index.html --report=reports/backend_tests_report.html_

# Environment variables required

# Command line options to configure execution