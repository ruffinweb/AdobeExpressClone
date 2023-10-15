import json
from pathlib import Path
from flask import current_app
from mediaApp.mm_app import db
from mediaApp.mm_app.explore.models import Video, Category

file_formats = [".mp4", "mov", "mp3", "wav", "jpg", "png"]


# return the data from one json file.
def parse_json(json_file):
    # json_file_path = Path(current_app.root_path, json_file)
    json_file_path = json_file
    with open(json_file_path) as f:
        data = json.load(f)
    return data


def one_folder(one_dir: str):
    aa = Path(one_dir)
    # print(aa.parts[-1])
    # print(aa.parents[0])

    all_videos = {aa.parts[-1]: []}
    for video in aa.iterdir():
        # print(video)
        if video.suffix in file_formats:
            all_videos[aa.parts[-1]].append(video.stem)

    return all_videos


# def insert_videos():
#     base_path = current_app.root_path
#     all_video_dirs = [
#         # Path(base_path, "mm_app/static/json/faqs.json"),
#         # Path(base_path, "mm_app/static/json/categories.json"),
#         # Path(base_path, "static/json/faqs.json"),
#         # Path(base_path, "static/json/categories.json"),
#         r"C://Programming/Projects/MultiMediaProject/mediaApp/mm_app/static/json/categories.json"
#     ]
#     for video_dir in all_video_dirs:
#         all_faqs = parse_json(file)
#
#         for index, faq in enumerate(all_faqs):
#             # print(faq)
#             video_record = Video(source_file=str(file), question=faq['question'], answer=faq['answer'])
#
#             exists = faQuestion.query.filter_by(question=faq['question'], answer=faq['answer']).first()
#
#             if not exists:
#                 db.session.add(faq_record)


# Include a check to see if there are new videos added.
def gather_video_dirs():
    all_video_dirs = []  # A list of paths to each video dir.
    base_path = current_app.root_path
    video_folders_url = Path(base_path, "static/folders")

    for video_dir in video_folders_url.iterdir():
        all_video_dirs.append(video_dir)

    return all_video_dirs


def insert_videos():
    video_dirs = gather_video_dirs()
    video_files = [a for a in video_dirs]

    video_dir_record = Video(file_name="", preview_url="", thumbnail_url="",
                             description="", runtime="", resolution="")
    exists = Category.query.filter_by(file_name=video_files[0].stem).first()

    if not exists:
        db.session.add(video_dir_record)


def insert_categories():
    base_path = current_app.root_path
    category_file_url = Path(base_path, "static/json/categories.json")
    data = parse_json(category_file_url)

    for index, category in enumerate(data):
        # print(faq)
        category_record = Category(category_name=str(category['name']),
                                   category_preview_url=str(category['preview_url']))

        exists = Category.query.filter_by(category_name=str(category['name']),
                                          category_preview_url=str(category['preview_url'])).first()

        if not exists:
            db.session.add(category_record)



