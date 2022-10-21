from property import app, db
from flask import render_template, redirect, url_for, flash, request
from property.forms import AddressForm
from property.models import User


@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home_page():
    form = AddressForm()

    if form.validate_on_submit():
        user_to_create = User(address=request.form['address'],
                              email_address=request.form['contact_details'])
        db.session.add(user_to_create)
        db.session.commit()

        return redirect(url_for("success_page"))

    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There was an error {err_msg}', category='danger')

    return render_template('home.html', form=form)


# @app.route("/contact_info", methods=['GET', 'POST'])
# def contact_info_page():
#     form = ContactForm()
#
#     if form.validate_on_submit():
#         user_to_create = User(address=request.form['address'],
#                               email_address=form.contact_details.data)
#         db.session.add(user_to_create)
#         db.session.commit()
#
#         return redirect(url_for("success_page"))
#
#     return render_template('contact_info.html', form=form)


@app.route("/success")
def success_page():
    return render_template('success.html')
