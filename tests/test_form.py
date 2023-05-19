import os
from selene.support.shared import browser
from selene import have, command
from models.registration_page import RegistrationPage


def test_practice_form(open_browser):
    registration_page = RegistrationPage()
    registration_page.open()

    registration_page.fill_first_name('Helen').fill_last_name('Morilova')

    registration_page.fill_email('test@test.ru')

    registration_page.fill_gender('Female')

    registration_page.fill_phone('5555555555')

    registration_page.fill_date_of_birth('1984', 'May', '12')

    registration_page.fill_subject('Arts')

    registration_page.fill_hobby('Sports')

    registration_page.upload_file('pic.png')

    registration_page.fill_adress('adress street, 1')

    registration_page.fill_state('NCR')

    registration_page.fill_city('Delhi')

    registration_page.click_submit()

    browser.element('#submit').perform(command.js.click)

    # THEN
    registration_page.should_registered_user_with(
        'Helen Morilova',
        'test@test.ru',
        'Female',
        '5555555555',
        '12 May,1984',
        'Arts',
        'Sports',
        'pic.png',
        'adress street, 1',
        'NCR Delhi',
    )


