# Generated from Python3Grammar.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .Python3GrammarParser import Python3GrammarParser
else:
    from Python3GrammarParser import Python3GrammarParser

# This class defines a complete listener for a parse tree produced by Python3GrammarParser.
class Python3GrammarListener(ParseTreeListener):

    # Enter a parse tree produced by Python3GrammarParser#lst.
    def enterLst(self, ctx:Python3GrammarParser.LstContext):
        pass

    # Exit a parse tree produced by Python3GrammarParser#lst.
    def exitLst(self, ctx:Python3GrammarParser.LstContext):
        pass


    # Enter a parse tree produced by Python3GrammarParser#dict_.
    def enterDict_(self, ctx:Python3GrammarParser.Dict_Context):
        pass

    # Exit a parse tree produced by Python3GrammarParser#dict_.
    def exitDict_(self, ctx:Python3GrammarParser.Dict_Context):
        pass


    # Enter a parse tree produced by Python3GrammarParser#set_.
    def enterSet_(self, ctx:Python3GrammarParser.Set_Context):
        pass

    # Exit a parse tree produced by Python3GrammarParser#set_.
    def exitSet_(self, ctx:Python3GrammarParser.Set_Context):
        pass


    # Enter a parse tree produced by Python3GrammarParser#tup.
    def enterTup(self, ctx:Python3GrammarParser.TupContext):
        pass

    # Exit a parse tree produced by Python3GrammarParser#tup.
    def exitTup(self, ctx:Python3GrammarParser.TupContext):
        pass


    # Enter a parse tree produced by Python3GrammarParser#num.
    def enterNum(self, ctx:Python3GrammarParser.NumContext):
        pass

    # Exit a parse tree produced by Python3GrammarParser#num.
    def exitNum(self, ctx:Python3GrammarParser.NumContext):
        pass


    # Enter a parse tree produced by Python3GrammarParser#array.
    def enterArray(self, ctx:Python3GrammarParser.ArrayContext):
        pass

    # Exit a parse tree produced by Python3GrammarParser#array.
    def exitArray(self, ctx:Python3GrammarParser.ArrayContext):
        pass


    # Enter a parse tree produced by Python3GrammarParser#val.
    def enterVal(self, ctx:Python3GrammarParser.ValContext):
        pass

    # Exit a parse tree produced by Python3GrammarParser#val.
    def exitVal(self, ctx:Python3GrammarParser.ValContext):
        pass


    # Enter a parse tree produced by Python3GrammarParser#data.
    def enterData(self, ctx:Python3GrammarParser.DataContext):
        pass

    # Exit a parse tree produced by Python3GrammarParser#data.
    def exitData(self, ctx:Python3GrammarParser.DataContext):
        pass


    # Enter a parse tree produced by Python3GrammarParser#arop.
    def enterArop(self, ctx:Python3GrammarParser.AropContext):
        pass

    # Exit a parse tree produced by Python3GrammarParser#arop.
    def exitArop(self, ctx:Python3GrammarParser.AropContext):
        pass


    # Enter a parse tree produced by Python3GrammarParser#asop.
    def enterAsop(self, ctx:Python3GrammarParser.AsopContext):
        pass

    # Exit a parse tree produced by Python3GrammarParser#asop.
    def exitAsop(self, ctx:Python3GrammarParser.AsopContext):
        pass


    # Enter a parse tree produced by Python3GrammarParser#conop.
    def enterConop(self, ctx:Python3GrammarParser.ConopContext):
        pass

    # Exit a parse tree produced by Python3GrammarParser#conop.
    def exitConop(self, ctx:Python3GrammarParser.ConopContext):
        pass


    # Enter a parse tree produced by Python3GrammarParser#func.
    def enterFunc(self, ctx:Python3GrammarParser.FuncContext):
        pass

    # Exit a parse tree produced by Python3GrammarParser#func.
    def exitFunc(self, ctx:Python3GrammarParser.FuncContext):
        pass


    # Enter a parse tree produced by Python3GrammarParser#funcVar.
    def enterFuncVar(self, ctx:Python3GrammarParser.FuncVarContext):
        pass

    # Exit a parse tree produced by Python3GrammarParser#funcVar.
    def exitFuncVar(self, ctx:Python3GrammarParser.FuncVarContext):
        pass


    # Enter a parse tree produced by Python3GrammarParser#funcDef.
    def enterFuncDef(self, ctx:Python3GrammarParser.FuncDefContext):
        pass

    # Exit a parse tree produced by Python3GrammarParser#funcDef.
    def exitFuncDef(self, ctx:Python3GrammarParser.FuncDefContext):
        pass


    # Enter a parse tree produced by Python3GrammarParser#return.
    def enterReturn(self, ctx:Python3GrammarParser.ReturnContext):
        pass

    # Exit a parse tree produced by Python3GrammarParser#return.
    def exitReturn(self, ctx:Python3GrammarParser.ReturnContext):
        pass


    # Enter a parse tree produced by Python3GrammarParser#returnPar.
    def enterReturnPar(self, ctx:Python3GrammarParser.ReturnParContext):
        pass

    # Exit a parse tree produced by Python3GrammarParser#returnPar.
    def exitReturnPar(self, ctx:Python3GrammarParser.ReturnParContext):
        pass


    # Enter a parse tree produced by Python3GrammarParser#arithExp.
    def enterArithExp(self, ctx:Python3GrammarParser.ArithExpContext):
        pass

    # Exit a parse tree produced by Python3GrammarParser#arithExp.
    def exitArithExp(self, ctx:Python3GrammarParser.ArithExpContext):
        pass


    # Enter a parse tree produced by Python3GrammarParser#arithAssignExp.
    def enterArithAssignExp(self, ctx:Python3GrammarParser.ArithAssignExpContext):
        pass

    # Exit a parse tree produced by Python3GrammarParser#arithAssignExp.
    def exitArithAssignExp(self, ctx:Python3GrammarParser.ArithAssignExpContext):
        pass


    # Enter a parse tree produced by Python3GrammarParser#assignExp.
    def enterAssignExp(self, ctx:Python3GrammarParser.AssignExpContext):
        pass

    # Exit a parse tree produced by Python3GrammarParser#assignExp.
    def exitAssignExp(self, ctx:Python3GrammarParser.AssignExpContext):
        pass


    # Enter a parse tree produced by Python3GrammarParser#conExp.
    def enterConExp(self, ctx:Python3GrammarParser.ConExpContext):
        pass

    # Exit a parse tree produced by Python3GrammarParser#conExp.
    def exitConExp(self, ctx:Python3GrammarParser.ConExpContext):
        pass


    # Enter a parse tree produced by Python3GrammarParser#ifExp.
    def enterIfExp(self, ctx:Python3GrammarParser.IfExpContext):
        pass

    # Exit a parse tree produced by Python3GrammarParser#ifExp.
    def exitIfExp(self, ctx:Python3GrammarParser.IfExpContext):
        pass


    # Enter a parse tree produced by Python3GrammarParser#elifExp.
    def enterElifExp(self, ctx:Python3GrammarParser.ElifExpContext):
        pass

    # Exit a parse tree produced by Python3GrammarParser#elifExp.
    def exitElifExp(self, ctx:Python3GrammarParser.ElifExpContext):
        pass


    # Enter a parse tree produced by Python3GrammarParser#elseExp.
    def enterElseExp(self, ctx:Python3GrammarParser.ElseExpContext):
        pass

    # Exit a parse tree produced by Python3GrammarParser#elseExp.
    def exitElseExp(self, ctx:Python3GrammarParser.ElseExpContext):
        pass


    # Enter a parse tree produced by Python3GrammarParser#ifStmt.
    def enterIfStmt(self, ctx:Python3GrammarParser.IfStmtContext):
        pass

    # Exit a parse tree produced by Python3GrammarParser#ifStmt.
    def exitIfStmt(self, ctx:Python3GrammarParser.IfStmtContext):
        pass


    # Enter a parse tree produced by Python3GrammarParser#whileExp.
    def enterWhileExp(self, ctx:Python3GrammarParser.WhileExpContext):
        pass

    # Exit a parse tree produced by Python3GrammarParser#whileExp.
    def exitWhileExp(self, ctx:Python3GrammarParser.WhileExpContext):
        pass


    # Enter a parse tree produced by Python3GrammarParser#forExp.
    def enterForExp(self, ctx:Python3GrammarParser.ForExpContext):
        pass

    # Exit a parse tree produced by Python3GrammarParser#forExp.
    def exitForExp(self, ctx:Python3GrammarParser.ForExpContext):
        pass


    # Enter a parse tree produced by Python3GrammarParser#loopExp.
    def enterLoopExp(self, ctx:Python3GrammarParser.LoopExpContext):
        pass

    # Exit a parse tree produced by Python3GrammarParser#loopExp.
    def exitLoopExp(self, ctx:Python3GrammarParser.LoopExpContext):
        pass


    # Enter a parse tree produced by Python3GrammarParser#loopStmt.
    def enterLoopStmt(self, ctx:Python3GrammarParser.LoopStmtContext):
        pass

    # Exit a parse tree produced by Python3GrammarParser#loopStmt.
    def exitLoopStmt(self, ctx:Python3GrammarParser.LoopStmtContext):
        pass


    # Enter a parse tree produced by Python3GrammarParser#exp.
    def enterExp(self, ctx:Python3GrammarParser.ExpContext):
        pass

    # Exit a parse tree produced by Python3GrammarParser#exp.
    def exitExp(self, ctx:Python3GrammarParser.ExpContext):
        pass


    # Enter a parse tree produced by Python3GrammarParser#program.
    def enterProgram(self, ctx:Python3GrammarParser.ProgramContext):
        pass

    # Exit a parse tree produced by Python3GrammarParser#program.
    def exitProgram(self, ctx:Python3GrammarParser.ProgramContext):
        pass


    # Enter a parse tree produced by Python3GrammarParser#block.
    def enterBlock(self, ctx:Python3GrammarParser.BlockContext):
        pass

    # Exit a parse tree produced by Python3GrammarParser#block.
    def exitBlock(self, ctx:Python3GrammarParser.BlockContext):
        pass



del Python3GrammarParser