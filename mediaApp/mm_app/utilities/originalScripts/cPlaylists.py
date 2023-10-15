import os
import subprocess
from pathlib import Path

test_videos_url = r"C:\Workspace\Sandbox\testMedia"

video_exts = [".mp4", ".mov", ".mkv"]
new_playlists_dir = Path(os.getcwd(), "Playlists")
new_playlists_dir.mkdir(exist_ok=True)


def create_playlist_directory(filename):
    dir_name = filename.stem
    playlist_dir = Path(os.getcwd(), 'Playlists', dir_name)
    playlist_dir.mkdir(exist_ok=True)
    return playlist_dir


def raw_video_files():
    test_videos_dir = Path(os.getcwd(), 'test_videos')
    test_videos_dir.mkdir(exist_ok=True)
    gathered_files = []
    for file in test_videos_dir.iterdir():
        if file.suffix in video_exts:
            gathered_files.append(file)
    return gathered_files


def playlist_cmd(selected_file):
    output_dir = create_playlist_directory(selected_file)
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


# Generate playlist for all files in the main directory.
# if __name__ == '__main__':
#     for video in raw_video_files():
#         try:
#             subprocess.run(playlist_cmd(video))
#         except TypeError as te:
#             print(f"Issue with type or what-ev.")
#         except OverflowError as oe:
#             print(f"Issue with type or what-ev.")
#         except ModuleNotFoundError as te:
#             print(f"Issue with type or what-ev.")


# Final test for generating playlists before using pytest.


for video_file in Path(test_videos_url).iterdir():
    print(video_file)
