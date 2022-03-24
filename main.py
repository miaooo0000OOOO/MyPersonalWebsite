from flask import Flask
import config
from blueprints import index_bp, lib_bp, blog_bp, about_bp
#from exts import db

app = Flask(__name__)
app.config.from_object(config)
#db.init_app(app)

app.register_blueprint(index_bp)
app.register_blueprint(lib_bp)
app.register_blueprint(blog_bp)
app.register_blueprint(about_bp)

@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')

if __name__ == '__main__':
    app.run(debug=True)