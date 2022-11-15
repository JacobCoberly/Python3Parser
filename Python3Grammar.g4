grammar Python3Grammar;

@lexer::members {
    depth = 0
    n = 0
}

//Data types
INT : [0-9]+ ; //Integer
FLT : INT '.' INT ; //Float
BOOL : 'TRUE' | 'FALSE' ; //Boolean
STR : '\'' ~('\n')*? '\'' //String with single quotes
    | '"' ~('\n')*? '"' //String with double quotes
    ;
CMPLX : (INT | FLT) 'i'? ('+' | '-') (INT | FLT) 'j' ; //Complex number
lst : '[' ']' | '[' (val | VAR) (',' (val | VAR))* ']' ; //List
dict_ : '{' '}' | '{' (val | VAR) ':' (val | VAR) (',' (val | VAR) ':' (val | VAR))* '}' ; //dictionary
set_ : '{' '}' | '{' (val | VAR) (',' (val | VAR))* '}' ; //set
tup : '(' ')' | '(' (val | VAR) (',' (val | VAR))* ')' ; //Tuple
NONE : 'None' ;

//Intermediate data types
num : INT | FLT | CMPLX ; //Number (integer or float)
array : STR | lst | set_ | tup | dict_ ; //Array
val : num | BOOL | array ; //Any data value

//Operators
arop : '+' | NEG | '*' | '/' | '%' ; //Arithmatic Operation
NEG : '-' ;
ASOP : '-=' | '+=' | '*=' | '/=' ; //Assignment Operation (excluding EQU)
EQU : '=' ;
CONOP : '==' | '!=' | '<' | '>' | '<=' | '>=' | 'and' | 'or' | 'is' | 'not' | IN ; //Conditional Operation
IN : 'in' ;

//KEYWORDS
IF : 'if' ;
ELIF : 'elif' ;
ELSE : 'else' ;
WHILE : 'while' ;
FOR : 'for' ;

//Misc
VAR : ( [a-z] | [A-Z] | '_' )([a-z] | [A-Z] | [0-9] | '_' )* ; //Variable Name
NL : '\n'+ ;
INDENT : '    ' ;
COMMENT : '#' ~'\n'* -> skip ;
WS : ' ' -> skip ; //Skip white spaces

//Core expressions
arithExp : arithExp (arop arithExp)+ | (num | VAR) | '(' arithExp ')' | NEG arithExp ;
arithAssignExp : VAR ASOP arithExp ;
assignExp: VAR EQU (VAR | array | arithExp | NONE) ;
conExp : (val | VAR) (CONOP (val | VAR))* | '(' conExp ')' ;
//If statements
ifExp : IF conExp ':' {depth = depth+1} ;
elifExp : ELIF conExp ':' {depth = depth+1} ;
elseExp : ELSE ':' {depth = depth+1} ;
ifStmt : ifExp NL program {depth = depth-1}
    (NL elifExp NL program {depth = depth-1})*
    (NL elseExp NL program {depth = depth-1})? ;
//While loops
whileExp : WHILE conExp ':' {depth = depth+1} ;
forExp: FOR (val | VAR) IN array ':' {depth = depth+1} ;
//This one is troublesome (+?)
indentation : INDENT* ;

exp : indentation (arithAssignExp | assignExp | ifStmt) ;
program: NL? (exp NL)* exp? ;
