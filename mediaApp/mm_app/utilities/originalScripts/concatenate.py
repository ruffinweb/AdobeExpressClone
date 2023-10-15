
import os
import subprocess
from pathlib import Path
from tempfile import NamedTemporaryFile


"""Still having issues with the final videos. Some frames are skipping, some videos are way too long."""


def test_videos_dir():
    test_videos = Path(os.getcwd(), 'test_videos')
    test_videos.mkdir(exist_ok=True)
    return test_videos  # returns the path to all the video directories to be turned into one video.


def new_videos_dir():
    new_videos = Path(os.getcwd(), "new_videos")
    new_videos.mkdir(exist_ok=True)
    return new_videos  # returns the path where the new videos will be created.


def raw_video_files():
    gathered_video_files = []
    for vid_dir in test_videos_dir().iterdir():
        for file in vid_dir.iterdir():
            if file.suffix in [".mp4", ".mov", ".mkv"]:
                gathered_video_files.append(file)
    return gathered_video_files  # returns one list of video files to combine into one video.


def concat_cmd(selected_files, new_location, filename):  # Selected files is a dir of files.
    with NamedTemporaryFile(mode='w+', delete=False, suffix='.txt') as f:
        for filepath in selected_files.iterdir():
            f.write(f"file '{filepath.as_posix()}'\n")
        clips_list = Path(f.name)

    cmd = ["ffmpeg", "-f", "concat", "-safe", "0", "-i", clips_list.as_posix(), "-c", "copy",
           Path(new_location, filename)]
    return cmd  # returns the command that will combine one specific set of videos into one video.


if __name__ == '__main__':
    for video_dir in test_videos_dir().iterdir():
        one_video_cmd = concat_cmd(video_dir, new_videos_dir(), f"{video_dir.stem}_combine.mov")
        subprocess.run(one_video_cmd)
