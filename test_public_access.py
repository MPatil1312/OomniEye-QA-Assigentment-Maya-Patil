
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    response = page.goto(
        "https://base-application-stage.oomnieye.com/",
        wait_until="domcontentloaded",
        timeout=30000
    )

    print("Page title:", page.title())

    # Check email field
    email_field = page.locator('input[type="email"]')
    print("Email field visible:", email_field.is_visible())
    print("Email field enabled:", email_field.is_enabled())
    assert email_field.is_visible(), "Email field is missing!"

    # Check password field
    password_field = page.locator('input[type="password"]')
    print("Password field visible:", password_field.is_visible())
    print("Password field enabled:", password_field.is_enabled())
    assert password_field.is_visible(), "Password field is missing!"

    # Check Sign In button
    login_button = page.get_by_role("button", name="SIGN IN")
    print("SIGN IN button visible:", login_button.is_visible())
    assert login_button.is_visible(), "SIGN IN button is missing!"

    # Check login page URL
    print("Page URL:", page.url)
    assert "/login" in page.url, "Login page did not open!"
    print("PASS: Login page opened")

    # Check HTTP response
    if response:
        print("HTTP status:", response.status)
        assert response.status == 200, "Page did not return HTTP 200!"

    browser.close()
