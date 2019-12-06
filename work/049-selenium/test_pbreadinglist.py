import os
import re
from time import sleep

import pytest

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

USERNAME = os.environ['PBREADLIST_USER']
PASSWORD = os.environ['PBREADLIST_PW']

HOME = 'https://pbreadinglist.herokuapp.com'
FIRST_BOOK = f'{HOME}/books/nHDtDAAAQBAJ'
SECOND_BOOK = f'{HOME}/books/NWqePwAACAAJ'
MY_BOOKS = 'My Books'

# https://pybit.es/pytest-fixtures.html


@pytest.fixture
def driver_home():
    driver = webdriver.Firefox()
    driver.get(HOME)
    # pytest's way of tearDown
    yield driver
    driver.quit()


@pytest.fixture
def driver_first_book():
    driver = webdriver.Firefox()
    driver.get(FIRST_BOOK)
    yield driver
    driver.quit()


@pytest.fixture
def driver_login():
    driver = webdriver.Firefox()

    driver.get(HOME)
    driver.find_element_by_link_text('Login').click()
    driver.find_element_by_name('username').send_keys(USERNAME)
    driver.find_element_by_name('password').send_keys(PASSWORD + Keys.RETURN)

    yield driver
    driver.quit()


def test_homepage_title(driver_home):
    expected_title = "PyBites My Reading List | Because We Love Books"
    assert driver_home.title == expected_title


def test_number_of_thumbs_homepage(driver_home):
    expected_image_count = 100
    images = driver_home.find_elements_by_tag_name("img")
    assert len(images) == expected_image_count


def test_has_login_link(driver_home):
    try:
        driver_home.find_element_by_link_text("Login")
    except NoSuchElementException:
        pytest.fail("There should be a login button on the site.")


def test_book_page_title(driver_first_book):
    expected_title = (
        "PyBites My Reading List | The Hitchhiker's Guide to Python"
    )
    assert driver_first_book.title == expected_title


def test_book_page_meta_data(driver_first_book):
    expected_authors = "Kenneth Reitz, Tanya Schlusser"
    expected_publisher = "O'Reilly Media, Inc."
    expected_date = "2016-08-30"

    page_source = driver_first_book.page_source
    assert expected_authors in page_source
    assert expected_publisher in page_source
    assert expected_date in page_source


def test_book_page_has_add_book_link(driver_first_book):
    try:
        driver_first_book.find_element_by_link_text("Add Book")
    except NoSuchElementException:
        pytest.fail("There should be an 'Add Book' link on the site.")


def test_search_box_auto_direct(driver_first_book):
    search_term = "Fluent Python"
    search_box = driver_first_book.find_element_by_name("searchTitles")
    search_box.send_keys(search_term)
    sleep(2)

    results = driver_first_book.find_elements_by_css_selector(
        "div.ac_results > ul > li",
    )
    first_result = results[0]
    first_result.click()

    expected_directed_page_title = "PyBites My Reading List | Fluent Python"
    assert driver_first_book.title == expected_directed_page_title


def test_login_to_site(driver_login):
    expected_link_texts = [
        "5-Hour Challenge",
        "My Books",
        "Logouts",
    ]
    try:
        for link_text in expected_link_texts:
            driver_login.find_elements_by_link_text(link_text)
    except NoSuchElementException:
        pytest.fail(
            "Not found all expected links for logged in users: {0}".format(
                expected_link_texts,
            ),
        )

    unwanted_link = "login"
    try:
        driver_login.find_element_by_link_text(unwanted_link)
        pytest.fail("Found unwanted link for logged in user: {0}".format(
            unwanted_link,
        ))
    except NoSuchElementException:
        # This is what we want.
        pass


def _get_number_books_read(driver):
    sleep(2)  # The site renders to slow to proceed immediately.
    driver.find_element_by_link_text(MY_BOOKS).click()

    mybooks_stats = driver.find_element_by_class_name("mui--text-subhead")
    pattern = r"Total reading: (\d+) books added.*"
    replacement = r"\g<1>"  # First group defined in parenthesis ()
    replaced_result = re.sub(pattern, replacement, mybooks_stats.text)
    return int(replaced_result)


def test_add_delete_book(driver_login):
    books_read_initial = _get_number_books_read(driver_login)

    # Visit second book and add it
    driver_login.get(SECOND_BOOK)
    driver_login.find_element_by_name("bookSubmit").click()

    # Check that count is increased
    books_read_after_add = _get_number_books_read(driver_login)
    assert books_read_after_add == books_read_initial + 1

    # Visit second book again and remove it
    driver_login.get(SECOND_BOOK)
    driver_login.find_element_by_name("deleteBook").click()

    # Check that counter is back to the initial value
    books_read_after_delete = _get_number_books_read(driver_login)
    assert books_read_after_delete == books_read_initial


def test_logout(driver_login):
    pass
