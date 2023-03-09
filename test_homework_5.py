import os
from selene import browser, have
from selenium.webdriver import Keys

def test_browser_submit(constants):
    browser.open_url('https://demoqa.com/automation-practice-form')
    browser.element('[id = "firstName"]').type('Sergey')
    browser.element('[id = "lastName"]').type('Pulatov')
    browser.element('[id = "userEmail"]').type('biglol9898@gmaol.com')
    browser.element('[for = "gender-radio-1"]').click()
    browser.element('[id = "userNumber"]').type('9567456232')
    browser.element('[id = "dateOfBirthInput"]').send_keys(Keys.COMMAND, "a").type('02 May 1997').press_enter()
    browser.element('[id = "subjectsInput"]').type('Economics').press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-3"]').click()
    browser.element('[id = "uploadPicture"]').send_keys(os.getcwd() + "/image.png")
    browser.element('[id = "currentAddress"]').type('Saint-Petersburg, Lensoveta street, 53')
    browser.execute_script("window.scrollBy(0, 500)")
    browser.element('[id = "react-select-3-input"]').type('NCR').press_enter()
    browser.element('[id = "react-select-4-input"]').type('Gurgaon').press_enter()
    browser.element('[id = "submit"]').submit()
    browser.element('[id = "example-modal-sizes-title-lg"]').should(have.text('Thanks for submitting the form'))






