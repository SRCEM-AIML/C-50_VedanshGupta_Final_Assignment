from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    error = None
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        age = request.form.get('age', '').strip()

        if not name or not age.isdigit():
            error = "Invalid input! Please enter a valid name and age."
            return render_template('form.html', error=error)
        return f"Hello, {name}! You are {age} years old."
    
    return render_template('form.html', error=error)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
