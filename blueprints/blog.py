from flask import Blueprint,render_template

bp = Blueprint("blog", __name__, url_prefix="/blog")

@bp.route('/')
def blog():
    return render_template('blog.html')
