from flask import Flask, render_template

app = Flask(__name__)
JOBS = [{
  'id': 1,
  'title': ' Plant operator',
  'location': ' Chandrapur ',
  'salary': ' Rs.22,000'
}, {
  'id': 2,
  'title': '  Welder',
  'location': ' Chandrapur ',
  'salary': ' Rs.15,000'
}, {
  'id': 3,
  'title': ' Weibgh Bridge Operater',
  'location': ' Chandrapur ',
  'salary': ' Rs.12,000'
}, {
  'id': 4,
  'title': ' Maintenance technician',
  'location': ' Chandrapur ',
  'salary': ' Rs.20,000'
}, {
  'id': 5,
  'title': ' Industrial electrician',
  'location': ' Chandrapur ',
  'salary': ' Rs.28,000'
}]


@app.route('/')
def home():
  return render_template('home.html', jobs=JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
