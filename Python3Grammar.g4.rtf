grammar Python3Grammar;

//Data types
INT : [0-9]+ ; //Integer
FLT : INT '.' INT ; //Float
BOOL : 'TRUE' | 'FALSE' ; //Boolean
STR : '\'' ~('\n')*? '\'' //String with single quotes
    | '"' ~('\n')*? '"' //String with double quotes
    | '\'\'\'' .*? '\'\'\'' //Multiline string with single quotes
    | '"""' .*? '"""' //Multiline string with double quotes
    ;
CMPLX : (INT | FLT) 'i'? ('+' | '-') (INT | FLT) 'j' ; //Complex number
lst : '[' ']' | '[' (val | VAR) (',' (val | VAR))* ']' ; //List
dict_ : '{' '}' | '{' (val | VAR) ':' (val | VAR) (',' (val | VAR) ':' (val | VAR))* '}' ; //dictionary
set_ : '{' '}' | '{' (val | VAR) (',' (val | VAR))* '}' ; //set
tup : '(' ')' | '(' (val | VAR) (',' (val | VAR))* ')' ; //Tuple
NONE : 'None' ;

//Intermediate data types
num : INT | FLT | CMPLX; //Number (integer or float)
array : STR | lst ; //Array (string or list)
val : num | BOOL | array | set_ | tup | dict_ ; //Any data value

//Operators
AROP : '+' | NEG | '*' | '/' | '%' ; //Arithmatic Operation
NEG : '-' ;
ASOP : '-=' | '+=' | '*=' | '/=' ; //Assignment Operation (excluding EQU)
EQU : '=' ;
CONOP : '==' | '!=' | '<' | '>' | '<=' | '>=' | 'and' | 'or' | 'is' | 'not' | 'in' ; //Conditional Operation

//KEYWORDS
IF : 'if' ;
ELIF : 'elif' ;
ELSE : 'else' ;

//Misc
VAR : ( [a-z] | [A-Z] | '_' )([a-z] | [A-Z] | [0-9] | '_' )* ; //Variable Name
NL : '\n'+ ;
WS : ' ' -> skip ; //Skip white spaces

//Core expressions
arithExp : arithExp (AROP arithExp)+ | (num | VAR) | '(' arithExp ')' ;
arithAssignExp : VAR ASOP NEG? arithExp ;
assignExp: VAR EQU (VAR | array | dict_ | set_ | tup | NEG? arithExp | NONE) ;
conExp : (val | VAR) (CONOP (val | VAR))* ;
ifExp : IF conExp ':' ;
elifExp : ELIF conExp ':' ;
elseExp : ELSE ':' ;
ifStmt : ifExp (NL elifExp)* (NL elseExp)? ;
//blankExp : '\n' ;

exp : arithAssignExp | assignExp ;
program: NL? (exp NL)* exp? ;
