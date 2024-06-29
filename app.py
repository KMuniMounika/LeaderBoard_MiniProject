

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
# def index():
    # return render_template('index.html')
    #return ""

@app.route('/student_registration')
def student_registration():
    return render_template('student_registration.html')

@app.route('/assessment_creation')
def assessment_creation():
    return render_template('assessment_creation.html')

@app.route('/result_update')
def result_update():
    return render_template('result_update.html')

@app.route('/leaderboard')
def leaderboard():
    return render_template('leaderboard.html')

if __name__ == '__main__':
    app.run(debug=True)
