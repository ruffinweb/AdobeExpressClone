
from mediaApp.mm_app import db
from flask import url_for, render_template, redirect, request, flash, Blueprint
# from mediaApp.mm_app.gallery.models import ContactFormModel
# from mediaApp.mm_app.gallery.forms import ContactForm
# from mediaApp.mm_app.gallery.utils import send_contact_email

import os


gallery_bp = Blueprint('gallery', __name__, template_folder='templates')


@gallery_bp.route('/gallery/<selected_tag>', methods=['GET', 'POST'])
def video_gallery(selected_tag):
    title = "Multimedia Gallery"

    return render_template('gallery.html', title=title, selected_tag=selected_tag)


# @gallery_bp.route('/gallery', methods=['GET', 'POST'])
# def video_gallery():
#     title = "Gallery"
#
#     return render_template('gallery.html', title=title)


# @gallery_bp.route('/gallery', methods=['GET', 'POST'])
# def photo_gallery():
#     title = "Multimedia Gallery"
#
#     return render_template('gallery.html', title=title)

