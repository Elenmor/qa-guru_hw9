import time

from selene import have, command
from selene.support.shared import browser

from tests import resource


class RegistrationPage:

    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.email = browser.element('#userEmail')
        self.phone = browser.element('#userNumber')
        self.state = browser.element('#state')
        self.subject = browser.element('#subjectsInput')
        self.adress = browser.element('#currentAddress')
        self.city = browser.element('#city')

    def open(self):
        browser.open('/automation-practice-form')
        return self

    def fill_first_name(self, value):
        self.first_name.type(value)
        return self

    def fill_last_name(self, value):
        self.last_name.type(value)
        return self

    def fill_email(self, value):
        self.email.type(value)
        return self

    def fill_gender(self, gender):
        browser.element(f'[value={gender}] + label').click()
        return self

    def fill_phone(self, value):
        self.phone.type(value)
        return self

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)'
        ).click()
        return self

    def fill_subject(self, value):
        self.subject.type(value).press_enter()
        return self

    def fill_hobby(self, value):
        browser.all('.custom-checkbox').element_by(have.exact_text(value)).click()
        return self

    def upload_file(self, file_name):
        browser.element('#uploadPicture').send_keys(resource.path(file_name))
        time.sleep(1)
        return self

    def fill_adress(self, value):
        self.adress.type(value)
        return self

    def fill_city(self, name):
        self.city.click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(name)
        ).click()
        return self

    def fill_state(self, name):
        self.state.perform(command.js.scroll_into_view)
        self.state.click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(name)
        ).click()
        return self

    def click_submit(self):
        browser.element('#submit').perform(command.js.click)

    def should_registered_user_with(self, *args):

        browser.element('.table').all('td').even.should(
            have.exact_texts(args)
        )
        return self
