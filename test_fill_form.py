import os
from selene import browser, be



def test_fill(browser_configuration):
    # browser.config.browser_name = "firefox"

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
    # browser.element('#uploadPicture"]').send_keys(os.getcwd() + '/pict.jpg')
    browser.element('#uploadPicture').send_keys(os.getcwd() + '\example.png')
    # ---------
    # browser.config.driver.capabilities.keys(keys.Control, "+")
    browser.element('#currentAddress').type("Sport Street, 140").press_enter()
    browser.element('#state').should(be.clickable).click()
    browser.element('#react-select-3-input').set_value("NCR").press_enter()
    browser.element('#city').should(be.clickable).click()
    browser.element('#react-select-4-input').set_value("Delhi").press_enter()
    browser.element('[id="submit"]').should(be.clickable).click()



