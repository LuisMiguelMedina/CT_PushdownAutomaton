# lexer.py
import ply.lex as lex

tokens = ("A", "B", "ERROR")

t_A = r'a'
t_B = r'b'
t_ignore = ' \t'

def t_error(t):
    t.type = "ERROR"
    t.value = t.value[0]
    t.lexer.skip(1)
    return t


lexer = lex.lex()

def begin_lexing(string):
    lexer.input(string)
    tokens = [tok for tok in iter(lexer.token, None)]
    illegal_characters = [tok.value for tok in tokens if tok.type == "ERROR"]
    return tokens, illegal_characters

