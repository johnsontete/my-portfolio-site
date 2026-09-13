from flask import Flask,render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resume')
def resume():
      return send_from_directory(directory='resume', path='Resume.pdf')

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')



