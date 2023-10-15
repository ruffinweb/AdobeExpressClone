
from mediaApp.mm_app import db
from flask import render_template, url_for
from flask import Blueprint, render_template
from mediaApp.mm_app.faqs.models import faQuestion
from mediaApp.mm_app.faqs.utils import insert_faqs


faqs_bp = Blueprint('faqs', __name__, template_folder='templates')


@faqs_bp.route('/faqs')
def faqs():
    title = "FAQs"
    questions = db.session.query(faQuestion).order_by(faQuestion.question_id).distinct()
    webdev_faqs = faQuestion.query.filter_by(source_file='webdev').all()
    bio_faqs = faQuestion.query.filter_by(source_file='portfolio').all()

    return render_template('faqs.html', title=title, 
                           all_questions=questions, webdev_faqs=webdev_faqs, bio_faqs=bio_faqs)
