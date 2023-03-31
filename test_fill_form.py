from selene import browser, have, be


def test_fill():
    browser.config.hold_browser_open = True
    browser.open("https://demoqa.com/automation-practice-form")
    browser.element('#firstName').type('Maria').press_enter()
    browser.element('#lastName').type('Ivanova').press_enter()
    browser.element('#userEmail').type('examplemail@mail.com').press_enter()
    # browser.element('[id="gender-radio-2"]').should(be.clickable).click()
    browser.element('[for="gender-radio-2"]').click()
    browser.element('#userNumber').type('8987654321')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').type('January')
    browser.element('.react-datepicker__year-select').type('1996')
    browser.element(f'.react-datepicker__day--0{"01"}').click()
    browser.element('#subjectsInput').set_value("English").press_enter()
    browser.element('[for ="hobbies-checkbox-1"]').click()