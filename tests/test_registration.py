from models.registration_page import RegistrationPage
from data.users import student


def test_registration_with_valid_data():
    registration_page = RegistrationPage(student)
    registration_page.open()

    registration_page.register(student)

    registration_page.should_have_registered_user_with(student)