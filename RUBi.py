#!/usr/bin/env python
# coding: utf-8

# In[21]:


from tkinter import *
from tkinter.ttk import *
import re

 
#initial popup window
window = Tk()
window.title("RUBi")
window.geometry('1300x800')

#welcome message
welcome = Label(window, text = "Hello, welcome to RUBi. Please fill out the following information:", font = ("Arial Bold", 20))
welcome.place(x=0, y = 0)

################################################     text box inputs     #####################################################################
#inputs user's desired temperature
tempInput = Label(window, text = "1. Please enter your desired temperature in Fahrenheit (50-85 Degrees)", font =("Veranda", 12))
tempInput.place(x = 0, y = 50)

desiredTemp = Entry(window, width = 15)
desiredTemp.place(x = 640, y = 53)

#validating proper input value
def get_temp():
    try:
        temp = int(desiredTemp.get())
        if temp > 49 and temp < 86:
            desiredTempUpdate = Label(window, text = "Value Accepted!")
            desiredTempUpdate.place(x=885, y=53)
        else:
            desiredTempUpdate = Label(window, text = "Please Enter Valid Integer")
            desiredTempUpdate.place(x=885, y=53)
    except:
        ValueError
        temp = 0
        desiredTempUpdate = Label(window, text = "Please Enter Valid Integer")
        desiredTempUpdate.place(x=885, y=53)

        
desiredTempButton = Button(window, text = "Verify", command = get_temp)
desiredTempButton.place(x = 770, y = 50)


#input for amount car must be charged during weekday
carWeekdayInput = Label(window, text = "2. Please enter what percentage your car must be charged on weekdays(0% - 100%)", font =("Veranda", 12))
carWeekdayInput.place(x = 0, y= 100)

carWeekday = Entry(window, width = 15)
carWeekday.place(x = 760, y = 103)

def get_CarWeekday():
    try:
        weekday = int(carWeekday.get())
        if weekday > -1 and weekday < 101:
            weekdayUpdate = Label(window, text = "Value Accepted!")
            weekdayUpdate.place(x=1010, y=103)
        else:
            weekdayUpdate = Label(window, text = "Please Enter Valid Integer")
            weekdayUpdate.place(x=1010, y=103)
    except:
        ValueError
        weekday = -2
        weekdayUpdate = Label(window, text = "Please Enter Valid Integer")
        weekdayUpdate.place(x=1010, y=103)
        
desiredWeekdayButton = Button(window, text = "Verify", command = get_CarWeekday)
desiredWeekdayButton.place(x = 890, y = 100)


#input for amount car must be charged during weekend
carWeekendInput = Label(window, text = "3. Please enter what percentage your car must be charged on weekends (0% - 100%)", font =("Veranda", 12))
carWeekendInput.place(x = 0, y= 150)

carWeekend = Entry(window, width = 15)
carWeekend.place(x = 765, y = 153)

def get_CarWeekend():
    try:
        weekend = int(carWeekend.get())
        if weekend > -1 and weekend < 101:
            weekendUpdate = Label(window, text = "Value Accepted!")
            weekendUpdate.place(x=1010, y=153)
        else:
            weekendUpdate = Label(window, text = "Please Enter Valid Integer")
            weekendUpdate.place(x=1010, y=153)
    except:
        ValueError
        weekend = -2
        weekendUpdate = Label(window, text = "Please Enter Valid Integer")
        weekendUpdate.place(x=1010, y=153)
        
desiredWeekendButton = Button(window, text = "Verify", command = get_CarWeekend)
desiredWeekendButton.place(x = 895, y = 150) 

#input for size of the house
houseSizeInput = Label(window, text = "4. Please enter the square footage of your home (1-20000 square feet)", font =("Veranda", 12))
houseSizeInput.place(x = 0, y = 200)

houseSize = Entry(window, width = 15)
houseSize.place(x = 640,y = 203)

def get_houseSize():
    try:
        size = int(houseSize.get())
        if size > -1 and size < 20001:
            sizeUpdate = Label(window, text = "Value Accepted!")
            sizeUpdate.place(x=890, y=203)
        else:
            sizeUpdate = Label(window, text = "Please Enter Valid Integer")
            sizeUpdate.place(x=890, y=203)
    except:
        ValueError
        size = -2
        sizeUpdate = Label(window, text = "Please Enter Valid Integer")
        sizeUpdate.place(x=890, y=203)

