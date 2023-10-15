
import pytest
from all_tests import (confirm_media_exists, gather_videos, create_directory, playlist_creation,
                       info_file_creation, preview_creation, thumbnail_creation)


# FFMpeg Server Side Video Processing Tests


def test_confirm_media_exists(sample_videos_dir_fix):
    confirm_media_exists(sample_videos_dir_fix)


def test_gather_videos(temp_dir_fix):
    gather_videos(temp_dir_fix)


def test_create_directory(sample_videos_dir_fix):
    create_directory(sample_videos_dir_fix)


# def test_playlist_creation(temp_dir_fix, sample_video_fix):
#     playlist_creation(temp_dir_fix, sample_video_fix)


# def test_info_file_creation():
#     info_file_creation()
#
#
# def test_preview_creation():
#     preview_creation()
#
#
# def test_thumbnail_creation():
#     thumbnail_creation()

