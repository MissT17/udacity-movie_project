from flask import Flask, request, render_template
from test_api import create_film_list


app = Flask(__name__)


# Create a default URL
@app.route('/')
def user_input_form():
    return render_template('user_input.html')


@app.route('/user_output', methods=['POST'])
def User_submit():
    # Create a list of films entered by the user.
    requested_films = []
    film_request1 = request.form['first_film']
    film_request2 = request.form['second_film']
    film_request3 = request.form['third_film']
    requested_films.append(film_request1)
    requested_films.append(film_request2)
    requested_films.append(film_request3)
    create_film_list(requested_films)
    return render_template('fresh_tomatoes.html')

if __name__ == '__main__':
    app.run(debug=True)
