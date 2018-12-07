from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from models import db
from views import index, detail, vector, update, delete


def create_app():
    '''
    Bootstrap the app with actual Bootstrap css
    :return: the flask application
    '''
    app = Flask(__name__)
    return app

app = create_app()
app.config['MONGODB_SETTINGS'] = {'DB': 'AndroBugs_DBs'}
app.config['TESTING'] = True
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
app.config['SECRET_KEY'] = 'aosenuthaoesunth'
app.debug = True

db.init_app(app)
DEBUG_TOOLBAR_ENABLED = True
#toolbar = DebugToolbarExtension(app)
from myfilters import *
app.add_url_rule('/', view_func=index)
app.add_url_rule('/detail/<md5>', view_func=detail)
app.add_url_rule('/vector/<vector_title>', view_func=vector)
app.add_url_rule('/update', view_func=update, methods=['POST'])
app.add_url_rule('/delete/<id>', view_func=delete, methods=['POST'])



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
