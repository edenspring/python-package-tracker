from flask_wtf import FlaskForm
from wtforms.fields import StringField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class PackageForm(FlaskForm):
    sender_name = StringField("Sender", validators=[DataRequired()])
    recipient_name = StringField("Recipient", validators=[DataRequired()])
    origin = SelectField("Origin", validators=[DataRequired()])
    destination = SelectField("Destination", validators=[DataRequired()])
    express = BooleanField("Express")
    submit = SubmitField("Submit")
    cancel = SubmitField("Cancel")

    def to_dict(self):
        return {
            "sender_name": self.sender_name.data,
            "recipient_name": self.recipient_name.data,
            "origin": self.origin.data,
            "destination": self.destination.data,
            "express": self.express.data,
            "submit": self.submit.data,
            "cancel": self.cancel.data
        }
