
import os
import subprocess
from pathlib import Path


# Check if at least one media file is found in the supplied media dir.
def confirm_media_files(raw_videos_dir: str):
    video_exts = [".mp4", ".mov", ".mkv"]
    for file in Path(raw_videos_dir).iterdir():
        if file.suffix in video_exts:
            return True
        else:
            return False


# iterates through the first level of a dir and adds filepaths that end in the correct file extensions to a list.
def gather_video_files(raw_videos_dir: str):
    gathered_files = []
    for file in Path(raw_videos_dir).iterdir():
        confirm_media_file(str(file))
        gathered_files.append(file)

    return gathered_files  # Returns a list of Pathlib objects.


def create_one_directory(location: str, filename):
    dir_name = Path(filename).stem.replace(" ", "_")
    playlist_dir = Path(location, 'VideoPlaylists', dir_name)
    playlist_dir.mkdir(parents=True, exist_ok=True)

    return playlist_dir  # returns a Pathlib object.


def playlist_cmd(location, selected_file):
    output_dir = create_one_directory(location, selected_file)
    playlist_path = f"{output_dir}/playlist.m3u8"
    ts_file_pattern = f"{output_dir}/segment_%03d.ts"
    cmd = [
        "ffmpeg",
        "-i", str(selected_file),
        "-map", "0:v:0",
        "-map", "0:a:0",
        "-c:v", "libx264",
        "-crf", "12",
        "-c:a", "aac",
        "-ar", "44100",
        "-preset", "fast",
        "-hls_list_size", "0",
        "-threads", "0",
        "-f", "hls",
        "-hls_time", "8",
        "-hls_flags", "independent_segments",
        "-hls_segment_filename", ts_file_pattern,
        "-y",
        playlist_path
    ]
    return cmd

