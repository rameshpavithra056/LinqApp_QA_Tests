# Linq App QA Automation

## Overview
This project contains Selenium-based automated tests for the `/welcome` page of LinqApp.

## Setup & Installation

1. Install dependencies:
    ```bash
    pip install selenium
    ```

2. Download and install [ChromeDriver](https://sites.google.com/chromium.org/driver/) for your Chrome version.

3. Run tests:
    ```bash
    python selenium_test.py
    ```

## CI Integration
A GitHub Actions workflow (`.github/workflows/test.yml`) runs the tests on each push.

## Test Cases
- Verify that the phone number input field works.
- Check the visibility of social login buttons (Email, Apple, Google, LinkedIn).

## Author
QA Engineer Candidate