houseSizeButton = Button(window, text = "Verify", command = get_houseSize)
houseSizeButton.place(x = 770, y = 200)

###################################################    combobox inputs      #########################################################################
#input for number of solar panels
panelsNumberInput = Label(window, text = "5. Please choose the number of solar panels you have installed:", font =("Veranda", 12))
panelsNumberInput.place(x = 0, y = 250)

panelsNumber = Combobox(window, width = 9)
panelsNumber.place(x = 570, y = 253)
panelsNumber['values'] = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20")

#number of lights in the house
numberLightsInput = Label(window, text = "6. Please choose the number of lights in your home: ", font = ("Veranda", 12))
numberLightsInput.place(x = 0, y = 300)

numberLights = Combobox(window, width = 9)
numberLights.place(x = 463, y = 303)
numberLights['values'] = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63", "64", "65", "66", "67", "68", "69", "70", "71", "72", "73", "74", "75", "76", "77", "78", "79", "80", "81", "82", "83", "84", "85", "86", "87", "88", "89", "90", "91", "92", "93", "94", "95", "96", "97", "98", "99", "100")

#when user is home during weekdays
homeWeekdayInput = Label(window, text = "7. Please choose the times you are home during weekdays:", font=("Veranda", 12))
homeWeekdayInput.place(x = 0, y = 350)
homeWeekdayInput1 = Label(window, text = "to", font = ("Veranda", 12))
homeWeekdayInput1.place(x = 640, y = 350)

homeWeekday1 = Combobox(window, width = 9)
homeWeekday1.place(x = 535, y = 351)
homeWeekday1['values'] = ("12:00 am", "1:00 am", "2:00 am", "3:00 am", "4:00 am", "5:00 am", "6:00 am", "7:00 am", "8:00 am", "9:00 am", "10:00 am", "11:00 am", "12:00 pm", "1:00 pm", "2:00 pm", "3:00 pm", "4:00 pm", "5:00 pm", "6:00 pm","7:00 pm", "8:00 pm","9:00 pm","10:00 pm","11:00 pm")

homeWeekday2 = Combobox(window, width = 9)
homeWeekday2.place(x = 665, y = 351)
homeWeekday2['values'] = ("12:00 am", "1:00 am", "2:00 am", "3:00 am", "4:00 am", "5:00 am", "6:00 am", "7:00 am", "8:00 am", "9:00 am", "10:00 am", "11:00 am", "12:00 pm", "1:00 pm", "2:00 pm", "3:00 pm", "4:00 pm", "5:00 pm", "6:00 pm","7:00 pm", "8:00 pm","9:00 pm","10:00 pm","11:00 pm")


#when user is home during weekends
homeWeekendInput = Label(window, text = "8. Please choose the times you are home during weekends:", font=("Veranda", 12))
homeWeekendInput.place(x = 0, y = 400)
homeWeekendInput1 = Label(window, text = "to", font = ("Veranda", 12))
homeWeekendInput1.place(x = 640, y = 400)

homeWeekend1 = Combobox(window, width = 9)
homeWeekend1.place(x = 535, y = 401)
homeWeekend1['values'] = ("12:00 am", "1:00 am", "2:00 am", "3:00 am", "4:00 am", "5:00 am", "6:00 am", "7:00 am", "8:00 am", "9:00 am", "10:00 am", "11:00 am", "12:00 pm", "1:00 pm", "2:00 pm", "3:00 pm", "4:00 pm", "5:00 pm", "6:00 pm","7:00 pm", "8:00 pm","9:00 pm","10:00 pm","11:00 pm")

homeWeekend2 = Combobox(window, width = 9)
homeWeekend2.place(x = 665, y = 401)
homeWeekend2['values'] = ("12:00 am", "1:00 am", "2:00 am", "3:00 am", "4:00 am", "5:00 am", "6:00 am", "7:00 am", "8:00 am", "9:00 am", "10:00 am", "11:00 am", "12:00 pm", "1:00 pm", "2:00 pm", "3:00 pm", "4:00 pm", "5:00 pm", "6:00 pm","7:00 pm", "8:00 pm","9:00 pm","10:00 pm","11:00 pm")


#when user goes to sleep during weekdays
sleepWeekdayInput = Label(window, text = "9. Please choose the hours you sleep during weekdays: ", font = ("Veranda", 12))
sleepWeekdayInput.place(x = 0, y =450)
sleepWeekdayInput1 = Label(window, text = "to", font = ("Veranda", 12))
sleepWeekdayInput1.place(x = 610, y = 450 )

