
from mediaApp.mm_app import db


class faQuestion(db.Model):
    question_id = db.Column(db.Integer, primary_key=True)
    source_file = db.Column(db.String(80), nullable=False)
    question = db.Column(db.String(80), nullable=False)
    answer = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f"faqQuestion('{self.question}', '{self.answer}')"
