Overview
This project is an automation testing framework designed to validate the functionality of a web application. 
The framework utilizes Python's unittest library and integrates other utilities to facilitate browser interactions, report generation, and automated email notifications.

Structure
run.py: Main execution script that orchestrates the test runs and reporting.
test_Asign.py, test_login.py: Test scripts for specific functionalities like assignment handling and user login.
Login_page.py, Setting_page.py, Signup_page.py: Page objects representing various pages of the application, encapsulating the respective page elements and interactions.
base_page.py, base_util.py: Base classes providing common functionalities to all page objects and utility functions.
DriverUtil.py: Utility class for managing WebDriver sessions and interactions.
email_util.py: Utility for sending email notifications post-test executions.
Installation
To set up the testing environment, ensure that Python and pip are installed on your system. Install the required Python packages by running:
pip install -r requirements.txt

Usage
To execute the tests and generate a report, run:
python run.py

This script initializes the test suite, runs the tests, and generates an HTML report that includes the details of the test cases executed and their outcomes.

Scheduler Setup
A scheduler is configured within run.py to execute tests periodically. Adjust the scheduler settings in the script to meet the frequency needs of your testing environment.

Reporting
Test reports are saved in HTML format under the ./report directory, named with the timestamp of the test execution.

Warning!!!:
You need to type the email address and security code in the common/email_util.py 
and account, password in the testcase/test_Asign.py and test_login.py!!!