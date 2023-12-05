import ply.lex as lex

tokens = (
    "A",
    "B",
)

t_A = r"a"
t_B = r"b"
t_ignore = " \t"


def t_error(t):
    if not hasattr(t.lexer, 'illegal_characters'):
        t.lexer.illegal_characters = []
    t.lexer.illegal_characters.append(t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()


def begin_lexing(string):
    lexer.input(string)
    lexer.illegal_characters = []
