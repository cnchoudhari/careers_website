from flask import Flask, render_template

app = Flask(__name__)
JOBS = [{
  'id': 1,
  'title': ' Weibgh Bridge Operater',
  'location': ' Chandrapur ',
  'salary': ' Rs.10,000'
}]


@app.route('/')
def home():
  return render_template('home.html', jobs=JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
