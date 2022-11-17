# Python3Parser

Basic python parser using ANTLR. Supports simple variable assignments, mathematical expressions, if statements, loops, and functions. Includes a Python3Grammar.g4 file, which defines the grammar, and a Python3Parser.py file, which translates the grammar into python 3. Also contains a testCode.py file to test the parser on.

Designed by Jacob Coberly.

# How to use on Mac
1. Install python 3.
2. Download antlr v4.11.1 from the antlr website.
3. Add the .jar file to the /usr/local/lib folder
4. Run the following commands in your terminal:
  a. $ export CLASSPATH=".:/usr/local/lib/antlr-4.11.1-complete.jar:$CLASSPATH"
  b. $ alias antlr4='java -Xmx500M -cp "/usr/local/lib/antlr-4.11.1-complete.jar:$CLASSPATH" org.antlr.v4.Tool'
5. Download the Python3Grammar.g4 file and the Python3Parser.py file. Navigate to the directory where these files are stored.
6. Run the following command:
  a. $ antlr4 -Dlanguage=Python3 Python3Grammar.g4
7. Run the following command:
  a. $ python3 Python3Parser.py testCode.py
