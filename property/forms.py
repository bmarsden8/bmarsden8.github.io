from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class AddressForm(FlaskForm):
    address = StringField(label='address'
                          , validators=[DataRequired(message='Cannot be empty!')]
                          )
    contact_details = StringField(label='contact_info'
                                  , validators=[DataRequired(message='Cannot be empty')])
    submit = SubmitField(label='submit')

#
# class ContactForm(FlaskForm):
#     contact_details = StringField(label='contact_info')
#     submit = SubmitField(label='submit')
