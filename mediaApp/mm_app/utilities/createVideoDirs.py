
import os
import subprocess
from pathlib import Path


"""
Every video needs these files in order for the ffmpeg commands to create a complete video dir:
A video file (mp4, mov, mkv, etc), a metadata file? closed captions file, a licence, 
"""


# iterates through the first level of a dir and adds filepaths that end in the correct file extensions to a list.
def gather_video_files(raw_videos_dir: str):
    video_exts = [".mp4", ".mov", ".mkv"]
    gathered_files = []
    for file in Path(raw_videos_dir).iterdir():
        if file.suffix in video_exts:
            gathered_files.append(file)

    return gathered_files  # Returns a list of Pathlib objects.


# Creates and returns the path to a directory.
def create_one_directory(location: str, filename):
    dir_name = Path(filename).stem.replace(" ", "_")
    playlist_dir = Path(location, 'VideoPlaylists', dir_name)
    playlist_dir.mkdir(parents=True, exist_ok=True)

    return playlist_dir  # returns a Pathlib object.


def create_video_dirs(videos_location: str):
    for one_video in Path(videos_location).iterdir():
        try:
            create_one_directory(videos_location, one_video)

        except TypeError as te:
            print(f"Issue with type or what-ev.")
        except OverflowError as oe:
            print(f"Issue with type or what-ev.")
        except ModuleNotFoundError as te:
            print(f"Issue with type or what-ev.")


# create_video_dirs(r"C:\Workspace\Sandbox\testMedia")


# Generate playlist for all files in the main directory.
if __name__ == '__main__':
    test_dir = r"C:\Workspace\Sandbox\testMedia"
    user_videos_dir = test_dir
    # user_videos_dir = os.getcwd()

    for video in gather_video_files(user_videos_dir):
        try:
            video_dir_location = create_one_directory(user_videos_dir, video)
            # video_playlist = create_playlist(video)
            # create_thumbnail = create_playlist_directory(video)
            # create_preview = create_playlist_directory(video)
            # create_info_file = create_playlist_directory(video)
            # create_video_preview = create_playlist_directory(video)
            # subprocess.run(videoDirCmd(video))
            # subprocess.run(videoDirCmd(video))
            # subprocess.run(videoDirCmd(video))
            # subprocess.run(videoDirCmd(video))

        except TypeError as te:
            print(f"Issue with type or what-ev.")
        except OverflowError as oe:
            print(f"Issue with type or what-ev.")
        except ModuleNotFoundError as te:
            print(f"Issue with type or what-ev.")
