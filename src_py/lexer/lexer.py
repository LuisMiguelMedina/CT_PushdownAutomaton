import ply.lex as lex

tokens = (
    "A",
    "B",
)

t_A = r"a"
t_B = r"b"
t_ignore = " \t"


def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)


lexer = lex.lex()
