import os
import subprocess
from pathlib import Path


"""Every video needs these files in order for the ffmpeg commands to create a complete video dir:
A video file (mp4, mov, mkv, etc), a metadata file? closed captions file, a licence, 

"""


# iterates through the first level of a dir and adds filepaths that end in the correct file extensions to a list.
def raw_video_files(raw_videos_dir):
    video_exts = [".mp4", ".mov", ".mkv"]
    gathered_files = []
    for file in Path(raw_videos_dir).iterdir():
        if file.suffix in video_exts:
            gathered_files.append(file)

    return gathered_files  # Returns a list of Pathlib objects.


# Creates and returns the path to a directory.
def create_playlist(location, filename):
    dir_name = filename.stem.replace(" ", "_")
    playlist_dir = Path(location, 'VideoPlaylists', dir_name)
    playlist_dir.mkdir(parents=True, exist_ok=True)

    return playlist_dir  # returns a Pathlib object.


def create_video_dirs(videos_location: str):
    for one_video in Path(videos_location).iterdir():
        try:
            create_playlist(videos_location, one_video)

        except TypeError as te:
            print(f"Issue with type or what-ev.")
        except OverflowError as oe:
            print(f"Issue with type or what-ev.")
        except ModuleNotFoundError as te:
            print(f"Issue with type or what-ev.")


# create_video_dirs2(r"C:\Workspace\Sandbox\testMedia")
