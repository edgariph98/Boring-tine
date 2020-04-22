from flask import Flask, render_template, url_for, flash, redirect, request
from flask_bootstrap import Bootstrap
import json
from .modules import personality_test, MoodQuizForm, questionsValidation, getQuestions, questionData, getNthMovieGenres, getNthMusicGenres, getNthBookGenres, getPersonality, getAllBooks, MovieFinder, getAllSongs

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'aDm0iW55TDrBldJ6dMbd'
    mf = MovieFinder()
    ########################################
    #          Main Page Route             #
    ########################################
    @app.route('/', methods=['GET','POST'])
    @app.route('/home', methods=['GET','POST'])
    def home():
        return render_template("home.html")


    #########################################
    #       Mood Quiz Form Page Route       #
    #########################################
    @app.route('/MoodQuiz', methods=['GET', 'POST'])
    def moodQuizRoute():
        #validating form
        quizMoodForm = MoodQuizForm()
        if quizMoodForm.validate_on_submit():
            validQuestionsResponses, error_msg = questionsValidation(quizMoodForm)
            questions = getQuestions(quizMoodForm)
            if not validQuestionsResponses:
                print("Questions Not validated")
                flash(error_msg,'danger')
            else:
                print("Quiz Form Validated")
                personalities = getPersonality(*questionData(quizMoodForm))
                movieGenres = getNthMovieGenres(personalities)
                musicGenres = getNthMusicGenres(personalities)
                bookGenres = getNthBookGenres(personalities)
                songs = getAllSongs(musicGenres,2)
                movies = mf.getMovies(movieGenres,4)
                books = getAllBooks(bookGenres,1)
                # uris = [['6GmUVqe73u5YRfUUynZK6I',"let her go"], ['41yIvlFgvGwxq8qTqAR7eG',"Bloom"]]
                flash('Quiz Submitted', 'success')
                # return redirect(url_for('Suggestions'), personalities = personalities)
                return render_template("Suggestions.html",personalities = personalities, songs=songs, books=books, movies=movies)
        #form not validated stay in sam
        elif request.method == "POST":
            flash('Quiz not Submitted, Revise your inputs', 'danger')
            print(quizMoodForm.errors)
            print("Form Not Validated")
        return render_template("MoodQuiz.html", form = quizMoodForm)

    @app.route('/Explore', methods= ['GET','POST'])
    def Explore():
        return render_template('Explore.html')

    @app.route('/Suggestions', methods= ['GET', 'POST'])
    def Suggestions():
        return render_template("Suggestions.html")

    @app.route('/ActivitySearch', methods=['GET','POST'])
    def ActivitySearch():
        return render_template('ActivitiesSearch.html')

    return app
if  __name__ == "__main__":

    create_app().run(debug=True)