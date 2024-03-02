from flask import Flask, render_template
from data import db_session
from data.users import User
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/', methods=['GET', 'POST'])
def work():
    db_sess = db_session.create_session()
    return render_template('index.html', info=db_sess.query(User, Jobs).filter(User.id == Jobs.team_leader))


def main():
    db_session.global_init("db/blog.db")
    app.run(port=8000, host='127.0.0.1', debug=True)


if __name__ == '__main__':
    main()