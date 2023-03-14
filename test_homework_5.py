import os
from selene import browser, have
from selenium.webdriver import Keys


def test_browser_submit(settingsofbrowser):
    browser.open_url('https://demoqa.com/automation-practice-form')
    browser.element('#firstName').type('Sergey')
    browser.element('#lastName').type('Pulatov')
    browser.element('#userEmail').type('biglol9898@gmaol.com')
    browser.element('[for = "gender-radio-1"]').click()
    browser.element('#userNumber').type('9567456232')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select [value="4"]').click()
    browser.element('.react-datepicker__year-select [value="1997"]').click()
    browser.element('.react-datepicker__day--002').click()
    browser.element('#subjectsInput').type('Economics').press_enter()
    browser.element('[for = "hobbies-checkbox-1"]').click()
    browser.element('[for = "hobbies-checkbox-3"]').click()
    browser.element('#uploadPicture').send_keys(os.getcwd() + "/image.png")
    browser.element('#currentAddress').type('Saint-Petersburg, Lensoveta street, 53')
    browser.execute_script("window.scrollBy(0, 500)")
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').type('Gurgaon').press_enter()
    browser.element('#submit').submit()
    # Let's check it
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.element('//table/tbody/tr[1]/td[2]').should(have.text('Sergey Pulatov'))
    browser.element('//table/tbody/tr[2]/td[2]').should(have.text('biglol9898@gmaol.com'))
    browser.element('//table/tbody/tr[3]/td[2]').should(have.text('Male'))
    browser.element('//table/tbody/tr[4]/td[2]').should(have.text('9567456232'))
    browser.element('//table/tbody/tr[5]/td[2]').should(have.text('02 May,1997'))
    browser.element('//table/tbody/tr[6]/td[2]').should(have.text('Economics'))
    browser.element('//table/tbody/tr[7]/td[2]').should(have.text('Sports, Music'))
    browser.element('//table/tbody/tr[8]/td[2]').should(have.text('image.png'))
    browser.element('//table/tbody/tr[9]/td[2]').should(have.text('Saint-Petersburg, Lensoveta street, 53'))
    browser.element('//table/tbody/tr[10]/td[2]').should(have.text('NCR Gurgaon'))
