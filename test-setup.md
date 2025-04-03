# Test Setup - Selenium

## Why Selenium?
Selenium is chosen because:
- It is widely used for web automation testing.
- It supports multiple browsers.
- It integrates well with CI/CD pipelines.

## Setup Instructions

1. **Install Python and Selenium**
   ```bash
   pip install selenium
   ```

2. **Download ChromeDriver**
   - Ensure it matches your installed Chrome version.
   - Place it in a directory included in your system PATH.

3. **Run the Tests**
   ```bash
   python selenium_test.py
   ```

## Configuration Files
- `selenium_test.py`: Contains the test scripts.
- `.github/workflows/test.yml`: Runs tests automatically on push to GitHub.
