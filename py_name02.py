#!/usr/bin/python3
####################################################

# Character classes
LETTER = 0
DIGIT = 1
UNKNOWN = 99
'''
# Token Codes
INT_LIT = 10
IDENT = 11
ASSIGN_OP = 20
ADD_OP = 21
SUB_OP = 22
MULT_OP = 23
DIV_OP = 24
LEFT_PAREN = 25
RIGHT_PAREN = 26
SEMICOLON = 27 # ';'
ASSIGNMENT_OPERATOR = 28 # '='
BIG = 29 # '>'
SMALL = 30 # '<'
LEFT_BRACKETS = 31 # '{'
RIGHT_BRACKETS = 32 # '}'

# Reserved Token Codes
FOR_CODE = 30
IF_CODE = 31
ELSE_CODE = 32
ELIF_CODE = 34
WHILE_CODE = 33
'''
EOF = -1
# Token Codes
INT_LIT = 'int_lit'
IDENT = 'ident'
ASSIGN_OP = 'assign_op'
ADD_OP = '+'
SUB_OP = '-'
MULT_OP = '*'
DIV_OP = '/'
LEFT_PAREN = '('
RIGHT_PAREN = ')'
SEMICOLON = ';'
ASSIGNMENT_OPERATOR = '='
BIG = '>'
SMALL = '<'
LEFT_BRACKETS = '{'
RIGHT_BRACKETS = '}'

# Reserved Token Codes
FOR_CODE = 'for'
IF_CODE = 'if'
ELSE_CODE = 'else'
ELIF_CODE = 'elif'
WHILE_CODE = 'while'
PRINT_CODE = 'print'
RANGE_CODE = 'range'

####################################################

class Lexer:
    charClass = 0
    lexeme = [] # 입력한 nextChar 저장 LETTER / DIGIT / UNKNOWN 
    nextChar = '' # 입력값
    lexLen = 0 # lex 길이
    nextToken = ''
    i = 0
    def __init__(self, in_fp):
        self.in_fp = in_fp

    ''' lookup - a function to lookup operators and parentheses
    and return the token '''
    def lookup(self, ch):
        if ch == '(':
            self.addChar()
            Lexer.nextToken += LEFT_PAREN
        elif ch == ')':
            self.addChar()
            Lexer.nextToken += RIGHT_PAREN
        elif ch == '+':
            self.addChar()
            Lexer.nextToken += ADD_OP
        elif ch == '-':
            self.addChar()
            Lexer.nextToken += SUB_OP
        elif ch == '*':
            self.addChar()
            Lexer.nextToken += MULT_OP
        elif ch == '/':
            self.addChar()
            Lexer.nextToken += DIV_OP
        elif ch == 'for':
            self.addChar()
            Lexer.nextToken += FOR_CODE
        elif ch == 'if':
            self.addChar()
            Lexer.nextToken += IF_CODE
        elif ch == 'else':
            self.addChar()
            Lexer.nextToken += ELSE_CODE
        elif ch == 'elif':
            self.addChar()
            Lexer.nextToken += ELIF_CODE
        elif ch == 'print':
            self.addChar()
            Lexer.nextToken += PRINT_CODE
        elif ch == 'range':
            self.addChar()
            Lexer.nextToken += RANGE_CODE
        elif ch == ';':
            self.addChar()
            Lexer.nextToken += SEMICOLON
        elif ch == '=':
            self.addChar()
            Lexer.nextToken += ASSIGNMENT_OPERATOR
        elif ch == '>':
            self.addChar()
            Lexer.nextToken += BIG
        elif ch == '<':
            self.addChar()
            Lexer.nextToken += SMALL
        elif ch == '{':
            self.addChar()
            Lexer.nextToken += LEFT_BRACKETS
        elif ch == '}':
            self.addChar()
            Lexer.nextToken += RIGHT_BRACKETS
        else :
            self.addChar()
            Lexer.nextToken += EOF
        return Lexer.nextToken
        
    # addChar - a function to add nextChar to lexeme #
    def addChar(self):
        print(Lexer.lexLen)
        if Lexer.lexLen <= 98:
            print("add")
            #################### 여기서 자꾸 오류가 난다 !!!!!!!!!!!!!!
            Lexer.lexeme[Lexer.lexLen].join(Lexer.nextChar)
            print(Lexer.lexeme[Lexer.lexLen])
            Lexer.lexLen += 1
            print(Lexer.lexLen)
            Lexer.lexeme[Lexer.lexLen] += 0
        else :
            print("Error - lexeme is too long \n")

    #getChar - a function to get the next character of
    #input and determine its character class 
    def getChar(self):
        Lexer.nextChar = self.in_fp[0][self.i]
        if Lexer.nextChar != None:
            if ''.join(map(str,Lexer.nextChar)).isalpha() == True:
                print("i")
                Lexer.charClass = LETTER
            elif ''.join(map(str,Lexer.nextChar)).isdigit() == True:
                print("ii")
                Lexer.charClass = DIGIT
            else:
                print("iii")  
                Lexer.charClass = UNKNOWN
        else: Lexer.charClass = EOF
        self.i += 1
        print(self.i)

    ''' getNonBlank - a function to call getChar until it
    returns a non-whitespace character '''
    def getNonBlank(self):
        while ''.join(map(str,Lexer.nextChar)).isspace() == True:
            self.getChar()
    ''' lex - a simple lexical analyzer for arithmetic
    expressions '''
    def lex(self):
        Lexer.lexLen = 0
        self.getNonBlank()
        print(Lexer.charClass)
        if Lexer.charClass == LETTER:
            print("l")
            self.addChar()
            self.getChar()
            while Lexer.charClass == LETTER or Lexer.charClass == DIGIT :
                print("ll")
                self.addChar()
                self.getCHar()
            Lexer.nextToken = IDENT
        elif Lexer.charClass == DIGIT:
            self.addChar()
            print("lll")
            self.getChar()
            while Lexer.charClass == DIGIT:
                self.addChar()
                print("llll")
                self.getChar()
            Lexer.nextToken = INT_LIT
        elif Lexer.charClass == UNKNOWN:
            self.lookup(Lexer.nextChar)
            print("lllll")
            self.getChar()
        else :
            print("ok")
            Lexer.nextToken = EOF
            Lexer.lexeme[0].append('E')
            Lexer.lexeme[1].append('O')
            Lexer.lexeme[2].append('F')
            Lexer.lexeme[3].append(0)

        print("Next token is: "+ Lexer.nextToken + ", Next lexeme is " + Lexer.lexeme)
        return Lexer.nextToken
    
####################################################
''' main 함수 '''
def main():
    # Open the input data file and process its list contents #
    #in_fp = open('front02.py','r')
    in_fp = [x.split(' ') for x in open('front02.py')]
    #in_fp = str(list1)
    if in_fp == None:
        print("ERROR - cannot open front02.py")
    else :
        lexer = Lexer(in_fp)
        lexer.getChar()    
        print(lexer.nextToken)
        while lexer.nextToken != EOF:
            print("right")
            lexer.lex()  
            
        
main()