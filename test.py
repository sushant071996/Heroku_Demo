from flask import Flask , render_template , request
import pickle


app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

@app.route('/')
def index():
    return "Hello World!.."

@app.route('/test')
def home():
    return render_template('index.html')

@app.route('/getData',methods=['POST'])
def home1():
    name = request.form['name']
    ApplicantIncome = int(request.form['ApplicantIncome'])
    gender = request.form['gender']
    Credit_History = float(request.form['Credit_History'])
    Loan_Amount_Term = int(request.form['Loan_Amount_Term'])
    loanAmount = int(request.form['loanAmount'])
    if gender=="Male":
        abc=int(1)
    else:
        abc=int(0)
    output = model.predict([[ApplicantIncome,loanAmount,Loan_Amount_Term,Credit_History,abc]])
    if output[0]==1:
        return render_template('index.html',prediction= " {} is Eligible for loan".format(name))
    else:
        return render_template('index.html',prediction= " {} is Not Eligible for loan".format(name))
    return ""

if __name__=="__main__":
    app.run(debug=True,use_reloader=False)