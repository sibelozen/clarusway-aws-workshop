from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST', 'GET'])
def index_post():
    number = (request.form['number'])
    mappings ={1000: "M", 900: "CM", 500: "D", 100: "C", 90 :"XC", 50: "L", 40: "XL", 10: "X", 
                9: "IX", 5: "V", 4: "IV", 1: "I"} 
    # 1994 "MCMXCIV"
    result = ""
    if not number.isdigit():
        return render_template("index.html", not_valid=True)
        #return("Not Valid! Please enter a number between 1 and 3999, inclusively.")

    else:
        if int(number)<1 or int(number)>3999:
            return render_template("index.html", not_valid=True)

        elif int(number)>=1 and int(number)<=3999:
            number=int(number)
            for k, v in mappings.items(): # k =1000
                value = number // k # 1
                result += v * value # M *1
                number%=k # 994
                    # "MCMXCIV"
    return render_template('result.html', number_decimal=request.form['number'], number_roman=result,developer_name='Sibel', not_valid=False)

@app.route('/', methods=['POST'])
def result_get():
    return (index_post())

if __name__ == '__main__':
    # app.run('localhost', port=5000, debug=True)  
     app.run(debug=True)   
     app.run('0.0.0.0', port=80)