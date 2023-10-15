import pytest
from pathlib import Path
import shutil
import os
import pytest
from mediaApp.wsgi import app
from mediaApp.mm_app.utilities.scripts import gather_video_files, create_one_directory, playlist_cmd

"""All Tests
This file is where every one of the tests that I wrote myself are stored.
I import the test I need into each a testing file. Testing files are separated based on what is being tested.
Im keeping all my tests in one place for now to see what functionality is repeated.

Example. Tests in ffmpeg.py are all related to the video processing commands 
used to prepare a multimedia web app or a web app for content creation.
Tests in general.py are meant to be used for every web app and 
includes tests that are similar to what is tested on Google Lighthouse.

"""


# General Tests Every Web App Can Use

# Title element value
def route_title(client, route, expected_title):
    response = client.get(route)
    assert f"<title>{expected_title}</title>".encode('utf-8') in response.data


# def route_title_elems(client, route, expected_title):
#     for route in app.url_map():
#         response = client.get(route)
#         assert f"<title>{expected_title}</title>".encode('utf-8') in response.data


def meta_tag(client, route):
    response = client.get(route)
    assert f'<meta name="viewport" content="width=device-width, initial-scale=1">'.encode('utf-8') in response.data


def link_success(client, route):
    response = client.get(route)
    assert f'<meta name="viewport" content="width=device-width, initial-scale=1">'.encode('utf-8') in response.data


def link_accuracy():
    pass


# FFMpeg Server Side Video Processing Tests


# Confirm the application has access to at least one media file.
def confirm_media_exists(temp_dir_fix):
    temp_dir = temp_dir_fix

    result = gather_video_files(str(temp_dir))
    expected = [temp_dir / 'video1.mp4', temp_dir / 'video2.mov']
    assert result == expected

    shutil.rmtree(temp_dir)


# Create a list of filepaths to videos.
def gather_videos(temp_dir_fix):
    temp_dir = temp_dir_fix

    result = gather_video_files(str(temp_dir))
    expected = [temp_dir / 'video1.mp4', temp_dir / 'video2.mov']
    assert result == expected

    shutil.rmtree(temp_dir)


#  Confirm directory creation command works.
def create_directory(temp_dir_fix):
    temp_dir = temp_dir_fix
    result = create_one_directory(str(temp_dir), str(temp_dir.stem))
    expected = Path(temp_dir, 'VideoPlaylists/testVideoDir')
    assert result == expected

    shutil.rmtree(temp_dir)


#  Confirm playlist creation command works.
def playlist_creation(temp_dir_fix, sample_video_fix):
    playlist_cmd(temp_dir_fix, sample_video_fix)

    result = playlist_cmd(temp_dir_fix, sample_video_fix)

    expected = Path(temp_dir_fix, 'VideoPlaylists/testVideoDir')
    assert result == expected


#  Confirm the video info file is created.
def info_file_creation():
    pass


#  Confirm the preview command works.
def preview_creation():
    pass


#  Confirm the thumbnail command works.
def thumbnail_creation():
    pass


# Multimedia App Tests


#  Confirm the required video files are present.
def video_playlist_files(client):
    pass
