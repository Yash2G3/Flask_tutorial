from flask import Flask, render_template,jsonify

app = Flask(__name__)
#this __name is a special variable in python whose values are :
#1. main( if the current script is the main script
# 2. or name of the current script  (if the current script is a secondary script)

# note : scripts are also called modules

JOBS  = [
  {
    'id':1, 
    'title' : 'Machine Learning Engineer',
    'location' : 'Bengaluru, India',
    'salary' : 'Rs 22,00,000'
  },

  {
    'id':2, 
    'title' : 'Systems Engineer',
    'location' : 'New Delhi, India'
  },

  {
    'id':3, 
    'title' : 'Data Analyst',
    'location' : 'Bombay, India',
    'salary' : 'Rs 14,00,000'
  },

  {
    'id':4, 
    'title' : 'Machine Learning Engineer',
    'location' : 'New York City , New York, USA',
    'salary' : '$ 250,000'
  },

  {
    'id':5, 
    'title' : 'AI Systems Manager',
    'location' : 'Los Angeles, USA',
    'salary' : '$500,000'
  }
]


@app.route("/") #this route renders the info(above dict JOBS) as an html template
def hello_world():
  return render_template('home.html', jobs = JOBS, company_name= "Jovian Careers")

@app.route("/api/jobs") #this route shows the same dict as a json file i.e as a JavaScript object file
def show_json():
  return jsonify(JOBS)

if __name__ == "__main__":  #checs if the current script is the main script
  app.run(host="0.0.0.0", debug=True)

  # host = 0.0.0.0 meas that we run this app on a local machine
  # debug = True means that any change in code is immediately reflected in the output page