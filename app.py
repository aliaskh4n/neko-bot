from flask import Flask, render_template, request, jsonify
from database import db

sql = db.Sqlite('data.db')
app = Flask(__name__)

@app.route('/')
def load():
    return render_template('load.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/anime-info')
def anime_info():
    anime_id = request.args.get('id')
    if anime_id == '123625':
        anime = sql.get_anime(anime_id)
        return render_template('anime_info.html', id=anime[0], series=anime[1], name=anime[2], description=anime[3], photo=anime[4],)

@app.route('/history')
def history():
    return render_template('history.html')

@app.route('/anime')
def anime():
    anime_id = request.args.get('id')
    anime_serie = request.args.get('serie')
    anime_series = int(request.args.get('series'))
    anime = sql.get_anime(anime_id)
    serie = sql.get_series(anime_id, anime_serie)
    return render_template('watch_anime.html', name=anime[2], url=serie[2], series=anime_series, id=anime_id, serie=anime_serie)


app.run(ssl_context='adhoc', debug=True, threaded=True)