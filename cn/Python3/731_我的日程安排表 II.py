# @algorithm @lc id=731 lang=python3 
# @title my-calendar-ii
import heapq
from itertools import count
class MyCalendarTwo:

    def __init__(self):
        self.book_list=[]


    def book(self, start: int, end: int) -> bool:
        s=0
        e=1
        collion=0
        for  book in self.book_list:
            if book[s]<end<book[e]:
                collion+=1
            elif start<=book[s] and end>book[e]:
                collion+=1
            elif book[s]<=start<book[e]:
                collion+=1
            elif start>=book[s] and end<book[e]:
                collion+=1
            if collion>1:
                return False
        for i in range(len(self.book_list)):
            if start<=self.book_list[i][s]:
                self.book_list.insert(i,(start,end))
                return True
        self.book_list.append((start,end))
        return True
            
MyCalendar=MyCalendarTwo()
print(MyCalendar.book(10, 20))
print(MyCalendar.book(50, 60))
print(MyCalendar.book(10, 40))
print(MyCalendar.book(5, 15) )
print(MyCalendar.book(5, 10) )
print(MyCalendar.book(25, 55))