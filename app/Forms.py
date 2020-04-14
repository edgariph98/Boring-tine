from flask_wtf import FlaskForm, Form
from wtforms import StringField, SubmitField, SelectField, IntegerField, SelectMultipleField
from wtforms.validators import DataRequired, Length, InputRequired


#this is thhe form that handles the parameters for mood quiz request
class MoodQuizForm(FlaskForm):
    moodOptions = [('happy','Happy'),('sad','Sad'),('energy','Energetic'),('scared','Scared'),('Mad','Mad')]
    options = [('1','strongly agree'), ('2','agree'), ('3', 'neutral'), ('4', 'disagree'), ('5', 'strongly disagree')]
    
    question1 = SelectMultipleField(u'I view myself as enthusiastic, extraverted', choices=options)
    question2 =  SelectMultipleField(u'I am quarrelsome, critical', choices=options)
    question3 = SelectMultipleField(u'I am dependable, self disciplined', choices=options)
    question4 =  SelectMultipleField(u'I am anxious or easily upset', choices=options)
    
    question5 = SelectMultipleField(u'I am open to new experiences, complex', choices=options)
    question6 =  SelectMultipleField(u'I am reserved, quiet', choices=options)
    question7 = SelectMultipleField(u'I am sympathetic, warm', choices=options)
    question8 =  SelectMultipleField(u'I am disorganized, careless', choices=options)
    question9 = SelectMultipleField(u'I am calm, emotionally stable', choices=options)
    question10 =  SelectMultipleField(u'I am conventional, uncreative', choices=options)
    name =  StringField('Name', validators=[InputRequired()])
    mood = SelectField(label='Mood', choices=moodOptions)
    age = IntegerField('Age',validators=[InputRequired()])
    gender = StringField('Gender',validators=[InputRequired()])
    interests = StringField('Interests',validators=[InputRequired()])
    submit = SubmitField('Submit')