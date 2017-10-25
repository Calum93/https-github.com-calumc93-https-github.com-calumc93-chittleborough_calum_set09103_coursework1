from flask import Flask, render_template
app = Flask(__name__)

@app.route('/home/') #route to home page
def root ():
  return render_template('home1.html'), 200
  
@app.route('/home/movies/') #route to movies page
def inheritsm():
  return render_template('movies.html'), 200

@app.route('/home/movies/starwars/') #route to star wars page
def inheritssw():
  return render_template('starwars.html'), 200

@app.route('/home/movies/serenity/') #route to serenity page
def inheritss():
  return render_template('serenity.html'), 200

@app.route('/home/movies/sunshine/') #route to sunshine page
def inheritsss():
  return render_template('sunshine.html'), 200

@app.route('/home/games/') #route to games page
def inheritsg():
  return render_template('games.html'), 200

@app.route('/home/games/horizon/') #route to horizon page
def inheritsh():
  return render_template('horizon.html'), 200 

@app.route('/home/games/masseffect/') #route to mass effect page
def inheritsme():
  return render_template('masseffect.html'), 200

@app.route('/home/games/ark/') #route to ark page
def inheritsa():
  return render_template('ark.html'), 200

@app.route('/home/tv/') #route to tv  page
def inherits():
  return render_template('tv1.html'), 200

@app.route('/home/tv/stargate/') #route to stargate page
def inheritssg():
  return render_template('stargate.html'), 200

@app.route('/home/tv/firefly/') #route to firefly page
def inheritsff():
  return render_template('firefly.html'), 200

@app.route('/home/tv/startrek/') #route to star trek page
def inheritsst():
  return render_template('startrek.html'), 200

@app.errorhandler(404) #route to error page
def page_not_found(error):
  return render_template('error.html'), 200

#@app . route ('/config/')
#def config () :
 # str = []
 # str.append('Debug:'+app.config['DEBUG'])
 # str.append('port:'+app.config['port'])
 # str.append('url:'+app.config['url'])
  #str.append('ip_address:'+ app.config['ip_address'])
  #return '\t'.join(str)

# def init(app):
    # config = ConfigParser.ConfigParser()
     #try:
      #  config_location = "etc/ defaults.cfg"
       # config.read(config_location)

        #app.config ['DEBUG'] = config.get ("config", " debug ")
        #app.config ['ip_address'] = config.get ("config", " ip_address")
        #app.config ['port'] = config.get ("config ", " port ")
        #app.config ['url'] = config.get ("config ", "url")
   # except :
    #  print " Could not read configs from : ", config_location

# if __name__ == '__main__':
# init(app)
# app.run(
# host = app.config ['ip_address'],
# port =int ( app.config ['port']) )
if __name__ == ("__main__"):
    app.run(host='0.0.0.0', debug=True)
