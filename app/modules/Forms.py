from flask_wtf import FlaskForm, Form
from wtforms import StringField, SubmitField, SelectField, IntegerField, SelectMultipleField
from wtforms.validators import DataRequired, Length, InputRequired
#helper functions
#gets the questions from a form
def getQuestions(form):
    return [form.question1,form.question2,form.question3,form.question4,form.question5,form.question6,form.question7,form.question8,form.question9,form.question10]
#validates questions responses
def questionsValidation(form):
    validResponses = True
    errorMessage = "Please choose an input for questions: "
    qNum = 1
    questions = [form.question1,form.question2,form.question3,form.question4,form.question5,form.question6,form.question7,form.question8,form.question9,form.question10]
    for question in questions:
        if question.data == '-1':
            validResponses = False
            errorMessage = errorMessage + "Q" + str(qNum) + ", "
        qNum +=1
    return validResponses, errorMessage

def questionData(form):
    arguments = []
    questions = getQuestions(form)
    for question in questions:
        arguments.append(int(question.data))
    return arguments
#this is thhe form that handles the parameters for mood quiz request
class MoodQuizForm(FlaskForm):
    moodOptions = [('happy','Happy'),('sad','Sad'),('energy','Energetic'),('scared','Scared'),('Mad','Mad')]
    options = [('-1','-choose option-'),('1','strongly agree'), ('2','agree'), ('3', 'neutral'), ('4', 'disagree'), ('5', 'strongly disagree')]
    
    question1 = SelectField(u'Q1. I view myself as enthusiastic, extraverted:', choices=options)
    question2 =  SelectField(u'Q2. I am quarrelsome, critical:', choices=options)
    question3 = SelectField(u'Q3. I am dependable, self disciplined:', choices=options)
    question4 =  SelectField(u'Q4. I am anxious or easily upset:', choices=options)
    
    question5 = SelectField(u'Q5. I am open to new experiences, complex:', choices=options)
    question6 =  SelectField(u'Q6. I am reserved, quiet:', choices=options)
    question7 = SelectField(u'Q7. I am sympathetic, warm:', choices=options)
    question8 =  SelectField(u'Q8. I am disorganized, careless:', choices=options)
    question9 = SelectField(u'Q9. I am calm, emotionally stable:', choices=options)
    question10 =  SelectField(u'Q10. I am conventional, uncreative:', choices=options)
    submit = SubmitField('Submit')
    questions = [question1,question2,question3,question4,question5,question6,question7,question8,question9,question10]