#!/usr/bin/env python
# coding: utf-8

# In[79]:


import pandas as pd


# In[80]:


df=pd.read_csv("C:/Users/user/Desktop/matlab_work/advent of code/aoc5.txt", delimiter='\n',names=['Seats'])
df.head()


# In[86]:


SeatID=[]

for ticket in range(len(df)):
    TotSeats=128
    seat_0=1
    seat_f=TotSeats
    TotCol=8
    Col_0=1
    Col_f=TotCol
    for i in range(7):
        if df.iloc[ticket]['Seats'][i]=='F':
            seat_f=seat_f-TotSeats/2
        else:
            seat_0=seat_0+TotSeats/2
        TotSeats=TotSeats/2
    for i in range(7,10):
        if df.iloc[ticket]['Seats'][i]=='L':
            Col_f=Col_f-TotCol/2
        else:
            Col_0=Col_0+TotCol/2
        TotCol=TotCol/2
    seat_f=seat_f-1
    Col_f=Col_f-1
    SeatID.append(seat_f*8+Col_f)


# In[87]:


max(SeatID)

