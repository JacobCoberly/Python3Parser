grammar Python3Grammar;

//https://github.com/antlr/grammars-v4/blob/master/python/python3/Python3Lexer.g4
//Describe tokens but don't define
tokens { INDENT, DEDENT }

//Lexer should have superclass. not parser
//https://github.com/antlr/grammars-v4/blob/master/python/python3/Python3Lexer.g4
//options { superClass = Python3LexerBase; }

//Data types
INT : [0-9]+ ; //Integer
FLT : INT '.' INT ; //Float
BOOL : 'TRUE' | 'FALSE' ; //Boolean
STR : '\'' ~('\n')*? '\'' //String with single quotes
    | '"' ~('\n')*? '"' //String with double quotes
    ;
CMPLX : (INT | FLT) 'i'? ('+' | '-') (INT | FLT) 'j' ; //Complex number
lst : '[' ']' | '[' (data) (',' (data))* ']' ; //List
dict_ : '{' '}' | '{' (data) ':' (data) (',' (data) ':' (data))* '}' ; //dictionary
set_ : '{' '}' | '{' (data) (',' (data))* '}' ; //set
tup : '(' (data) (',' (data))+ ')' ; //Tuple
NONE : 'None' ;

//Intermediate data types
num : INT | FLT | CMPLX ; //Number (integer or float)
array : STR | lst | set_ | tup | dict_ ; //Array
val : num | BOOL | array ; //Any literal data value
data : val | VAR | func ; //Any data value

//Operators
arop : '+' | NEG | '*' | '/' | '%' ; //Arithmatic Operation
NEG : '-' ;
asop : '-=' | '+=' | '*=' | '/=' ; //Assignment Operation (excluding EQU)
EQU : '=' ;
conop : '==' | '!=' | '<' | '>' | '<=' | '>=' | 'and' | 'or' | 'is' | 'not' | IN ; //Conditional Operation

//KEYWORDS
IF : 'if' ;
ELIF : 'elif' ;
ELSE : 'else' ;
WHILE : 'while' ;
FOR : 'for' ;
IN : 'in' ;
DEF : 'def' ;
RETURN : 'return' ;

//Misc
VAR : ( [a-z] | [A-Z] | '_' )([a-z] | [A-Z] | [0-9] | '_' )* ; //Variable Name
//https://github.com/antlr/grammars-v4/blob/master/python/python3/Python3Lexer.g4
NL : ( {self.atStartOfInput()}?   SPACE
  | ( '\r'? '\n' | '\r' | '\f' ) SPACE?
  )
  {self.onNewLine();}
;
SPACE : '    '+ ;
COMMENT : '#' ~'\n'* -> skip ;
WS : ' ' -> skip ; //Skip white spaces

//Functions
func : VAR '(' ')' | VAR '(' (data) (',' (data))* ')' ;
funcVar : VAR '(' ')' | VAR '(' (VAR) (',' (VAR))* ')'  ;
funcDef : DEF funcVar ':' NL block ;
return : RETURN returnPar ;
returnPar : '(' returnPar ')' | (data | arithExp) ;

//Assignment/arithmatic expressions
arithExp : arithExp (arop arithExp)+
    | (num | VAR)
    | '(' arithExp ')'
    | NEG arithExp ;
arithAssignExp : VAR asop arithExp ;
assignExp: VAR EQU (VAR | array | arithExp | NONE | func) ;
//If statements
conExp : (data) (conop (data))* | '(' conExp ')' ;
ifExp : IF conExp ':' ;
elifExp : ELIF conExp ':' ;
elseExp : ELSE ':' ;
ifStmt : ifExp NL block
    (elifExp NL block)*
    (elseExp NL block)? ;
//While loops
whileExp : WHILE conExp ':' ;
forExp: FOR (val | VAR) IN (array | func) ':' ;
loopExp : whileExp | forExp ;
loopStmt : loopExp NL block ;

//Expressions with blocks should not be followed by NL
//because the block ends with a NL
exp : (arithAssignExp | assignExp | func | return) NL
    | (ifStmt | loopStmt | funcDef) ;
program : (exp | NL)* EOF ;
block : INDENT (exp | NL)* DEDENT ;
