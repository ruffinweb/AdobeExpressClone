
from mediaApp.mm_app import db
from flask import url_for, render_template, redirect, request, flash, Blueprint
from mediaApp.mm_app.contact.models import ContactFormModel
from mediaApp.mm_app.contact.forms import ContactForm
from mediaApp.mm_app.contact.utils import send_contact_email

import os


contact_bp = Blueprint('contact', __name__, template_folder='templates')


@contact_bp.route('/contact', methods=['GET', 'POST'])
def contact():
    title = "Contact Page"
    contact_form = ContactForm()

    if request.method == 'POST' and contact_form.validate_on_submit():
        users_email = contact_form.email.data
        name = contact_form.name.data
        company = contact_form.company.data
        email = contact_form.email.data
        subject = contact_form.subject.data
        users_message = contact_form.content.data

        new_contact = ContactFormModel(
            name=name,
            company=company,
            email=email,
            subject=subject,
            content=users_message
        )
        db.session.add(new_contact)
        db.session.commit()
        send_contact_email(name, company, email, subject, users_message)
        flash('Your message has been recorded. I will respond ASAP!', 'success')
        return redirect(url_for('main.home'))

    return render_template('contact.html', title=title,
                           form=contact_form)


# @contact_bp.route('/submit_contact_form', methods=['POST'])
# def submit_contact_form():
#     referrer = request.referrer
#     # origin_route = referrer.split("50510/")[1]
#     # origin_vid_folder = origin_route.split("/")[1]
#
#     new_contact = contactFormModel(email=request.form["email"], first_name=request.form["first_name"],
#                                    last_name=request.form["last_name"], content=request.form["content"])
#     db.session.add(new_contact)
#     db.session.commit()
#
#     return redirect(url_for('main.home'))
