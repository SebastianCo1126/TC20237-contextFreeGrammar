import nltk
from nltk import CFG

nltk.download('punkt')

grammar = CFG.fromstring("""
    S -> E
    E -> P F
    F -> '+' E |'-' E | '.'
    P -> INT T DIFF
    T -> VAR EXP | CONST R | CONST | '.'
    R -> VAR EXP | CONST T | '.'
    INT -> '%'
    DIFF -> 'dx'
    VAR -> 'x'
    CONST -> '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
    EXP -> '^' CONST | '.'
""")

parser = nltk.ChartParser(grammar)


def parseIntegral(integral):
    '''
      Parse the given integral expression and print its parse tree.

      Args:
          integral (str): The integral expression to parse.

      Returns:
          None
    '''
    flag = False
    tokens = nltk.word_tokenize(integral)

    # Parse the integral
    for tree in parser.parse(tokens):
        tree.pretty_print()
        flag = True

    print(flag)

# Test section
testSentences = [
    "% 2 x ^ 2 dx .",
    "% 2 x ^ 2 dx + % 7 dx .",
    "% 2 x ^ 2 dx + % 5 x ^ 3 dx .",
    "% 8 1 x ^ 8 dx - % 7 2 1 x ^ 2 dx + % 5 dx .",
    "% 1 0 2 1 x . dx - % 1 2 x . dx + % 1 3 x ^ 9 dx - % 1 dx .",
    "% 1 3 x ^ 2 .",  # Invalid
    "% 7 x ^ 2 dx + % 1 7 x .",  # Invalid
    "% 4 5 1 x ^ 1 0 dx .",  # Invalid
    "% 1 0 dx + % 9 x ^ 4 - 1 0 dx .",  # Invalid
    "% 9 8 x ^ 5 dx - % 1 x ^ 2 + % 1 0 0 dx + 1 2 x dx"  # Invalid
]

for i, sentence in enumerate(testSentences, start = 1):
    print(f"\n### Test {i}")
    parseIntegral(sentence)
