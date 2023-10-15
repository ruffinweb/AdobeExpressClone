import pytest

from mediaApp.wsgi import app

# Home Page Tests

"""Test 1
Confirming the home page uses the correct title tag.
"""


def test_home_title(client):
    response = client.get("/")
    assert b"<title>Multimedia App</title>" in response.data


"""Test 2.


"""

"""Test 3.
FAQS 

"""

"""Test 4.


"""

"""Test 5.


"""

"""Test 6.


"""

# Contact Page Tests

""" Test 1
Confirming the home page uses the correct title tag.
"""


def test_contact_title(client):
    response = client.get("/contact")
    assert b"<title> Contact Page </title>" in response.data


"""Test 2.


"""

"""Test 3.
FAQS 

"""

"""Test 4.


"""

"""Test 5.


"""

# FAqs Page Tests

"""Test 1
Confirming the home page uses the correct title tag.
"""


def test_faqs_title(client):
    response = client.get("/faqs")
    assert b"<title> FAQs </title>" in response.data


"""Test 2.


"""

"""Test 3.
FAQS 

"""

"""Test 4.


"""

"""Test 5.


"""

# Memberships Page Tests

"""Test 1
Confirming the home page uses the correct title tag.
"""


# def test_memberships_title(client):
#     response = client.get("/faqs")
#     assert b"<title> FAQs </title>" in response.data


"""Test 2.


"""

"""Test 3.
FAQS 

"""

"""Test 4.


"""

"""Test 5.


"""

# Registration Page Tests

"""Test 1
Confirming the home page uses the correct title tag.
"""


# def test_registration_title(client):
#     response = client.get("/faqs")
#     assert b"<title> FAQs </title>" in response.data


"""Test 2.


"""

"""Test 3.
FAQS 

"""

"""Test 4.


"""

"""Test 5.


"""

# Login Page Tests

"""Test 1
Confirming the home page uses the correct title tag.
"""


# def test_login_title(client):
#     response = client.get("/faqs")
#     assert b"<title> FAQs </title>" in response.data


"""Test 2.


"""

"""Test 3.
FAQS 

"""

"""Test 4.


"""

"""Test 5.


"""

# Explore Page Tests

"""Test 1
Confirming the home page uses the correct title tag.
"""


# def test_explore_title(client):
#     response = client.get("/faqs")
#     assert b"<title> FAQs </title>" in response.data


"""Test 2.


"""

"""Test 3.
FAQS 

"""

"""Test 4.


"""

"""Test 5.


"""

# Search Page Tests

"""Test 1
Confirming the home page uses the correct title tag.
"""


# def test_search_title(client):
#     response = client.get("/faqs")
#     assert b"<title> FAQs </title>" in response.data


"""Test 2.


"""

"""Test 3.
FAQS 

"""

"""Test 4.


"""

"""Test 5.


"""

# Categories Page Tests

"""Test 1
Confirming the home page uses the correct title tag.
"""


# def test_categories_title(client):
#     response = client.get("/faqs")
#     assert b"<title> FAQs </title>" in response.data


"""Test 2.


"""

"""Test 3.
FAQS 

"""

"""Test 4.


"""

"""Test 5.


"""
