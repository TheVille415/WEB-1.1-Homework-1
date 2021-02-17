# TODO: Follow the assignment instructions to complete the required routes!
# (And make sure to delete this TODO message when you're done!)

from flask import Flask
import random
app = Flask(__name__)

@app.route('/')
def homepage():
    """Shows a greeting to the user."""
    return 'Are you there, world? It\'s me, Ducky!'

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return f'Wow, {users_animal} is my favorite animal, too!'

@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    """Display a message to the user that changes based on their favorite dessert."""
    return f'How did you know I liked {users_dessert}'

@app.route('/madlibs/<adjective>/<noun>')
def madlibs(adjective, noun):
    """Display a message to the user that changes based on their noun and adjective choice."""
    return f'Becareful not to vacuum the {adjective} {noun}!'

@app.route('/multiply/<number1>/<number2>')
def multiply(number1, number2):
    """Display a message to the user that changes based on their numbers."""
    if number1.isdigit() and number2.isdigit() == True:
        # All route variables are of type string, which means you’ll need to cast them as integers 
        return f'{number1} times {number2} equals {(int(number1) * int(number2))}'
    else:
        return f'Invalid inputs. Please try again by entering 2 numbers!'

@app.route('/sayntimes/<word>/<n>')
def sayntimes(word, n):
    """Display a message to the user that changes based on their word and times they want to say it."""
    if n.isdigit() == True:
        number = int(n)
        for w in range(number):
            w = (word + " ") * number
            return f" {w} "
    else:
        return f'Invalid input. Please try again by entering a word and a number!'

@app.route('/dicegame')
def dicegame():
    """Display a dice game."""
    rolldice = random.randint(1,6)

    if rolldice == 6:
        return f'You rolled a {rolldice}. You won!'
    else:
        return f'You rolled a {rolldice}. You LOST YOU LOSER HAHAHA!'

# this turns on the server for serving!
if __name__ == '__main__':
    app.run(debug=True)