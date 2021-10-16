#!/usr/bin/env python
# coding: utf-8

# In[29]:


from pynotifier import Notification
import time
import datetime

# for 20 second delay......
def time_sleep():
    n=5
    time.sleep(n)
    x = datetime.datetime.now()
    print(x.strftime("%I:%M:%S"))
    
# First Word....    
def About():
    Notification(
        title='About',
        description='Hindi : के बारे में         Gujrati : વિશે',
        urgency='normal'
        ).send()

# Second word.....
def Add():
    Notification(
      title='Add',
      description='Hindi : जोड़ें ......... Gujrati : ઉમેરો',
      urgency='Critical'
        ).send()

# Third word.....
def Bitter():
    Notification(
      title='Bitter',
      description='Hindi : कड़वा ......... Gujrati : કડવું',
      urgency='normal'
        ).send()

# Fourth word
def Sweet():
    Notification(
      title='Sweet',
      description='Hindi : मिठा ......... Gujrati : મીઠી',
      urgency='normal'
        ).send()

# Fifth word.....
def Moist():
    Notification(
      title='Moist',
      description='Hindi : गीला ......... Gujrati : ભેજ',
      urgency='normal'
        ).send()

# Sixth word.....
def Bland():
    Notification(
      title='Bland',
      description='Hindi : नरम ......... Gujrati : કોમળ',
      urgency='normal'
        ).send() 

while(True):
    About()
    time_sleep()

    Add()
    time_sleep()

    Bitter()
    time_sleep()

    Sweet()
    time_sleep()

    Moist()
    time_sleep()

    Bland()
    time_sleep()

