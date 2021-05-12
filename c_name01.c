#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<ctype.h>

/* 전역 변수 선언*/
int charClass;
char lexeme[100]; // 입력한 nextChar 저장 LETTER / DIGIT / UNKNOWN 
char nextChar; // 입력값
int lexLen; // lex 길이
int Token[100]; // 입력한 nextToken 저장
int nextToken;
FILE* in_fp, * fopen();

/* 함수 선언 */
void addChar(); // 입력값 저장
void getChar(); // 저장한 입력값 분류
void getNonBlank();
int lex();

/* Character classes */
#define LETTER 0
#define DIGIT 1
#define UNKNOWN 99

/* Token codes */
#define INT_LIT 10
#define IDENT 11
#define ASSIGN_OP 20
#define ADD_OP 21
#define SUB_OP 22
#define MULT_OP 23
#define DIV_OP 24
#define LEFT_PAREN 25
#define RIGHT_PAREN 26
#define SEMICOLON 27 // ';'
#define ASSIGNMENT_OPERATOR 28 // '='
#define BIG 36 // '>'
#define SMALL 37 // '<'
#define LEFT_BRACKETS 39 // '{'
#define RIGHT_BRACKETS 40 // '}'

/* Reserved Token Codes */
/* 'while' 과 'do_while' 과 'switch' 와 'float' 이 case 'while': 과 같이 쓰일때
오류가 나서 제외 시킴. for문만 사용함. */

#define FOR_CODE 30
#define IF_CODE 31
#define ELSE_CODE 32
#define INT_CODE 35
#define CHAR_CODE 38

/******************************************************/
/* main driver */
int main(void) {
	/* Open the input data file and process its contents */
	if ((in_fp = fopen("front01.c", "r")) == NULL)
		printf("ERROR - cannot open front01.c \n");
	else {
		getChar();
		do {
			lex();
		} while (nextToken != EOF);
	}
	return 0;
}
/*****************************************************/
/* lookup - a function to lookup operators and parentheses
 and return the token */
int lookup(char ch) {
	switch (ch) {
		case '(':
			addChar();
			nextToken = LEFT_PAREN;
			break;
		case ')':
			addChar();
			nextToken = RIGHT_PAREN;
			break;
		case '+':
			addChar();
			nextToken = ADD_OP;
			break;
		case '-':
			addChar();
			nextToken = SUB_OP;
			break;
		case '*':
			addChar();
			nextToken = MULT_OP;
			break;
		case '/':
			addChar();
			nextToken = DIV_OP;
			break;
		case 'for':
			addChar();
			nextToken = FOR_CODE;
			break;
		case 'if':
			addChar();
			nextToken = IF_CODE;
			break;
		case 'else':
			addChar();
			nextToken = ELSE_CODE;
			break;
		case 'int':
			addChar();
			nextToken = INT_CODE;
			break;
		case 'char':
			addChar();
			nextToken = CHAR_CODE;
			break;
		case ';':
			addChar();
			nextToken = SEMICOLON;
			break;
		case '=':
			addChar();
			nextToken = ASSIGNMENT_OPERATOR;
			break;
		case '>':
			addChar();
			nextToken = BIG;
			break;
		case '<':
			addChar();
			nextToken = SMALL;
			break;
		case '{':
			addChar();
			nextToken = LEFT_BRACKETS;
			break;
		case '}':
			addChar();
			nextToken = RIGHT_BRACKETS;
			break;
		default:
			addChar();
			nextToken = EOF;
			break;
	}
	return nextToken;
}
/*****************************************************/
/* addChar - a function to add nextChar to lexeme */
void addChar() {
	if (lexLen <= 98) {
		lexeme[lexLen++] = nextChar;
		lexeme[lexLen] = 0;
	}
	else
		printf("Error - lexeme is too long \n");
}
/*****************************************************/
/* getChar - a function to get the next character of
 input and determine its character class */
void getChar() {
	int i = 0;
	if ((nextChar = getc(in_fp)) != EOF) {
		if (isalpha(nextChar))
			charClass = LETTER;
		else if (isdigit(nextChar))
			charClass = DIGIT;
		else charClass = UNKNOWN;
	}
	else
		charClass = EOF;
	i++;
}
/*****************************************************/
/* getNonBlank - a function to call getChar until it
 returns a non-whitespace character */
void getNonBlank() {
	while (isspace(nextChar))
		getChar();
}
/*****************************************************/
/* lex - a simple lexical analyzer for arithmetic
 expressions */
int lex() {
	lexLen = 0;
	getNonBlank();
	switch (charClass) {
		/* Parse identifiers */
	case LETTER:
		addChar();
		getChar();
		while (charClass == LETTER || charClass == DIGIT) {
			addChar();
			getChar();
		}
		nextToken = IDENT;
		break;
		/* Parse integer literals */
	case DIGIT:
		addChar();
		getChar();
		while (charClass == DIGIT) {
			addChar();
			getChar();
		}
		nextToken = INT_LIT;
		break;
		/* Parentheses and operators */
	case UNKNOWN:
		lookup(nextChar);
		getChar();
		break;
		/* EOF */
	case EOF:
		nextToken = EOF;
		lexeme[0] = 'E';
		lexeme[1] = 'O';
		lexeme[2] = 'F';
		lexeme[3] = 0;
		break;
	} /* End of switch */
	printf("Next token is: %d, Next lexeme is %s\n", nextToken, lexeme);
	return nextToken;
} /* End of function lex */

