from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    try:
        num1 = int(data['num1'])
        num2 = int(data['num2'])
    except ValueError:
        return jsonify({'error': 'Invalid input'}), 400
    
    operator = data['operator']

    if operator == 'add':
        result = num1 + num2
    elif operator == 'subtract':
        result = num1 - num2
    elif operator == 'multiply':
        result = num1 * num2
    elif operator == 'divide':
        if num2 == 0:
            return jsonify({'error': 'Cannot divide by zero'}), 400, 
        result = num1 / num2
    else:
        return jsonify({'error': 'Invalid operator'}), 400

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
