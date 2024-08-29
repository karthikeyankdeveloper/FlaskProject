from flask import Flask, render_template, request
# for ibm
# import ibm_db
# conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=764264db-9824-4b7c-82df-40d1b13897c2.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=32536;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=hhn68702;PWD=JDmq4keRKWs2f0Mi", '', '')
# end of ibm


app = Flask(__name__) 

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/loginuser')
def loginuser():
    return render_template('login_user.html')

@app.route('/loginadmin')
def loginadmin():
    return render_template('login_admin.html')

@app.route('/signupuser')
def signupuser():
    return render_template('signup_user.html')

@app.route('/signupadmin')
def signupadmin():
    return render_template('signup_admin.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
