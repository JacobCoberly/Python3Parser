# Python3Parser

Basic Python parser using ANTLR. Supports simple variable assignments, mathematical expressions, if statements, loops, and functions. Includes a Python3Grammar.g4 file, which defines the grammar, and a Python3Parser.py file, which translates the grammar into python 3. Also contains a testCode.py file to test the parser on. Other files are necessary dependants created by ANTLR, some of which are hand modified.

Designed by Jacob Coberly.
Utilizes some code from https://github.com/antlr/grammars-v4/blob/master/python/python3/.
Utilized code is marked in the respective files.

## How to use on Mac
1. Install Python IDLE Shell 3.9.12 in your terminal.
2. Download antlr v4.11.1 from the antlr website.
3. Add the .jar file to the /usr/local/lib folder
4. Download all files in the directory. Navigate to the directory where these files are stored in the terminal.
5. Run the following commands in the terminal, in order:  
- $ export CLASSPATH=".:/usr/local/lib/antlr-4.11.1-complete.jar:$CLASSPATH"  
- $ python3 Python3Parser.py testCode.py  
The testCode.py document can be modified or replaced with any Python 3 document that you wish to parse.

## Recompiling the grammar
It is recommended that you do **not** recompile the grammar if avoidable. If you do, ensure you modify Python3GrammarLexer in the following way:
1. On line 131, change the line from  
    - class Python3GrammarLexer(Lexer):  

   to  
    - class Python3GrammarLexer(Python3LexerBase):

To recompile the grammar:
1. Install Python IDLE Shell 3.9.12 in your terminal.
2. Download antlr v4.11.1 from the antlr website.
3. Add the .jar file to the /usr/local/lib folder
4. Download all files in the directory. Navigate to the directory where these files are stored in the terminal.
5. Run the following commands in the terminal, in order:  
- $ export CLASSPATH=".:/usr/local/lib/antlr-4.11.1-complete.jar:$CLASSPATH"  
- $ alias antlr4='java -Xmx500M -cp "/usr/local/lib/antlr-4.11.1-complete.jar:$CLASSPATH"  
- $ antlr4 -Dlanguage=Python3 Python3Grammar.g4
