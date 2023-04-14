import os
from selene import browser, have
from selene import command


def test_fill(browser_configuration):
    #открытие страницы
    browser.open("https://demoqa.com/automation-practice-form")

    browser.all('[id^=google_ads][id$=container__]').with_(timeout=3).wait_until(
        have.size_greater_than_or_equal(3)
    )
    browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)

    #заполнение полей
    browser.element('#firstName').type('Maria').press_enter()
    browser.element('#lastName').type('Ivanova').press_enter()
    browser.element('#userEmail').type('examplemail@mail.com').press_enter()
    browser.element('[for="gender-radio-2"]').click()
    browser.element('#userNumber').type('8987654321')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').type('January')
    browser.element('.react-datepicker__year-select').type('1996')
    browser.element(f'.react-datepicker__day--0{"01"}').click()
    browser.element('#subjectsInput').set_value("English").press_enter()
    browser.element('[for ="hobbies-checkbox-1"]').click()
    browser.element('#uploadPicture').send_keys(os.getcwd() + '\example.png')
    browser.element('#currentAddress').type("Sport Street, 140").press_enter()
    browser.element('#state').click()
    browser.element('#react-select-3-input').set_value("NCR").press_enter()
    browser.element('#city').click()
    browser.element('#react-select-4-input').set_value("Delhi").press_enter()
    browser.element('[id="submit"]').click()

    #сверка данных
    browser.element('[class=table-responsive]').should(have.text("Maria Ivanova"))
    browser.element('[class=table-responsive]').should(have.text("examplemail@mail.com"))
    browser.element('[class=table-responsive]').should(have.text("Female"))
    browser.element('[class=table-responsive]').should(have.text("8987654321"))
    browser.element('[class=table-responsive]').should(have.text("01 January,1996"))
    browser.element('[class=table-responsive]').should(have.text("English"))
    browser.element('[class=table-responsive]').should(have.text("Sports"))
    browser.element('[class=table-responsive]').should(have.text("example.png"))
    browser.element('[class=table-responsive]').should(have.text("Sport Street, 140"))
    browser.element('[class=table-responsive]').should(have.text("NCR Delhi"))


