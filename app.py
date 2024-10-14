from flask import Flask
from models import db
from routes import task_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


def create_tables():
    db.create_all()

app.register_blueprint(task_bp)

if __name__ == '__main__':
    app.run(debug=True)
