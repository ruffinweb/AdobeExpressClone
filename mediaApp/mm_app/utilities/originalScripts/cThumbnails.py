
import json
import subprocess
import os
from pathlib import Path

"""This is for all the tools Ill use to generate the website content. The functionality can be used later for server side
video editing in the application.

Tools/Functionality Needed

- Video Dirs. Each video needs to be run through each of these functions. create_preview, create_thumbnail,
create_streaming_playlist, etc. This will take a long time so Ill use my raspberry pi (if its powerful enough) to run
batch commands over the next few days. 

create_streaming_playlist- Create a m3u8 plyalist folder to allow efficent video streaming in smaller chunks.
create_preview - Create a short preview video for the album page. 
create_thumbnail- Create a grid of video frames for the video page.

"""

# test_dir = os.getcwd()
# video_dirs = Path(test_dir).iterdir()
#
# print("Done")

# Constants
OUTPUT_FOLDER = "output"  # Folder where previews and other files will be stored

# Create the output folder if it doesn't exist
if not os.path.exists(OUTPUT_FOLDER):
    os.mkdir(OUTPUT_FOLDER)


def calculate_frames(video_path, num_of_frames=7):
    ffprobe_cmd = f'ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "{video_path}"'
    duration = float(subprocess.check_output(ffprobe_cmd, shell=True).decode('utf-8').strip())
    frame_interval = duration / num_of_frames
    return frame_interval


def create_preview(video_path, frame_interval):
    frames = []
    for i in range(7):
        seek_time = i * frame_interval
        frame_file = f"{OUTPUT_FOLDER}/{video_path.stem}_frame_{i}.png"
        frames.append(frame_file)
        cmd = f'ffmpeg -ss {seek_time} -i "{video_path}" -vf "select=eq(n\\,0)" -vframes 1 {frame_file}'
        subprocess.run(cmd, shell=True)

    frame_list_file = f"{OUTPUT_FOLDER}/frames.txt"
    with open(frame_list_file, "w") as f:
        for frame in frames:
            f.write(f"file '{frame}'\n")
            f.write(f"duration 1\n")

    preview_cmd = f'ffmpeg -f concat -safe 0 -i {frame_list_file} -y -pix_fmt yuv420p "{OUTPUT_FOLDER}/{video_path.stem}_preview.mp4"'
    subprocess.run(preview_cmd, shell=True)


def main():
    all_video_dirs = Path(".")
    video_extensions = ['*.mp4', '*.avi', '*.mov', '*.mkv', '*.wmv', '*.flv', '*.mpg', '*.mpeg', '*.3gp', '*.webm',
                        '*.ogg', '*.ogv', '*.ts', '*.m4v']

    a = [f for f in all_video_dirs]

    all_video_files = []
    all_video_files = [f for ext in video_extensions for f in video_folder.glob(ext)]

    for video_dir in all_video_dirs:


    for video_file in all_video_files:
        print(f"Processing {video_file} ...")

        frame_interval = calculate_frames(video_file)
        print(f"Calculated frame interval: {frame_interval}")

        create_preview(video_file, frame_interval)
        print(f"Preview created for {video_file}")

        print(f"{video_file} processed successfully.\n")


if __name__ == "__main__":
    main()
