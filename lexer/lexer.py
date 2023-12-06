# lexer.py
import ply.lex as lex

tokens = (
    "A",
    "B",
    "ERROR"
)

t_A = r'a'
t_B = r'b'
t_ignore = ' \t'

def t_error(t):
    t.type = "ERROR"  # Cambiar el tipo a ERROR
    t.value = t.value[0]  # Conservar solo el caracter ilegal
    t.lexer.skip(1)
    return t


lexer = lex.lex()

def begin_lexing(string):
    lexer.input(string)
    return list(lexer)
