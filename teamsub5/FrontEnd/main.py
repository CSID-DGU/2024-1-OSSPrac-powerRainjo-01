from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def input():
    return render_template('input.html')

@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        result = {}
        result['Name'] = request.form.get('name')
        result['Student Number'] = request.form.get('student_number')
        result['University'] = request.form.get('university')
        result['Major'] = request.form.get('major')
        result['Gender'] = request.form.get('gender')
        email_prefix = request.form.get('email_prefix')
        email_domain = request.form.get('email_domain')
        result['Email'] = f"{email_prefix}@{email_domain}"
        result['Programming Languages'] = ", ".join(request.form.getlist('languages'))
        return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
