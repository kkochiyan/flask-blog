from flask import Blueprint, render_template, request, redirect
from app import db
from app.models import Article

articles_bp = Blueprint('articles', __name__)

# Главная страница со статьями (будет в main.py)
# Остальные маршруты оставляем как были

@articles_bp.route('/posts')
def posts():
    articles = Article.query.order_by(Article.date.desc()).all()
    return render_template('posts.html', articles=articles)

@articles_bp.route('/posts/<int:id>')
def post_detail(id):
    article = Article.query.get(id)
    return render_template('post-info.html', article=article)

@articles_bp.route('/posts/<int:id>/update', methods=['POST', 'GET'])
def post_update(id):
    article = Article.query.get(id)
    if request.method == 'POST':
        article.title = request.form['title']
        article.intro = request.form['intro']
        article.text = request.form['text']

        try:
            db.session.commit()
            return redirect('/posts')
        except:
            return 'При редактировании статьи произошла ошибка'
    else:
        return render_template('post-update.html', article=article)

@articles_bp.route('/posts/<int:id>/del')
def post_delete(id):
    article = Article.query.get_or_404(id)

    try:
        db.session.delete(article)
        db.session.commit()
        return redirect('/posts')
    except:
        return 'При удалении статьи произошла ошибка'