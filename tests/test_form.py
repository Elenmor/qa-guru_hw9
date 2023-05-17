import os
from selene.support.shared import browser
from selene import have, command



def test_practice_form(browser_open):
    browser.open('/automation-practice-form')

    # WHEN

    browser.element('#firstName').type('Helen')
    browser.element('#lastName').type('Morilova')
    browser.element('#userEmail').type('test@test.ru')

    #Choose gender
    browser.element('.custom-control [for=gender-radio-2]').click()

    browser.element('#userNumber').type('5555555555')

    #Choose birthday
    browser.element("#dateOfBirthInput").click()
    browser.element('.react-datepicker__year-select').send_keys('1984')
    browser.element('.react-datepicker__month-select').send_keys('May')
    browser.element('.react-datepicker__day--012').click()

    #Choose subject and hobby
    browser.element('#subjectsInput').type('Art').press_enter()
    browser.element('.custom-control [for=hobbies-checkbox-1]').click()

    #Upload piture
    #browser.element('#uploadPicture').send_keys(os.getcwd() + "/pic.png")
    browser.element('#uploadPicture').send_keys(os.getcwd() + "/resources/pic.png")

    #Choose adress
    browser.element('#currentAddress').type('adress street, 1')
    browser.element('#state').click()
    browser.element('#react-select-3-input').set_value('NCR').press_tab()
    browser.element('#city').click()
    browser.element('#react-select-4-input').set_value('Delhi').press_tab()

    browser.element('#submit').perform(command.js.click)

    #THAN
    browser.element('table').all('td').even.should(
        have.exact_texts(
            'Helen Morilova',
            'test@test.ru',
            'Female',
            '5555555555',
            '12 May,1984',
            'Arts',
            'Sports',
            'pic.png',
            'adress street, 1',
            'NCR Delhi'

        )
    )



    print('\nТест пройден успешно.')
