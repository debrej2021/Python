from flask import Flask , request , jsonify , render_template

app = Flask(__name__)

products = [{"name": "bats", "price": 40}, {"name": "ball", "price": 20}]

@app.route('/')

def home():
    return render_template("index.html")


@app.route('/addnum/<n1>/<n2>')
def add(n1,n2):
 num = str(int(n1)+int(n2))

 return num

@app.route('/subtract/<n1>/<n2>')

def subtract(n1,n2):
 num = str(int(n1)-int(n2))
 return num



@app.route('/add', methods=['GET'])
def add_numbers():
    num1 = request.args.get('num1')
    num2 = request.args.get('num2')
    
    if num1 is None or num2 is None:
        return jsonify({'error': 'Please provide both num1 and num2'}), 400

    try:
        result = float(num1) + float(num2)
    except ValueError:
        return jsonify({'error': 'Both num1 and num2 must be numbers'}), 400

    return jsonify({'result': result})

@app.route('/addnumpost', methods=['POST'])
def add_numbers1():
    data = request.get_json()
    num1 = data.get('num1')
    num2 = data.get('num2')
    
    if num1 is None or num2 is None:
        return jsonify({'error': 'Please provide both num1 and num2'}), 400

    try:
        result = float(num1) + float(num2)
    except ValueError:
        return jsonify({'error': 'Both num1 and num2 must be numbers'}), 400

    return jsonify({'result': result})

@app.route('/addnumwith', methods=['GET'])
def add_numbers2():
    num1 = request.args.get('num1')
    num2 = request.args.get('num2')
    
    if num1 is None or num2 is None:
        return "Please provide both num1 and num2", 400

    try:
        result = float(num1) + float(num2)
    except ValueError:
        return "Both num1 and num2 must be numbers", 400

    return f"Result: {result}"
if __name__ == '__main__':

    app.run(debug=True)
