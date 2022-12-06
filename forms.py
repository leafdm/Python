from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField


class Form(FlaskForm):
    publication_day = StringField(label='Publication Day')
    categorie = StringField(label='Categorie')
    nb_worlds_title = StringField(label='Number of wolrd in the title')
    nb_worlds_article = StringField(label='Number of world in the article')
    nb_link = StringField(label='number of link')
    submit=SubmitField(label='Calculate the popularity')

