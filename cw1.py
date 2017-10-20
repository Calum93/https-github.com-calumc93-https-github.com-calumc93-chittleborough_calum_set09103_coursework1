from flask import Flask, render_template
app = Flask(__name__)

@app.route('/home/')
def root ():
  return render_template('home1.html'), 200

@app.route('/home/movies/')
def inheritsm():
  return render_template('movies.html'), 200

@app.route('/home/movies/starwars/')
def inheritssw():
  return render_template('starwars.html'), 200

@app.route('/home/movies/serenity/')
def inheritss():
  return render_template('serenity.html'), 200

@app.route('/home/movies/sunshine/')
def inheritsss():
  return render_template('sunshine.html'), 200

@app.route('/home/games/')
def inheritsg():
  return render_template('games.html'), 200

@app.route('/home/games/horizon/')
def inheritsh():
  return render_template('horizon.html'), 200

@app.route('/home/gamess/masseffect/')
def inheritsme():
  return render_template('masseffect.html'), 200

@app.route('/home/gamess/ark/')
def inheritsa():
  return render_template('ark.html'), 200

@app.route('/home/tv/')
def inherits():
  return render_template('tv1.html'), 200

@app.route('/home/tv/stargate/')
def inheritssg():
  return render_template('stargate.html'), 200

@app.route('/home/tv/firefly/')
def inheritsff():
  return render_template('firefly.html'), 200

@app.route('/home/tv/startrek/')
def inheritsst():
  return render_template('startrek.html'), 200

@app.errorhandler(404)
def page_not_found(error):
  return render_template('error.html'), 200

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
