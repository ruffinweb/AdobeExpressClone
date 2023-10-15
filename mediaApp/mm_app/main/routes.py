
from mediaApp.mm_app import db
from flask import Blueprint, render_template
from mediaApp.mm_app.faqs.utils import insert_faqs
from mediaApp.mm_app.faqs.models import faQuestion
from mediaApp.mm_app.explore.utils import insert_categories
from mediaApp.mm_app.explore.models import Video, Category
from sqlalchemy.exc import OperationalError

main_bp = Blueprint('main', __name__)


def is_model_initialized(model):
    try:
        return model.query.first() is not None
    except OperationalError:
        return False


def initialize_db_and_insert_models(models, insertion_functions):
    db.create_all()

    for model, insertion_function in zip(models, insertion_functions):
        if not is_model_initialized(model):
            insertion_function()

    db.session.commit()


# main route. layout.html is used for the general skeleton of all pages.
@main_bp.route('/')
@main_bp.route("/home")
def home():
    title = "Multimedia App"

    # List of models to check and initialize
    models_to_initialize = [faQuestion, Video, Category]  # Add more models to this list as needed

    # Corresponding list of functions to call for data insertion
    insertion_functions_to_call = [insert_faqs, insert_categories]  # Add more functions as needed

    # Initialize DB and insert data
    initialize_db_and_insert_models(models_to_initialize, insertion_functions_to_call)

    return render_template('home.html', title=title, is_home_page=True)


@main_bp.route("/info/<selected_info>")
def info(selected_info):
    title = "Portfolio Info"

    selected_info = selected_info

    return render_template('info.html', title=title, selected_info=selected_info)


@main_bp.route('/services')
def services():
    services_url = "mm_app/static/json/services.json"

    return render_template('services.html', title='Product Info')
