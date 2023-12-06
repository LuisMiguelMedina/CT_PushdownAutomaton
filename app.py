# app.py
from flask import Flask, render_template, request
from pda.palindrome import PalindromePDA
from lexer.lexer import begin_lexing

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/check_palindrome', methods=['POST'])
def check_palindrome():
    input_string = request.form['input_string']
    tokens = begin_lexing(input_string)

    pda = PalindromePDA()
    token_values = [token.value for token in tokens if token.type != 'ERROR']

    if len(input_string) % 2 != 0 or len(token_values) != len(tokens):
        result = "Invalid input: String contains illegal characters or is not of even length."
    else:
        accepted = pda.process_token(token_values)
        result = "String accepted: It is an even-length palindrome." if accepted else "String rejected: It is not an even-length palindrome."

    return render_template('result.html', input_string=input_string, result=result)


if __name__ == '__main__':
    app.run(debug=True)
