# @algorithm @lc id=1000027 lang=python3 
# @title calculator-lcci

import re
from time import sleep
from typing import List, Optional
from cn.Python3.mod.preImport import *
# @test("3+2*2")=7
# @test(" 3/2 ")=1
# @test(" 3+5 / 2 ")=5
# @test("1+1+1")=3
tp=0
val=1
class Solution:
    def scan(self,s):
        l=[]
        start=0
        current = 0
        TYPE=""
        while current< len(s):
            start=current
            if '0'<=s[current]<='9':
                TYPE="NUMBER"
                while current < len(s) and '0'<=s[current]<='9':
                    current+=1
            elif s[current] == '+':
                TYPE="PLUS"
                current+=1
            elif s[current] == '-':
                TYPE="MINUS"
                current+=1
            elif s[current] == '*':
                TYPE="STAR"
                current+=1
            elif s[current] == '/':
                TYPE="SLASH"
                current+=1
            elif s[current] == ' ':
                current+=1
                continue
            l.append((TYPE,s[start:current]))
        
        self.tokens=l
    def primary(self):
        if self.current>=len(self.tokens):
            return 0
        if self.tokens[self.current][tp]=='NUMBER':
            self.current+=1
            return int(self.tokens[self.current-1][val])
        return 0
    def factor(self):
        expr=self.primary()
        if self.current>=len(self.tokens):
            return expr
        while self.current<len(self.tokens) and self.tokens[self.current][tp] in ("STAR","SLASH"):
            if self.tokens[self.current][tp]=="STAR":
                self.current+=1
                expr=expr * self.primary()
            elif self.tokens[self.current][tp]=="SLASH":
                self.current+=1
                expr=expr // self.primary()
        return expr
        

    def term(self):
        expr=self.factor()
        if self.current>=len(self.tokens):
            return expr
        while self.current<len(self.tokens) and self.tokens[self.current][tp] in ("PLUS","MINUS"):
            if self.tokens[self.current][tp] in ("PLUS"):
                self.current+=1
                expr= expr + self.factor()
            elif self.tokens[self.current][tp]=="MINUS":
                self.current+=1
                expr=expr - self.factor()
        return expr
        
    def expression(self):
        return self.term()

    def calculate(self, s: str) -> int:
        self.start=0
        self.current=0
        self.scan(s)
        return self.expression()
                


        