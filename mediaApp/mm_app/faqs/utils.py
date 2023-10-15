import json
from flask import current_app
from mediaApp.mm_app import db
from mediaApp.mm_app.faqs.models import faQuestion
from pathlib import Path


# return the data from one json file.
def parse_json(json_file):
    # json_file_path = Path(current_app.root_path, json_file)
    json_file_path = json_file
    with open(json_file_path) as f:
        data = json.load(f)
    return data


def insert_faqs():
    base_path = current_app.root_path
    faqs_url = Path(base_path, "static/json/faqs.json")
    faqs_file = parse_json(faqs_url)
    for index, faq in enumerate(faqs_file):
        # print(faq)
        faq_record = faQuestion(source_file=str(faq), question=faq['question'], answer=faq['answer'])

        exists = faQuestion.query.filter_by(question=faq['question'], answer=faq['answer']).first()

        if not exists:
            db.session.add(faq_record)
