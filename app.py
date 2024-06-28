from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    user_data = None
    if request.method == 'POST':
        name = request.form.get('name')
        city = request.form.get('city')
        hobbies = request.form.get('hobbies')
        age = request.form.get('age')
        user_data = {
            'name': name,
            'city': city,
            'hobbies': hobbies,
            'age': age,
        }
    return render_template('index.html', user_data=user_data)

if __name__ == '__main__':
    app.run(debug=True)