sleepWeekday1 = Combobox(window, width = 9)
sleepWeekday1.place(x = 505, y = 451)
sleepWeekday1['values'] = ("12:00 am", "1:00 am", "2:00 am", "3:00 am", "4:00 am", "5:00 am", "6:00 am", "7:00 am", "8:00 am", "9:00 am", "10:00 am", "11:00 am", "12:00 pm", "1:00 pm", "2:00 pm", "3:00 pm", "4:00 pm", "5:00 pm", "6:00 pm","7:00 pm", "8:00 pm","9:00 pm","10:00 pm","11:00 pm")

sleepWeekday2 = Combobox(window, width = 9)
sleepWeekday2.place(x = 640, y = 451)
sleepWeekday2['values'] = ("12:00 am", "1:00 am", "2:00 am", "3:00 am", "4:00 am", "5:00 am", "6:00 am", "7:00 am", "8:00 am", "9:00 am", "10:00 am", "11:00 am", "12:00 pm", "1:00 pm", "2:00 pm", "3:00 pm", "4:00 pm", "5:00 pm", "6:00 pm","7:00 pm", "8:00 pm","9:00 pm","10:00 pm","11:00 pm")


#when user goes to sleep during weekends
sleepWeekendInput = Label(window, text = "10. Please choose the hours you sleep during weekends: ", font = ("Veranda", 12))
sleepWeekendInput.place(x = 0, y =500)
sleepWeekendInput1 = Label(window, text = "to", font = ("Veranda", 12))
sleepWeekendInput1.place(x = 610, y = 500 )

sleepWeekend1 = Combobox(window, width = 9)
sleepWeekend1.place(x = 505, y = 501)
sleepWeekend1['values'] = ("12:00 am", "1:00 am", "2:00 am", "3:00 am", "4:00 am", "5:00 am", "6:00 am", "7:00 am", "8:00 am", "9:00 am", "10:00 am", "11:00 am", "12:00 pm", "1:00 pm", "2:00 pm", "3:00 pm", "4:00 pm", "5:00 pm", "6:00 pm","7:00 pm", "8:00 pm","9:00 pm","10:00 pm","11:00 pm")

sleepWeekend2 = Combobox(window, width = 9)
sleepWeekend2.place(x = 640, y = 501)
sleepWeekend2['values'] = ("12:00 am", "1:00 am", "2:00 am", "3:00 am", "4:00 am", "5:00 am", "6:00 am", "7:00 am", "8:00 am", "9:00 am", "10:00 am", "11:00 am", "12:00 pm", "1:00 pm", "2:00 pm", "3:00 pm", "4:00 pm", "5:00 pm", "6:00 pm","7:00 pm", "8:00 pm","9:00 pm","10:00 pm","11:00 pm")

#sleep while asleep
#inputs user's desired temperature
tempInputSleep = Label(window, text = "11. Please enter your desired temperature while sleeping in Fahrenheit (50-85 Degrees)", font =("Veranda", 12))
tempInputSleep.place(x = 0, y = 550)

desiredTempSleep = Entry(window, width = 15)
desiredTempSleep.place(x = 780, y = 553)

#validating proper input value
def get_tempSleep():
    try:
        temp = int(desiredTempSleep.get())
        if temp > 49 and temp < 86:
            desiredTempSleepUpdate = Label(window, text = "Value Accepted!")
            desiredTempSleepUpdate.place(x=1030, y=553)
        else:
            desiredTempSleepUpdate = Label(window, text = "Please Enter Valid Integer")
            desiredTempSleepUpdate.place(x=1030, y=553)
    except:
        ValueError
        temp = 0
        desiredTempSleepUpdate = Label(window, text = "Please Enter Valid Integer")
        desiredTempSleepUpdate.place(x=1030, y=553)

        
desiredTempSleepButton = Button(window, text = "Verify", command = get_tempSleep)
desiredTempSleepButton.place(x = 915, y = 550)


#current season
#currentSeasonInput = Label(window, text = "11. Which season is it currently")

#can add later for complexity

################################################   pop up window with outputs   ###################################################################
#solar power generated


#Appliance Power Usage per hour


#comparison of optimized versus unoptomized utility bill


####################################################   user overrides   #####################################################################################
#charge car manually


#turn off thermostat control


window.mainloop()


# In[ ]:





# In[ ]:




