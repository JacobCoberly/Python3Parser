grammar Python3Grammar;

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
NL : '\n'+ ;
INDENT : '    ' ;
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
    (NL elifExp NL block)*
    (NL elseExp NL block)? ;
//While loops
whileExp : WHILE conExp ':' ;
forExp: FOR (val | VAR) IN (array | func) ':' ;
loopExp : whileExp | forExp ;
loopStmt : loopExp NL block ;
//This one is troublesome
indentation : INDENT* ;

exp : indentation (arithAssignExp | assignExp | ifStmt | loopStmt | funcDef | func | return) ;
program : NL? (exp NL)* exp? ;
block : (exp NL)* exp ;
