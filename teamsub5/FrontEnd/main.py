from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/')
def input():
    return render_template('input.html')

@app.route('/result',methods=['POST','GET'])
def result():
    if request.method =='POST':
        result=dict()
        result['Name']=request.form.get('name')
        result['Student Number']=request.form.get('StudentNumber')
        result['University'] = request.form.get('University')
        result['Major']=request.form.get('Major')
        result['Gender']=request.form.get('Gender')
        email_prefix = request.form.get('Email')
        email_domain = request.form.get('email_domain')
        result['Email'] = f"{email_prefix}@{email_domain}"
        result['Programming Languages']=" ".join(request.form.getlist('PL'))
        return render_template('result.html',result=result)

if __name__ =='__main__':
     app.run(debug=True)
     
