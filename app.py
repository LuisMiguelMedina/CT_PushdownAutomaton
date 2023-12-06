from flask import Flask, request, jsonify
from pda.palindrome import PalindromePDA
from lexer.lexer import begin_lexing
import os
import signal

app = Flask(__name__)

@app.route('/simulate', methods=['POST'])
def simulate_pda_api():
    data = request.json
    string = data.get('string')

    tokens, illegal_characters = begin_lexing(string)
    token_values = [token.value for token in tokens]
    pda = PalindromePDA()
    results = []

    for i, token in enumerate(token_values):
        pda.process_token(token, i, len(token_values))
        results.append({
            "estado": pda.get_current_state(),
            "por_leer": string[i+1:],
            "pila": pda.get_stack_contents()
        })

    pda.finalize()
    cadena_aceptada = pda.get_current_state() == 'f'

    response = {
        "resultados": results,
        "caracteres_ilegales": illegal_characters,
        "cadena_aceptada": cadena_aceptada
    }

    return jsonify(response)

    return jsonify(response)

@app.errorhandler(Exception)
def handle_error(e):
    return jsonify(error=str(e)), 500

@app.route('/shutdown', methods=['POST'])
def shutdown():
    os.kill(os.getpid(), signal.SIGTERM)
    return "Servidor detenido"


if __name__ == '__main__':
    app.run(debug=True)
