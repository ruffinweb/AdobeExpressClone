
from mediaApp.mm_app import db
from flask import url_for, render_template, redirect, request, flash, Blueprint
from mediaApp.mm_app.explore.models import Video, Category
from mediaApp.mm_app.explore.utils import insert_categories

import os


explore_bp = Blueprint('explore', __name__, template_folder='templates')


@explore_bp.route('/explore')
def explore():
    title = "Explore Videos"

    return render_template('explore.html', title=title)


@explore_bp.route('/video/<string:single_video_id>', methods=['GET', 'POST'])
def single_video(single_video_id=""):
    title = "Suggestions"
    try:
        video = Video.query.filter_by(video_id=single_video_id).first()
        if video is None:
            raise ValueError("Video not found")
    except ValueError as e:
        return "", 404  # return empty string and 404 status code

    return render_template('explore.html', title=title, video=video)


@explore_bp.route('/categories')
def categories():
    title = "Categories"
    page_num = request.args.get('page', 1, type=int)

    category_list = db.session.query(Category).filter(Category.category_name).distinct()
    category_pages = category_list.paginate(per_page=12, page=page_num)

    return render_template('categories.html', title=title, category_pages=category_pages)


@explore_bp.route('/tags', methods=['GET', 'POST'])
def tags():
    title = "Tags"

    return render_template('tags.html', title=title)


@explore_bp.route('/search', methods=['GET', 'POST'])
def search():
    title = "Search"

    return render_template('search.html', title=title)


@explore_bp.route('/latest', methods=['GET', 'POST'])
def latest():
    title = "Latest Videos"

    return render_template('latest.html', title=title)


@explore_bp.route('/suggestions', methods=['GET', 'POST'])
def suggestions():
    title = "Suggestions"

    return render_template('explore.html', title=title)



