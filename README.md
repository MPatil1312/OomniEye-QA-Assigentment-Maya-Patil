# OomniEye – Playwright Automation Testing

## 1. Objective
The objective of this automation test is to verify that the public login page opens and that its essential UI elements are visible.

## 2. Tools and Technologies
- Python
- Playwright
- Chromium browser
- Visual Studio Code

## 3. Test File
`Test/test_public_access.py`

## 4. Test Scenario
Verify that the OomniEye login page loads and displays the email field, password field, and SIGN IN button.

## 5. Test Steps
1. Launch the Chromium browser.
2. Open the OomniEye staging application.
3. Check the page title.
4. Verify that the email field is visible and enabled.
5. Verify that the password field is visible and enabled.
6. Verify that the SIGN IN button is visible.
7. Check that the URL contains `/login`.
8. Check that the HTTP response status is 200.

## 6. Assertions
Assertions are used to verify expected conditions. If an assertion fails, Python raises an error and stops the script unless the error is handled.

## 7. Execution Result
The script executed successfully. The recorded output showed that the email field, password field, and SIGN IN button were visible and enabled. The page URL contained `/login`, the HTTP status was 200, and the script exited with code 0.

## 8. Limitations
Valid login credentials were not available. Therefore, successful login and authenticated application modules were not tested. This test covers only the public login page.

## 9. How to Run
Install Playwright if needed:

`pip install playwright`

Install the browser if needed:

`playwright install chromium`

Run the test from the assignment's root folder:

`python "automation/Test/test_public_access.py"`