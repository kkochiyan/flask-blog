from flask import Blueprint, render_template, request
from sqlalchemy import desc
from app.models import Article

search_bp = Blueprint('search', __name__)

@search_bp.route('/search', methods=['POST', 'GET'])
def search():
    if request.method == 'POST':
        word = request.form.get('word', '')

        res = (
            Article.query
            .filter(Article.title.like(f'%{word}%'))
            .order_by(desc(Article.date))
            .all()
        )

        return render_template('needs-posts.html', articles=res)
    else:
        return render_template('needs-posts.html')