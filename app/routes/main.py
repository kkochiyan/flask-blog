from flask import Blueprint, render_template, request, redirect
from app import db
from app.models import Article

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    article_index = Article.query.order_by(Article.date.desc()).all()
    return render_template('index.html', articles=article_index)

@main_bp.route('/about')
def about_us():
    return render_template('about.html')

@main_bp.route('/create-article', methods=['POST', 'GET'])
def create_article():
    if request.method == 'POST':
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']

        article = Article(title=title, intro=intro, text=text)

        try:
            db.session.add(article)
            db.session.commit()
            return redirect('/')
        except:
            return 'При добавлении статьи произошла ошибка'
    else:
        return render_template('create-article.html')