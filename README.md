# Assignment_Gmail source 


<img width="1830" alt="截圖 2024-10-16 中午12 48 38" src="https://github.com/user-attachments/assets/05ccdbc0-b7da-4d70-a62b-60c7a4e8b0d6">

## Gmail Login-Send-View Test Flow with Pytest Selenium Framework

This project is a Gmail login, email sending, and viewing email test flow based on Python 3.12, integrated with the pytest selenium framework.

## Requirements

The following packages are required:

- pytest
- selenium
- undetected_chromedriver
- webdriver-manager
- setuptools

## Setup Instructions

### 1. (Optional) Switch to Python Virtual Environment

To ensure an isolated environment, you may switch to a Python virtual environment.

### 2. Install Requirements

Run the following command to install all required packages:

```bash
python3 -m pip install -r requirements.txt
```

### 3. (Optional) Modify Test Account in config.py

Update the following fields in config.py with your test Gmail account details:

```bash
USER = {YOUR EMAIL ACCOUNT}
PASSWORD = {YOUR PASSWORD}
SEND_TO = {RECIPIENT EMAIL ADDRESS}
```

### Running Tests
To execute the Gmail login, send, and view email tests, navigate to the path /Assignment_Gmail and run the following pytest command:

```bash
python3 -m pytest ./test/test_gmail.py
```

Or you can exeute the test via Test Exploere in VS Code

<img width="398" alt="截圖 2024-10-16 中午12 45 56" src="https://github.com/user-attachments/assets/9ccaedbc-83d3-4e82-847c-cd3a2ccbcc54">

