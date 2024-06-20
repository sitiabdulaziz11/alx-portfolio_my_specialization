from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
db = SQLAlchemy(app)
login = LoginManager(app)


if __name__ == '__main__':
    app.run(debug=True)