import sys
from antlr4 import *
from antlr4.tree.Trees import Trees
from Python3GrammarLexer import Python3GrammarLexer
from Python3GrammarParser import Python3GrammarParser
#from Python3Grammar.g4 import Python3Grammar
 
def main(argv):
    input_stream = FileStream(argv[1])
    lexer = Python3GrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = Python3GrammarParser(stream)
    tree = parser.program()
    print(Trees.toStringTree(tree, None, parser))
 
if __name__ == '__main__':
    main(sys.argv)
