import pytest
from all_tests import route_title, meta_tag, link_success, link_accuracy
# from all_tests import route_title, route_title_elems, meta_tag, link_success, link_accuracy

from mediaApp.wsgi import app


"""Home Route Tests 
Tests for confirming the functionality found on the home page.
"""


def test_home_title(client, home_route="/"):
    route_title(client, home_route, "Multimedia App")
    # route_title_elems(client, home_route, "Multimedia App")


def test_home_meta_tag(client, home_route="/"):
    meta_tag(client, home_route)


# def test_home_title(client, home_route="/"):
#     route_title(client, home_route, "Multimedia App")


"""Explore Route Tests
Tests for confirming the functionality found on the explore page.
"""


def test_explore_title(client, explore_route="/explore"):
    route_title(client, explore_route, "Explore Videos")


def test_explore_meta_tag(client, explore_route="/explore"):
    meta_tag(client, explore_route)


"""Gallery Route Tests
Tests for confirming the functionality found on the video gallery page.
"""


def test_gallery_page_title(client):
    route_title(client, "/gallery/video_gallery", "Multimedia Gallery")


"""Categories Route Tests
Tests for confirming the functionality found on the video categories page.
"""


def test_categories_page_title(client):
    route_title(client, "/categories", "Categories")


def test_grid_layout(client):
    pass


# def test_title_emphasis(client):
#     pass


# def test_preview_play(client):
#     pass
#
#
# def test_preview_stop(client):
#     pass
#
#
# def test_preview_rewind(client):
#     pass
#
#
# def test_category_link_interaction(client):
#     pass
#
#
# def test_category_link_status(client):
#     pass
#
#
# def test_category_link_accuracy(client):
#     pass
#
#
# def test_sort_options_quantity(client):
#     pass
#
#
# def test_sort_button_toggle(client):
#     pass
#
#
# def test_sort_button_options(client):
#     pass
