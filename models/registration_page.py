import time
from selene import browser, have, command
from data.users import Users
from tests import resource

class RegistrationPage:
    def __init__(self, user: Users):
        self.first_name = browser.element("#firstName")
        self.last_name = browser.element("#lastName")
        self.email = browser.element("#userEmail")
        self.gender = browser.element(f'[value="{user.gender.name}"] + label')
        self.phone = browser.element("#userNumber")
        self.subject = browser.element("#subjectsInput")
        self.hobby = browser.all("[for^=hobbies]").element_by(
            have.exact_text(f"{user.hobby.name}")
        )
        self.address = browser.element("#currentAddress")
        self.state = browser.element('#state')
        self.city = browser.element('#city')
        self.submit = browser.element("#submit")

    def open(self):
        browser.open("/automation-practice-form")
        browser.all("[id^=google_ads][id$=container__]").with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(2)
        )
        browser.all("[id^=google_ads][id$=container__]").perform(command.js.remove)

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)'
        ).click()
        return self

    def select_picture(self, file_name):
        browser.element('#uploadPicture').send_keys(resource.path(file_name))
        time.sleep(1)
        return self

    def choose_state(self, name):
        self.state.perform(command.js.scroll_into_view)
        self.state.click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(name)
        ).click()
        return self

    def choose_city(self, name):
        self.city.click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(name)
        ).click()
        return self

    def register(self, user: Users):
        self.first_name.type(user.first_name)
        self.last_name.type(user.last_name)
        self.email.type(user.email)
        self.gender.click()
        self.phone.type(user.phone)
        self.fill_date_of_birth(
            user.date_of_birth.strftime("%Y"),
            user.date_of_birth.strftime("%B"),
            user.date_of_birth.strftime("%d"),
        )
        self.subject.type(user.subject).press_enter()
        self.hobby.click()
        self.select_picture(user.picture)
        self.address.type(user.address)
        self.choose_state(user.state)
        self.choose_city(user.city)
        self.submit.press_enter()

    def should_have_registered_user_with(self, user: Users):
        browser.all(".table").all("td").should(
            have.exact_texts(
                ("Student Name", f"{user.first_name} {user.last_name}"),
                ("Student Email", user.email),
                ("Gender", user.gender.name),
                ("Mobile", user.phone),
                ("Date of Birth", user.date_of_birth.strftime("%d %B,%Y")),
                ("Subjects", user.subject),
                ("Hobbies", user.hobby.name),
                ("Picture", user.picture),
                ("Address", user.address),
                ("State and City", f"{user.state} {user.city}"),
            )
        )