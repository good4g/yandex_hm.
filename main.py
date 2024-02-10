from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Колонизация</title>
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css"
                     rel="stylesheet"
                      integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN"
                       crossorigin="anonymous">
                  </head>
                  <body>
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}"/>
                    <h1>Жди нас, Марс!</h1>
                    <img width=250px src="{url_for('static', filename='image/mars.jpeg')}"/>
                    <div class="alert alert-primary" role="alert">
                      <h4>Человечество вырастает из детства<h4/>
                    </div>
                    <div class="alert alert-secondary" role="alert">
                      <h4>Человечеству мала одна планета.<h4/>
                    </div>
                    <div class="alert alert-success" role="alert">
                      <h4>Мы сделаем обитаемыми безжизненные пока планеты.<h4/>
                    </div>
                    <div class="alert alert-danger" role="alert">
                      <h4>И начнем с Марса!<h4/>
                    </div>
                    <div class="alert alert-warning" role="alert">
                      <h4>Присоединяйся!<h4/>
                    </div>
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')