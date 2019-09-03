# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 17:51:57 2018

@author: ASHUTOSH
"""

import turtle

a=turtle.Turtle()
a1=turtle.Turtle()

b=turtle.Screen()
b.setup(width=1366,height=748,startx=0,starty=0)
b.bgpic(r"C:\Users\ASHUTOSH\Desktop\game\bg1.gif") #add your own path
img1=r"C:\Users\ASHUTOSH\Desktop\game\car1.gif"
img2=r"C:\Users\ASHUTOSH\Desktop\game\car2.gif"

b.addshape(img1)
b.addshape(img2)

a.shape(img1)
a1.shape(img2)

a.penup()
a1.penup()

x=-600


#pos1=a.xcor()
#pos2=a1.xcor()



#    if (pos1==450):
#        a.write("WINNER!!!!")
#        break
#    elif (pos2==450):
#        a1.write("WINNER!!!")
#        break
#    #a.setposition(-x,0)
    #a1.setposition(-x,-200)


        
a.setposition(-600,-100)
def forward():
    a.forward(12)
    a.speed(5)
        

b.onkey(forward,"Right")    
b.listen()


#a.home()    




zz=a.xcor()  
a1.speed(5)
while(x<500) and (zz<400):
    zz=a.xcor()
    a1.setposition(x,-200)
    b.onkey(forward,"Right")    
    b.listen()
    x=x+1

        
#a.write("WINNER!!",font=("Arial",10,"bold"))

        
        
        
b.exitonclick()
turtle.done()