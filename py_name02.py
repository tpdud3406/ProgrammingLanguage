#!/usr/bin/python3
from nltk.tokenize import word_tokenize

# Character classes
LETTER = 0
DIGIT = 1
UNKNOWN = 99
EOF = -1

# Token Codes
INT_LIT = 10 # 숫자
IDENT = 11 #sum
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
VARIABLE = 31 # 변수
IN = 32 # for 문에 사용
COLON = 33 # for 문에 사용

# Reserved Token Codes
FOR_CODE = 30
IF_CODE = 31
ELSE_CODE = 32
ELIF_CODE = 33
WHILE_CODE = 34
PRINT_CODE = 35
RANGE_CODE = 36

#############################################################
''' 리스트에 해당 토큰에 해당하는 값과 문자를 보여줘야 함'''

'''
# 해당 문자가 LETTER 인지 DIGIT 인지 UNKOWN인지 파악!
def getChar(x):
        nextChar = x
        if nextChar != None:
            if str(nextChar).isalpha() == True:
                charClass = LETTER
            elif str(nextChar).isdigit() == True:
                charClass = DIGIT
            else:
                charClass = UNKNOWN
        else: 
            charClass = EOF 
        return charClass
'''

# 연산자 lexeme 리스트에 추가!
def lex(ch):
    if ch == '(':
        return LEFT_PAREN
    elif ch == ')':
        return RIGHT_PAREN
    elif ch == '+':
        return ADD_OP
    elif ch == '-':
        return SUB_OP
    elif ch == '*':
        return MULT_OP
    elif ch == '/':
        return DIV_OP
    elif ch == 'for':
        return FOR_CODE
    elif ch == 'if':
        return IF_CODE
    elif ch == 'else':
        return ELSE_CODE
    elif ch == 'elif':
        return ELIF_CODE
    elif ch == 'print':
        return PRINT_CODE
    elif ch == 'range':
        return RANGE_CODE
    elif ch == ';':
        return SEMICOLON
    elif ch == '=':
        return ASSIGNMENT_OPERATOR
    elif ch == '>':
        return BIG
    elif ch == '<':
        return SMALL
    elif ch == 'x':
        return VARIABLE
    elif ch == 'in':
        return IN
    elif ch == ':':
        return COLON
    elif ch == 'sum':
        return IDENT
    else :
        return INT_LIT
####################################################
''' main 함수 '''
def main():
    # Open the input data file and process its list contents #
    in_fp = [x for x in open('front02.py')]
    in_fp = in_fp[0]
    in_fp = word_tokenize(in_fp)
    
    lexeme = []

    if in_fp == None:
        print("ERROR - cannot open front02.py")
    else :
        for x in in_fp:
            lexeme.append(lex(x))
        for x,y in zip(lexeme,in_fp):
            print("Next token is: " + str(x) + ", Next lexeme is " + str(y))    

    print("Next token is: -1, Next lexeme is EOF")

main()
