/* A Bison parser, made by GNU Bison 3.0.2.  */

/* Bison interface for Yacc-like parsers in C

   Copyright (C) 1984, 1989-1990, 2000-2013 Free Software Foundation, Inc.

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

#ifndef YY_BCP11_PARSER11_TAB_H_INCLUDED
# define YY_BCP11_PARSER11_TAB_H_INCLUDED
/* Debug traces.  */
#ifndef YYDEBUG
# define YYDEBUG 0
#endif
#if YYDEBUG
extern int bcp11_debug;
#endif

/* Token type.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
  enum yytokentype
  {
    LPAREN = 258,
    RPAREN = 259,
    LBRACKET = 260,
    RBRACKET = 261,
    SEMICOLON = 262,
    COMMA = 263,
    DEF = 264,
    ASSIGN = 265,
    EQUIVf = 266,
    IMPLYf = 267,
    ORf = 268,
    ANDf = 269,
    ODDf = 270,
    EVENf = 271,
    NOTf = 272,
    ITEf = 273,
    IMPLY = 274,
    EQUIV = 275,
    OR = 276,
    ODD = 277,
    AND = 278,
    NOT = 279,
    ID = 280,
    TRUE = 281,
    FALSE = 282,
    NUM = 283
  };
#endif

/* Value type.  */
#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef union YYSTYPE YYSTYPE;
union YYSTYPE
{
#line 37 "parser11.y" /* yacc.c:1909  */

  char *charptr;
  int intval;
  Gate *gate;
  std::list<Gate*>* list;

#line 90 "parser11.tab.h" /* yacc.c:1909  */
};
# define YYSTYPE_IS_TRIVIAL 1
# define YYSTYPE_IS_DECLARED 1
#endif


extern YYSTYPE bcp11_lval;

int bcp11_parse (void);

#endif /* !YY_BCP11_PARSER11_TAB_H_INCLUDED  */
