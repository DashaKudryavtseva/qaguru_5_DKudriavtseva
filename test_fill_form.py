from selene import browser, have, be


def test_fill():
    browser.config.hold_browser_open = True
    browser.open("https://demoqa.com/automation-practice-form")
    browser.element('#firstName').type('Maria').press_enter()
    browser.element('#lastName').type('Ivanova').press_enter()
    browser.element('#userEmail').type('examplemail@mail.com').press_enter()
