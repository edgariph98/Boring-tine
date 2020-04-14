from flask_wtf import FlaskForm, Form
from wtforms import StringField, SubmitField, SelectField, IntegerField, SelectMultipleField
from wtforms.validators import DataRequired, Length, InputRequired


#this is thhe form that handles the parameters for mood quiz request
class MoodQuizForm(FlaskForm):
    
    moodOptions = [('1','Happy'), ('2','Sad'), ('3','Mad'), ('4','Energetic'), ('5', 'CLear')]
    questions = SelectMultipleField(u'Programming Language', choices=moodOptions)
    name =  StringField('Name', validators=[InputRequired()])
    mood = SelectField(label='Mood', choices=moodOptions)
    age = IntegerField('Age',validators=[InputRequired()])
    gender = StringField('Gender',validators=[InputRequired()])
    interests = StringField('Interests',validators=[InputRequired()])
    submit = SubmitField('Submit')