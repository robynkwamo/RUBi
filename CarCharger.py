#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Imports
import math
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt 
import numpy as geek
#Fake Inputs
isHome_week = [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 
               0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]

isSleeping_week = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]

#Power usage by the A/C (the optimized amount) expecting ~3000-5000 kwH
AcPower = [4,0,0,3,0,0,0,0,0,0,0,0,
           0,0,0,0,0,0,0,0,3,3,0,3] 

#%charged before starting
Charge_Percent = 50

#Miles needed
MilesNeeded = 60


#power cost per hour
Power_Cost = [0.092,0.092, 0.092, 0.096, 0.1, 0.128, 0.164, 0.164, 
              0.148, 0.14, 0.14, 0.128,0.12, 0.108, 0.104, 0.104, 
              0.104, 0.108, 0.124, 0.148, 0.128, 0.112, 0.104, 0.096]

sun_available = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0]

Panel_power = 0.370
numPanels = 3

total_solar_available = [(sun_available[0]*numPanels*Panel_power), (sun_available[1]*numPanels*Panel_power), 
                        (sun_available[2]*numPanels*Panel_power),  (sun_available[3]*numPanels*Panel_power), 
                        (sun_available[4]*numPanels*Panel_power),  (sun_available[5]*numPanels*Panel_power), 
                        (sun_available[6]*numPanels*Panel_power),  (sun_available[7]*numPanels*Panel_power),
                        (sun_available[8]*numPanels*Panel_power),  (sun_available[9]*numPanels*Panel_power),
                        (sun_available[10]*numPanels*Panel_power), (sun_available[11]*numPanels*Panel_power),
                        (sun_available[12]*numPanels*Panel_power), (sun_available[13]*numPanels*Panel_power),
                        (sun_available[14]*numPanels*Panel_power), (sun_available[15]*numPanels*Panel_power), 
                        (sun_available[16]*numPanels*Panel_power), (sun_available[17]*numPanels*Panel_power),
                        (sun_available[18]*numPanels*Panel_power), (sun_available[19]*numPanels*Panel_power),
                        (sun_available[20]*numPanels*Panel_power), (sun_available[21]*numPanels*Panel_power),
                        (sun_available[22]*numPanels*Panel_power), (sun_available[23]*numPanels*Panel_power)]

isLight_week = []
n = 0
while n <= 23:
    if (isHome_week[n] == 1) and (isSleeping_week[n] == 0):
        isLight_week.append(1)
    else:
        isLight_week.append(0)
    n=n+1
    
numLights = 20
onelight_power = .060

Waterheater_power_week = [0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 
                         0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0]

Fridge_power = [0, .100, 0, 0, .70, 0, 0, .150, .080, .080, 0, 0, .100, 
                0, .090, 0, 0, .150, .100, 0, 0, .080, 0, .075]

Light_power_week = [(numLights*isLight_week[0]*onelight_power), (numLights*isLight_week[1]*onelight_power),
                    (numLights*isLight_week[2]*onelight_power), (numLights*isLight_week[3]*onelight_power),
                    (numLights*isLight_week[4]*onelight_power), (numLights*isLight_week[5]*onelight_power), 
                    (numLights*isLight_week[6]*onelight_power), (numLights*isLight_week[7]*onelight_power),
                    (numLights*isLight_week[8]*onelight_power), (numLights*isLight_week[9]*onelight_power), 
                    (numLights*isLight_week[10]*onelight_power), (numLights*isLight_week[11]*onelight_power),
                    (numLights*isLight_week[12]*onelight_power), (numLights*isLight_week[13]*onelight_power),
                    (numLights*isLight_week[14]*onelight_power), (numLights*isLight_week[15]*onelight_power), 
                    (numLights*isLight_week[16]*onelight_power), (numLights*isLight_week[17]*onelight_power),
                    (numLights*isLight_week[18]*onelight_power), (numLights*isLight_week[19]*onelight_power),
                    (numLights*isLight_week[20]*onelight_power), (numLights*isLight_week[21]*onelight_power), 
                    (numLights*isLight_week[22]*onelight_power), (numLights*isLight_week[23]*onelight_power)]

total_static_power_used = [(Waterheater_power_week[0]+Fridge_power[0]+Light_power_week[0]), 
                                (Waterheater_power_week[1]+Fridge_power[1]+Light_power_week[1]), 
                                (Waterheater_power_week[2]+Fridge_power[2]+Light_power_week[2]), 
                                (Waterheater_power_week[3]+Fridge_power[3]+Light_power_week[3]), 
                                (Waterheater_power_week[4]+Fridge_power[4]+Light_power_week[4]), 
                                (Waterheater_power_week[5]+Fridge_power[5]+Light_power_week[5]),
                                (Waterheater_power_week[6]+Fridge_power[6]+Light_power_week[6]), 
                                (Waterheater_power_week[7]+Fridge_power[7]+Light_power_week[7]),
                                (Waterheater_power_week[8]+Fridge_power[8]+Light_power_week[8]),
                                (Waterheater_power_week[9]+Fridge_power[9]+Light_power_week[9]),
                                (Waterheater_power_week[10]+Fridge_power[10]+Light_power_week[10]),
                                (Waterheater_power_week[11]+Fridge_power[11]+Light_power_week[11]),
                                (Waterheater_power_week[12]+Fridge_power[12]+Light_power_week[12]),
                                (Waterheater_power_week[13]+Fridge_power[13]+Light_power_week[13]),
                                (Waterheater_power_week[14]+Fridge_power[14]+Light_power_week[14]),
                                (Waterheater_power_week[15]+Fridge_power[15]+Light_power_week[15]), 
                                (Waterheater_power_week[16]+Fridge_power[16]+Light_power_week[16]), 
                                (Waterheater_power_week[17]+Fridge_power[17]+Light_power_week[17]),
                                (Waterheater_power_week[18]+Fridge_power[18]+Light_power_week[18]),
                                (Waterheater_power_week[19]+Fridge_power[19]+Light_power_week[19]),
                                (Waterheater_power_week[20]+Fridge_power[20]+Light_power_week[20]),
                                (Waterheater_power_week[21]+Fridge_power[21]+Light_power_week[21]),
                                (Waterheater_power_week[22]+Fridge_power[22]+Light_power_week[22]),
                                (Waterheater_power_week[23]+Fridge_power[23]+Light_power_week[23])]


# In[2]:


#Local Input variables and preliminary Calcs

#get ACPower and static power while there is sun available
Power_WhileSun = [(AcPower[i]+total_static_power_used[i])*sun_available[i] for i in range(len(AcPower))]

#solar power avaiable for Car Charger Use
SolarAvailable = [Power_WhileSun[i]-total_solar_available[i] for i in range(len(AcPower))]
for x in range(len(SolarAvailable)):
    if SolarAvailable[x] < 0:
        SolarAvailable[x] = 0
    else:
        continue

#Available hours total
Hours_Available = 0
#use power or not list
UsePowerFlag = []
#Minimum cost periods for charging
Cost_Mins = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


#Total Range of car
TotalRange = 260
#charge rate
Charge_Rate = 0.125

#Percent Charge needed derived from miles needed
Charge_PercentNeeded = MilesNeeded/TotalRange
#Charge percent after (goal)
Charge_PercentAfter = Charge_Percent + Charge_PercentNeeded

#Time needed to charge in hours
Charge_TimeNeeded = Charge_PercentNeeded/Charge_Rate

#round up an hour
Charge_Periods = math.ceil(Charge_TimeNeeded)
#print(Charge_Periods)

#calculate How many total hours the device is available to ensure charging is possible
for x in range(len(isHome_week)):
    if isHome_week[x] == 1:
        Hours_Available = Hours_Available + 1
    else:
        continue

#ensure charging is possible
if Charge_Periods > Hours_Available:
    print('Error: Full charge is impossible with allocated time')


# In[3]:


#Decide whether to charge based on Power Cost, Solar Power available and Availabilty values for the hour
Cost_Periodcost = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Cost_Period = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Cost_Periodcost = [(Power_Cost[i]*(7.2-SolarAvailable[i]))*isHome_week[i] for i in range(len(Power_Cost))]
Cost_Period = [(Power_Cost[i]*(7.2-SolarAvailable[i]))*isHome_week[i] for i in range(len(Power_Cost))]
for x in range(len(Cost_Period)):
    if Cost_Period[x] == 0:
        Cost_Period[x] = 100
        round(Cost_Period[x], 4)
    else:
        Cost_Period[x] = round(Cost_Period[x], 4)
        continue
        

p = Charge_Periods
for x in range(p):
    Cost_Min_ind = Cost_Period.index(min(Cost_Period))
    Cost_Mins[Cost_Min_ind] = 1
    Cost_Min = min(Cost_Period)
    #print(Cost_Min)
    #print(Cost_Period)
    for x in range(len(Cost_Period)):
        if Cost_Period[x] == Cost_Min:
            Cost_Period[x] = 1000
        else:
            continue  
            
#print(Cost_Mins)
            
Start_afternoon = 1
#for x in range(23):
#    if Cost_Mins[x] == 1:
#        print("Please start program after 5PM ")
#        Start_afternoon = 1
#        break
#    else:
#        continue


# In[4]:


#charge
Charger_Power_Usage = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Charger_Power_Cost = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Charge_Percent_curve = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Charge_Percent_current = Charge_Percent
#Charge_Percent_curve[0] = (Charge_Percent)
Charge_PercentNeeded2 = Charge_PercentNeeded*100
#print(Charge_PercentNeeded2)

for x in range(len(Cost_Mins)):
    if Cost_Mins[x] == 1:
        Charger_Power_Usage[x] = Charger_Power_Usage[x] + 7.2
        Charger_Power_Cost[x] = Cost_Periodcost[x]
#        Charge_Percent_current = Charge_Percent_current + 12.5
        #Charge_Percent_curve[x] = Charge_Percent_current
#    if x == 15:
#        Charge_Percent_current = Charge_Percent_current - Charge_PercentNeeded2
        #Charge_Percent_curve[x] = Charge_Percent_current
    else:
        continue
        
print(Charger_Power_Cost)        
#deal with %Charged        
Cost_Mins_Afternoon = Cost_Mins.copy()
#print(Cost_Mins_Afternoon)
if Start_afternoon == 1:
    Charge_Percent_curve[16] = Charge_Percent
    for x in range(8):
        #print(x)
        if Cost_Mins_Afternoon[x+16] == 1:
            Charge_Percent_curve[x+16] = Charge_Percent + 12.5
            Charge_Percent_current_afternoon = Charge_Percent + 12.5
            Cost_Mins_Afternoon[x+16] = 0
            #print(Charge_Percent_curve)
            break
        else:
            continue
    for x in range(8):
        if Cost_Mins_Afternoon[16+x] == 1:
            Charge_Percent_curve[16+x] = Charge_Percent_current_afternoon + 12.5
            Charge_Percent_current_afternoon = Charge_Percent_current_afternoon + 12.5
            Cost_Mins_Afternoon[16+x] = 0
            break
        else:
            continue
    for x in range(8):
        if Cost_Mins_Afternoon[16+x] == 1:
            Charge_Percent_curve[16+x] = Charge_Percent_current_afternoon + 12.5
            Charge_Percent_current_afternoon = Charge_Percent_current_afternoon + 12.5
            Cost_Mins_Afternoon[16+x] = 0
            break
        else:
            continue
    for x in range(8):
       # print(x)
        if Cost_Mins_Afternoon[x+16] == 1:
            Charge_Percent_curve[x+16] = Charge_Percent_current_afternoon + 12.5
            Charge_Percent_current_afternoon = Charge_Percent_current_afternoon + 12.5
            Cost_Mins_Afternoon[x+16] = 0
            #print(Charge_Percent_curve)
            break
        else:
            continue
    for x in range(8):
        if Cost_Mins_Afternoon[16+x] == 1:
            Charge_Percent_curve[16+x] = Charge_Percent_current_afternoon + 12.5
            Charge_Percent_current_afternoon = Charge_Percent_current_afternoon + 12.5
            Cost_Mins_Afternoon[16+x] = 0
            break
        else:
            continue
    for x in range(8):
        #print(x)
        if Cost_Mins_Afternoon[16+x] == 1:
            Charge_Percent_curve[16+x] = Charge_Percent_current_afternoon + 12.5
            Charge_Percent_current_afternoon = Charge_Percent_current_afternoon + 12.5
            Cost_Mins_Afternoon[16+x] = 0
            break
        else:
            continue
    for x in range(8):
        #print(x)
        if Cost_Mins_Afternoon[x+16] == 1:
            Charge_Percent_curve[x+16] = Charge_Percent_current_afternoon + 12.5
            Charge_Percent_current_afternoon = Charge_Percent_current_afternoon + 12.5
            Cost_Mins_Afternoon[x+16] = 0
            #print(Charge_Percent_curve)
            break
        else:
            continue
    for x in range(16):
        if Cost_Mins_Afternoon[x] == 1:
            Charge_Percent_curve[x] = Charge_Percent_current_afternoon + 12.5
            Charge_Percent_current_afternoon = Charge_Percent_current_afternoon + 12.5
            Cost_Mins_Afternoon[x] = 0
            #print(Charge_Percent_curve)
            break
        else:
            continue
    for x in range(16):
        if Cost_Mins_Afternoon[x] == 1:
            Charge_Percent_curve[x] = Charge_Percent_current_afternoon + 12.5
            Charge_Percent_current_afternoon = Charge_Percent_current_afternoon + 12.5
            Cost_Mins_Afternoon[x] = 0
            break
        else:
            continue
    for x in range(16):
        if Cost_Mins_Afternoon[x] == 1:
            Charge_Percent_curve[x] = Charge_Percent_current_afternoon + 12.5
            Charge_Percent_current_afternoon = Charge_Percent_current_afternoon + 12.5
            Cost_Mins_Afternoon[x] = 0
            break
        else:
            continue
    for x in range(16):
        if Cost_Mins_Afternoon[x] == 1:
            Charge_Percent_curve[x] = Charge_Percent_current_afternoon + 12.5
            Charge_Percent_current_afternoon = Charge_Percent_current_afternoon + 12.5
            Cost_Mins_Afternoon[x] = 0
            break
        else:
            continue
    for x in range(16):
        #print(x)
        if Cost_Mins_Afternoon[x] == 1:
            Charge_Percent_curve[x] = Charge_Percent_current_afternoon + 12.5
            Charge_Percent_current_afternoon = Charge_Percent_current_afternoon + 12.5
            Cost_Mins_Afternoon[x] = 0
            break
        else:
            continue
    for x in range(16):
        if Cost_Mins_Afternoon[x] == 1:
            Charge_Percent_curve[x] = Charge_Percent_current_afternoon + 12.5
            Charge_Percent_current_afternoon = Charge_Percent_current_afternoon + 12.5
            Cost_Mins_Afternoon[x] = 0
           # print(Charge_Percent_curve)
            break
        else:
            continue
    for x in range(16):
        if Cost_Mins_Afternoon[x] == 1:
            Charge_Percent_curve[x] = Charge_Percent_current_afternoon + 12.5
            Charge_Percent_current_afternoon = Charge_Percent_current_afternoon + 12.5
            Cost_Mins_Afternoon[x] = 0
            break
        else:
            continue
    for x in range(16):
        if Cost_Mins_Afternoon[x] == 1:
            Charge_Percent_curve[x] = Charge_Percent_current_afternoon + 12.5
            Charge_Percent_current_afternoon = Charge_Percent_current_afternoon + 12.5
            Cost_Mins_Afternoon[x] = 0
            break
        else:
            continue
    for x in range(16):
        if Cost_Mins_Afternoon[x] == 1:
            Charge_Percent_curve[x] = Charge_Percent_current_afternoon + 12.5
            Charge_Percent_current_afternoon = Charge_Percent_current_afternoon + 12.5
            Cost_Mins_Afternoon[x] = 0
            break
        else:
            continue
    for x in range(16):
        #print(x)
        if Cost_Mins_Afternoon[x] == 1:
            Charge_Percent_curve[x] = Charge_Percent_current_afternoon + 12.5
            Charge_Percent_current_afternoon = Charge_Percent_current_afternoon + 12.5
            Cost_Mins_Afternoon[x] = 0
            break
        else:
            continue
    for x in range(16):
        if Cost_Mins_Afternoon[x] == 1:
            Charge_Percent_curve[x] = Charge_Percent_current_afternoon + 12.5
            Charge_Percent_current_afternoon = Charge_Percent_current_afternoon + 12.5
            Cost_Mins_Afternoon[x] = 0
            #print(Charge_Percent_curve)
            break
        else:
            continue
    for x in range(16):
        if Cost_Mins_Afternoon[x] == 1:
            Charge_Percent_curve[x] = Charge_Percent_current_afternoon + 12.5
            Charge_Percent_current_afternoon = Charge_Percent_current_afternoon + 12.5
            Cost_Mins_Afternoon[x] = 0
            break
        else:
            continue
    for x in range(16):
        if Cost_Mins_Afternoon[x] == 1:
            Charge_Percent_curve[x] = Charge_Percent_current_afternoon + 12.5
            Charge_Percent_current_afternoon = Charge_Percent_current_afternoon + 12.5
            Cost_Mins_Afternoon[x] = 0
            break
        else:
            continue
    for x in range(16):
        if Cost_Mins_Afternoon[x] == 1:
            Charge_Percent_curve[x] = Charge_Percent_current_afternoon + 12.5
            Charge_Percent_current_afternoon = Charge_Percent_current_afternoon + 12.5
            Cost_Mins_Afternoon[x] = 0
            break
        else:
            continue
    for x in range(16):
        #print(x)
        if Cost_Mins_Afternoon[x] == 1:
            Charge_Percent_curve[x] = Charge_Percent_current_afternoon + 12.5
            Charge_Percent_current_afternoon = Charge_Percent_current_afternoon + 12.5
            Cost_Mins_Afternoon[x] = 0
            break
        else:
            continue
            
            
#print(Charge_Percent)
#print(Charge_Percent_curve)

for x in range(len(isHome_week)):
    if isHome_week[x] == 0:
        Charge_Percent_curve[x] = Charge_Percent
    else:
        continue
#print(Charge_Percent_curve)
for x in range(24):
    if Charge_Percent_curve[x] == 0 and Charge_Percent_curve[x-1] != 0:
        Charge_Percent_curve[x] = Charge_Percent_curve[x-1]
    else:
        continue
for x in range(24):
    if Charge_Percent_curve[x] == 0 and Charge_Percent_curve[23] != 0:
        Charge_Percent_curve[x] = Charge_Percent_curve[23]
    else:
        continue

#print(Charge_Percent_curve)     

#for x in range(len(Charge_Percent_curve)):
#    if Charge_Percent_curve[x] == 0:
#        Charge_Percent_curve[x] = Charge_Percent_curve[x-1]
#    else:
#        continue


# In[5]:


#Cost Comparison
Cost_Optimized_CarCharger = 0
Cost_Optimized_CarCharger = sum(Charger_Power_Cost)

Total_Power_Usage = [AcPower[i]+total_static_power_used[i] for i in range(len(AcPower))]
Total_Power_Costbefore = [Total_Power_Usage[i]*Power_Cost[i] for i in range (len(Total_Power_Usage))]
Total_Power_Cost = [Total_Power_Costbefore[i]+Charger_Power_Cost[i] for i in range (len(Total_Power_Usage))]

b = sum(Total_Power_Cost)

#Hours plugged in and not used in unoptimized variant
Hours_Unused_PluggedIn = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Hours_used_PluggedIn = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

Charge_Remaining = 100 - Charge_Percent
Charge_Time_Full = (Charge_Remaining/100)/Charge_Rate

Charge_Percent_Unoptimized = [Charge_Percent, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Charge_Percent_current_unopt = Charge_Remaining


for x in range(len(Charge_Percent_Unoptimized)):
    if Charge_Percent_Unoptimized[x] < 100:
        if x == 0:
            Charge_Percent_Unoptimized[x] = Charge_Percent_Unoptimized[x]
        else:
            Charge_Percent_Unoptimized[x] = Charge_Percent_current_unopt + 12.5
            Charge_Percent_current_unopt = Charge_Percent_current_unopt + 12.5
    if Charge_Percent_Unoptimized[x-1] > 100:
        Charge_Percent_Unoptimized[x-1] = 100
    if Charge_Percent_Unoptimized[x-1] == 100:
        Charge_Percent_Unoptimized[x] = 100
    else:
        continue

Unoptimized_TotalPower_Usedpluggedin = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Unoptimized_TotalPower_Unusedpluggedin = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Unoptimized_TotalCost = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 
Unoptimized_TotalPower_UsedpluggedinCost = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 
PowerCost_charger_Unoptimized_UnusedPluggedin = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 

iterator_unoptimized = round(Charge_Time_Full)
for x in range(iterator_unoptimized):
        if isHome_week[x+18] == 1:
            Hours_used_PluggedIn[x+18] = 1
        else:
            if isHome_week[x+19] == 1:
                Hours_used_PluggedIn[x+19] = 1
            else:
                if isHome_week[x+20] == 1:
                    Hours_used_PluggedIn[x+20] = 1
                else: 
                    if isHome_week[x+21] == 1:
                        Hours_used_PluggedIn[x+21] = 1
                    else:
                        if isHome_week[x+22] == 1:
                            Hours_used_PluggedIn[x+22] = 1
                        else:
                            if isHome_week[x+23] == 1:
                                Hours_used_PluggedIn[x+23] = 1
                            else:
                                if isHome_week[x+24] == 1:
                                    Hours_used_PluggedIn[x+24] = 1
                                else:
                                    continue
                                    

#print(Hours_used_PluggedIn)                                    
for x in range(len(Hours_Unused_PluggedIn)):
    if Hours_used_PluggedIn[x] == 1:
        Hours_Unused_PluggedIn[x] = 0
    elif isHome_week[x] == 1 and Hours_Unused_PluggedIn[x] == 0:
        Hours_Unused_PluggedIn[x] = 1
    else:
        continue
        
for x in range(17):
    Charge_Percent_Unoptimized.insert(0, Charge_Percent_Unoptimized.pop())
for x in range(17):
    if Charge_Percent_Unoptimized[x] == 100:
        Charge_Percent_Unoptimized[x] = Charge_Percent
    else:
        continue


#print(Hours_used_PluggedIn)
for x in range(24):
    if Hours_used_PluggedIn[x] == 1:
        Unoptimized_TotalPower_UsedpluggedinCost[x] = Cost_Periodcost[x]
    else:
        continue
#print(Unoptimized_TotalPower_UsedpluggedinCost)
Unoptimized_TotalPower_Usedpluggedin = [Hours_used_PluggedIn[i]*7.2 for i in range (len(Hours_Unused_PluggedIn))]


Unoptimized_TotalPower_Unusedpluggedin = [Hours_Unused_PluggedIn[i]*.03 for i in range (len(Hours_Unused_PluggedIn))]


Unoptimized_TotalPower = [Unoptimized_TotalPower_Usedpluggedin[i]+Unoptimized_TotalPower_Unusedpluggedin[i] for i in range (len(Unoptimized_TotalPower_Usedpluggedin))]

PowerCost_charger_Unoptimized_UnusedPluggedin = [Unoptimized_TotalPower_Unusedpluggedin[i]*Power_Cost[i] for i in range (len(Unoptimized_TotalPower))]
#print(PowerCost_charger_Unoptimized_UnusedPluggedin)
PowerCost_charger_Unoptimized = [Unoptimized_TotalPower_UsedpluggedinCost[i]+PowerCost_charger_Unoptimized_UnusedPluggedin[i] for i in range (len(Unoptimized_TotalPower))]
#print(PowerCost_charger_Unoptimized)
#print(PowerCost_charger_Unoptimized)
c = sum(PowerCost_charger_Unoptimized)

Total_Power_Usage_Unopt = [AcPower[i]+total_static_power_used[i]+Unoptimized_TotalPower[i] for i in range(len(AcPower))]

Total_Power_Cost_Unopt = [Total_Power_Usage_Unopt[i]*Power_Cost[i] for i in range(len(Total_Power_Usage_Unopt))]

a_Total_Power_Cost_Unopt = sum(Total_Power_Cost_Unopt)

x_Charger_Power_Usage = Charger_Power_Usage.copy()
y = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]


i = Unoptimized_TotalPower


# In[6]:


x_Charger_Power_Usage_integral = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 
i_integral = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

x_Charger_Power_Usage_integral = geek.cumsum(x_Charger_Power_Usage)  
#print(x_Charger_Power_Usage_weekend_integral)

i_integral = geek.cumsum(i)  
#print(i_consecutive_weekend_integral)


plt.plot(y, x_Charger_Power_Usage) 
plt.xlabel('Time of Day') 
plt.ylabel('Power Consumed (Kwh)') 
plt.title('Optimized Vs First Day Unoptimized Power Consumption ') 
orange_patch = mpatches.Patch(color='Orange', label='Unoptimized')
blue_patch = mpatches.Patch(color='Blue', label='Optimized')
plt.legend(handles=[blue_patch,orange_patch])
plt.plot(y, i) 
plt.show() 

plt.plot(y, x_Charger_Power_Usage_integral) 
plt.xlabel('Time of Day') 
plt.ylabel('Power Consumed (Kw)') 
plt.title('Total Optimized Vs First Day Unoptimized Power Consumption ') 
orange_patch = mpatches.Patch(color='Orange', label='Unoptimized')
blue_patch = mpatches.Patch(color='Blue', label='Optimized')
plt.legend(handles=[blue_patch,orange_patch])
plt.plot(y, i_integral) 
plt.show() 


plt.plot(y, Charge_Percent_curve)
plt.xlabel('Time of Day') 
plt.ylabel('% Charged') 
plt.title('First Day Optimized Vs Unoptimized charge Curve') 
orange_patch = mpatches.Patch(color='Orange', label='Unoptimized')
blue_patch = mpatches.Patch(color='Blue', label='Optimized')
plt.legend(handles=[blue_patch,orange_patch])
#plt.show() 

plt.plot(y, Charge_Percent_Unoptimized)
plt.xlabel('Time of Day') 
plt.ylabel('% Charged') 

plt.show() 


print('The Optimized weekday cost of the optimized car charger will be:$', round(Cost_Optimized_CarCharger,2))
print('The Unoptimized Initial weekday cost for the car charger is:$', round(c,2))
print('\n')


# In[7]:


#Consecutive days for unoptimized cost
Charge_Periods_consecutive = math.ceil(Charge_TimeNeeded)

#Hours plugged in and not used in unoptimized variant
Hours_Unused_PluggedIn_consecutive = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Hours_used_PluggedIn_consecutive = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

Charge_Percent_before_consecutive = 100 - Charge_PercentNeeded*100

#print(Charge_Percent_before_consecutive)
Charge_Percent_Unoptimized_consecutive = [Charge_Percent_before_consecutive, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Charge_Percent_current_unopt_consecutive = Charge_Percent_before_consecutive


for x in range(len(Charge_Percent_Unoptimized_consecutive)):
    if Charge_Percent_Unoptimized_consecutive[x] < 100:
        if x == 0:
            Charge_Percent_Unoptimized_consecutive[x] = Charge_Percent_Unoptimized_consecutive[x]
        else:
            Charge_Percent_Unoptimized_consecutive[x] = Charge_Percent_current_unopt_consecutive + 12.5
            Charge_Percent_current_unopt_consecutive = Charge_Percent_current_unopt_consecutive + 12.5
    if Charge_Percent_Unoptimized_consecutive[x-1] > 100:
        Charge_Percent_Unoptimized_consecutive[x-1] = 100
    if Charge_Percent_Unoptimized_consecutive[x-1] == 100:
        Charge_Percent_Unoptimized_consecutive[x] = 100
    else:
        continue
        

Unoptimized_TotalPower_Usedpluggedin_consecutive = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Unoptimized_TotalPower_Unusedpluggedin_consecutive = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Unoptimized_TotalCost_consecutive = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 
Unoptimized_TotalPower_UsedpluggedinCost_consecutive = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 
PowerCost_charger_Unoptimized_UnusedPluggedin_consecutive = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 

iterator_unoptimized_consecutive = round(Charge_Periods_consecutive)
for x in range(iterator_unoptimized_consecutive):
        if isHome_week[x+18] == 1:
            Hours_used_PluggedIn_consecutive[x+18] = 1
        else:
            if isHome_week[x+19] == 1:
                Hours_used_PluggedIn_consecutive[x+19] = 1
            else:
                if isHome_week[x+20] == 1:
                    Hours_used_PluggedIn_consecutive[x+20] = 1
                else: 
                    if isHome_week[x+21] == 1:
                        Hours_used_PluggedIn_consecutive[x+21] = 1
                    else:
                        if isHome_week[x+22] == 1:
                            Hours_used_PluggedIn_consecutive[x+22] = 1
                        else:
                            if isHome_week[x+23] == 1:
                                Hours_used_PluggedIn_consecutive[x+23] = 1
                            else:
                                if isHome_week[x+24] == 1:
                                    Hours_used_PluggedIn_consecutive[x+24] = 1
                                else:
                                    continue
                                    

#print(Hours_used_PluggedIn_consecutive)                                    
for x in range(len(Hours_Unused_PluggedIn_consecutive)):
    if Hours_used_PluggedIn_consecutive[x] == 1:
        Hours_Unused_PluggedIn_consecutive[x] = 0
    elif isHome_week[x] == 1 and Hours_Unused_PluggedIn_consecutive[x] == 0:
        Hours_Unused_PluggedIn_consecutive[x] = 1
    else:
        continue
        
for x in range(17):
    Charge_Percent_Unoptimized_consecutive.insert(0, Charge_Percent_Unoptimized_consecutive.pop())
for x in range(17):
    if Charge_Percent_Unoptimized_consecutive[x] == 100:
        Charge_Percent_Unoptimized_consecutive[x] = Charge_Percent_before_consecutive
    else:
        continue

for x in range(24):
    if Hours_used_PluggedIn_consecutive[x] == 1:
        Unoptimized_TotalPower_UsedpluggedinCost_consecutive[x] = Cost_Periodcost[x]
    else:
        continue

        
Unoptimized_TotalPower_Usedpluggedin_consecutive = [Hours_used_PluggedIn_consecutive[i]*7.2 for i in range (len(Hours_Unused_PluggedIn_consecutive))]


Unoptimized_TotalPower_Unusedpluggedin_consecutive = [Hours_Unused_PluggedIn_consecutive[i]*.030 for i in range (len(Hours_Unused_PluggedIn_consecutive))]


Unoptimized_TotalPower_consecutive = [Unoptimized_TotalPower_Usedpluggedin_consecutive[i]+Unoptimized_TotalPower_Unusedpluggedin_consecutive[i] for i in range (len(Unoptimized_TotalPower_Usedpluggedin_consecutive))]

PowerCost_charger_Unoptimized_UnusedPluggedin_consecutive = [Unoptimized_TotalPower_Unusedpluggedin[i]*Power_Cost[i] for i in range (len(Unoptimized_TotalPower))]
#print(PowerCost_charger_Unoptimized_UnusedPluggedin_consecutive)
PowerCost_charger_Unoptimized_consecutive = [Unoptimized_TotalPower_UsedpluggedinCost_consecutive[i]+PowerCost_charger_Unoptimized_UnusedPluggedin_consecutive[i] for i in range (len(Unoptimized_TotalPower_consecutive))]
#print(PowerCost_charger_Unoptimized_consecutive)
#print(PowerCost_charger_Unoptimized)
c_consecutive = sum(PowerCost_charger_Unoptimized_consecutive)        
        
        

Total_Power_Usage_Unopt_consecutive = [AcPower[i]+total_static_power_used[i]+Unoptimized_TotalPower_consecutive[i] for i in range(len(AcPower))]

Total_Power_Cost_Unopt_consecutive = [Total_Power_Usage_Unopt_consecutive[i]*Power_Cost[i] for i in range(len(Total_Power_Usage_Unopt_consecutive))]

a_consecutive = sum(Total_Power_Cost_Unopt_consecutive)

i_consecutive = Unoptimized_TotalPower_consecutive


# In[8]:


i_consecutive_integral = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

i_consecutive_integral = geek.cumsum(i_consecutive)  
#print(i_consecutive_integral)

plt.plot(y, x_Charger_Power_Usage) 
plt.plot(y, i_consecutive) 
plt.xlabel('Time of Day') 
plt.ylabel('Power Consumed (Kwh)') 
plt.title('Consecutive unoptimized Power Consumed') 

orange_patch = mpatches.Patch(color='Orange', label='Unoptimized')
blue_patch = mpatches.Patch(color='Blue', label='Optimized')
plt.legend(handles=[blue_patch,orange_patch])
plt.title('Optimized Vs Consecutive Unoptimized Power Consumption') 
plt.show() 

plt.plot(y, x_Charger_Power_Usage_integral) 
plt.plot(y, i_consecutive_integral) 
plt.xlabel('Time of Day') 
plt.ylabel('Power Consumed (Kw)') 
plt.title('Optimized Vs Consecutive Unoptimized Total Power Consumption') 
orange_patch = mpatches.Patch(color='Orange', label='Unoptimized')
blue_patch = mpatches.Patch(color='Blue', label='Optimized')
plt.legend(handles=[blue_patch,orange_patch])
plt.show() 

plt.plot(y, Charge_Percent_curve)
plt.plot(y, Charge_Percent_Unoptimized_consecutive)
plt.xlabel('Time of Day') 
plt.ylabel('% Charged') 
plt.title('Optimized Vs Consecutive Unoptimized charge Curve') 
orange_patch = mpatches.Patch(color='Orange', label='Unoptimized')
blue_patch = mpatches.Patch(color='Blue', label='Optimized')
plt.legend(handles=[blue_patch,orange_patch])
plt.show() 

print('The Unoptimized Consecutive Weekday cost for the car charger is:$', round(c_consecutive,2))
print('\n')


# In[9]:


isHome_weekend = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
               1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]

isSleeping_weekend = [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]

Power_Cost_weekend = [0.092, 0.092, 0.096, 0.096, 0.092, 0.096, 0.108, 0.108, 0.116, 0.112, 0.108, 0.104,
                      0.096, 0.092, 0.092, 0.092, 0.096, 0.1, 0.112, 0.128, 0.116, 0.104, 0.096, 0.092]

isLight_weekend = []
n = 0
while n <= 23:
    if (isHome_weekend[n] == 1) and (isSleeping_weekend[n] == 0):
        isLight_weekend.append(1)
    else:
        isLight_weekend.append(0)
    n=n+1

Waterheater_power_weekend = [0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 
                         0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0]

Light_power_weekend = [(numLights*isLight_weekend[0]*onelight_power), (numLights*isLight_weekend[1]*onelight_power),
                    (numLights*isLight_weekend[2]*onelight_power), (numLights*isLight_weekend[3]*onelight_power),
                    (numLights*isLight_weekend[4]*onelight_power), (numLights*isLight_weekend[5]*onelight_power), 
                    (numLights*isLight_weekend[6]*onelight_power), (numLights*isLight_weekend[7]*onelight_power),
                    (numLights*isLight_weekend[8]*onelight_power), (numLights*isLight_weekend[9]*onelight_power), 
                    (numLights*isLight_weekend[10]*onelight_power), (numLights*isLight_weekend[11]*onelight_power),
                    (numLights*isLight_weekend[12]*onelight_power), (numLights*isLight_weekend[13]*onelight_power),
                    (numLights*isLight_weekend[14]*onelight_power), (numLights*isLight_weekend[15]*onelight_power), 
                    (numLights*isLight_weekend[16]*onelight_power), (numLights*isLight_weekend[17]*onelight_power),
                    (numLights*isLight_weekend[18]*onelight_power), (numLights*isLight_weekend[19]*onelight_power),
                    (numLights*isLight_weekend[20]*onelight_power), (numLights*isLight_weekend[21]*onelight_power), 
                    (numLights*isLight_weekend[22]*onelight_power), (numLights*isLight_weekend[23]*onelight_power)]

total_static_power_used_weekend = [(Waterheater_power_weekend[0]+Fridge_power[0]+Light_power_weekend[0]), 
                                (Waterheater_power_weekend[1]+Fridge_power[1]+Light_power_weekend[1]), 
                                (Waterheater_power_weekend[2]+Fridge_power[2]+Light_power_weekend[2]), 
                                (Waterheater_power_weekend[3]+Fridge_power[3]+Light_power_weekend[3]), 
                                (Waterheater_power_weekend[4]+Fridge_power[4]+Light_power_weekend[4]), 
                                (Waterheater_power_weekend[5]+Fridge_power[5]+Light_power_weekend[5]),
                                (Waterheater_power_weekend[6]+Fridge_power[6]+Light_power_weekend[6]), 
                                (Waterheater_power_weekend[7]+Fridge_power[7]+Light_power_weekend[7]),
                                (Waterheater_power_weekend[8]+Fridge_power[8]+Light_power_weekend[8]),
                                (Waterheater_power_weekend[9]+Fridge_power[9]+Light_power_weekend[9]),
                                (Waterheater_power_weekend[10]+Fridge_power[10]+Light_power_weekend[10]),
                                (Waterheater_power_weekend[11]+Fridge_power[11]+Light_power_weekend[11]),
                                (Waterheater_power_weekend[12]+Fridge_power[12]+Light_power_weekend[12]),
                                (Waterheater_power_weekend[13]+Fridge_power[13]+Light_power_weekend[13]),
                                (Waterheater_power_weekend[14]+Fridge_power[14]+Light_power_weekend[14]),
                                (Waterheater_power_weekend[15]+Fridge_power[15]+Light_power_weekend[15]), 
                                (Waterheater_power_weekend[16]+Fridge_power[16]+Light_power_weekend[16]), 
                                (Waterheater_power_weekend[17]+Fridge_power[17]+Light_power_weekend[17]),
                                (Waterheater_power_weekend[18]+Fridge_power[18]+Light_power_weekend[18]),
                                (Waterheater_power_weekend[19]+Fridge_power[19]+Light_power_weekend[19]),
                                (Waterheater_power_weekend[20]+Fridge_power[20]+Light_power_weekend[20]),
                                (Waterheater_power_weekend[21]+Fridge_power[21]+Light_power_weekend[21]),
                                (Waterheater_power_weekend[22]+Fridge_power[22]+Light_power_weekend[22]),
                                (Waterheater_power_weekend[23]+Fridge_power[23]+Light_power_weekend[23])]

#%charged before starting
Charge_Percent_weekend = 50

#Miles needed
MilesNeeded_weekend = 20


# In[10]:


#Local Input variables and preliminary Calcs

#get ACPower and static power while there is sun available
Power_WhileSun_weekend = [(AcPower[i]+total_static_power_used_weekend[i])*sun_available[i] for i in range(len(AcPower))]

#solar power avaiable for Car Charger Use
SolarAvailable_weekend = [Power_WhileSun[i]-total_solar_available[i] for i in range(len(AcPower))]
for x in range(len(SolarAvailable)):
    if SolarAvailable_weekend[x] < 0:
        SolarAvailable_weekend[x] = 0
    else:
        continue

Hours_Available_weekend = 0
#Minimum cost periods for charging
Cost_Mins_weekend = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


#Percent Charge needed derived from miles needed
Charge_PercentNeeded_weekend = MilesNeeded_weekend/TotalRange
#Charge percent after (goal)
Charge_PercentAfter_weekend = Charge_Percent_weekend + Charge_PercentNeeded_weekend

#Time needed to charge in hours
Charge_TimeNeeded_weekend = Charge_PercentNeeded_weekend/Charge_Rate

#round up an hour
Charge_Periods_weekend = math.ceil(Charge_TimeNeeded_weekend)
#print(Charge_Periods_weekend)

#calculate How many total hours the device is available to ensure charging is possible
for x in range(len(isHome_weekend)):
    if isHome_weekend[x] == 1:
        Hours_Available_weekend = Hours_Available_weekend + 1
    else:
        continue

#ensure charging is possible
if Charge_Periods_weekend > Hours_Available_weekend:
    print('Error: Full charge is impossible with allocated time')


# In[11]:


#Decide whether to charge based on Power Cost, Solar Power available and Availabilty values for the hour
Cost_Periodcost_weekend = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Cost_Period_weekend = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Cost_Periodcost_weekend = [(Power_Cost_weekend[i]*(7.2-SolarAvailable_weekend[i]))*isHome_weekend[i] for i in range(len(Power_Cost_weekend))]
Cost_Period_weekend = [(Power_Cost_weekend[i]*(7.2-SolarAvailable_weekend[i]))*isHome_weekend[i] for i in range(len(Power_Cost_weekend))]
for x in range(len(Cost_Period_weekend)):
    if Cost_Period_weekend[x] == 0:
        Cost_Period_weekend[x] = 100
        round(Cost_Period_weekend[x], 4)
    else:
        Cost_Period_weekend[x] = round(Cost_Period_weekend[x], 4)
        continue
        
#print(Cost_Period_weekend)
p_weekend = Charge_Periods_weekend
#print(p_weekend)
for x in range(p_weekend):
    Cost_Min_ind_weekend = Cost_Period_weekend.index(min(Cost_Period_weekend))
    #print(Cost_Min_ind_weekend)
    Cost_Mins_weekend[Cost_Min_ind_weekend] = 1
    Cost_Min_weekend = min(Cost_Period_weekend)
    #print(Cost_Min)
    #print(Cost_Period)
    for x in range(len(Cost_Period_weekend)):
        if Cost_Period_weekend[x] == Cost_Min_weekend:
            Cost_Period_weekend[x] = 1000
        else:
            continue  

            
#print(Cost_Mins_weekend)
Start_afternoon_weekend = 0
for x in range(23):
    if Cost_Mins_weekend[x] == 1:
        print("Please start program after 5PM ")
        Start_afternoon_weekend = 1
        break
    else:
        continue


# In[12]:


#charge
Charger_Power_Usage_weekend = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Charger_Power_Cost_weekend = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Charge_Percent_curve_weekend = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Charge_Percent_current_weekend = Charge_Percent_weekend
Charge_PercentNeeded2_weekend = Charge_PercentNeeded_weekend*100
#print(Charge_PercentNeeded2_weekend)

for x in range(len(Cost_Mins_weekend)):
    if Cost_Mins_weekend[x] == 1:
        Charger_Power_Usage_weekend[x] = Charger_Power_Usage_weekend[x] + 7.2
        Charger_Power_Cost_weekend[x] = Cost_Periodcost_weekend[x]
#        Charge_Percent_current_weekend = Charge_Percent_current_weekend + 12.5
#        Charge_Percent_curve_weekend[x] = Charge_Percent_current_weekend
#    if x == 15:
#        Charge_Percent_current_weekend = Charge_Percent_current_weekend - Charge_PercentNeeded2_weekend
#        Charge_Percent_curve_weekend[x] = Charge_Percent_current_weekend
    else:
        continue
        
#print(Charge_Percent_curve_weekend)
#deal with %Charged        
Cost_Mins_weekend_afternoon_weekend = Cost_Mins_weekend.copy()
Charge_Percent_current_afternoon_weekend = 0
#print(Cost_Mins_weekend_afternoon_weekend)
#print(Start_afternoon_weekend)
if Start_afternoon_weekend == 1:
    Charge_Percent_curve_weekend[16] = Charge_Percent_weekend
    for x in range(8):
        #print(x)
        if Cost_Mins_weekend_afternoon_weekend[x+16] == 1:
            Charge_Percent_curve_weekend[x+16] = Charge_Percent_weekend + 12.5
            Charge_Percent_current_afternoon_weekend = Charge_Percent_weekend + 12.5
            Cost_Mins_weekend_afternoon_weekend[x+16] = 0
            break
        else:
            continue
    for x in range(8):
        if Cost_Mins_weekend_afternoon_weekend[16+x] == 1:
            Charge_Percent_curve_weekend[16+x] = Charge_Percent_current_afternoon + 12.5
            Charge_Percent_current_afternoon_weekend = Charge_Percent_current_afternoon_weekend+ 12.5
            Cost_Mins_weekend_afternoon_weekend[16+x] = 0
            break
        else:
            continue
    for x in range(8):
        if Cost_Mins_weekend_afternoon_weekend[16+x] == 1:
            Charge_Percent_curve_weekend[16+x] = Charge_Percent_current_afternoon_weekend+ 12.5
            Charge_Percent_current_afternoon_weekend= Charge_Percent_current_afternoon_weekend+ 12.5
            Cost_Mins_weekend_afternoon_weekend[16+x] = 0
            break
        else:
            continue
    for x in range(8):
       # print(x)
        if Cost_Mins_weekend_afternoon_weekend[x+16] == 1:
            Charge_Percent_curve_weekend[x+16] = Charge_Percent_current_afternoon_weekend+ 12.5
            Charge_Percent_current_afternoon_weekend= Charge_Percent_current_afternoon_weekend+ 12.5
            Cost_Mins_weekend_afternoon_weekend[x+16] = 0
            #print(Charge_Percent_curve_weekend)
            break
        else:
            continue
    for x in range(8):
        if Cost_Mins_weekend_afternoon_weekend[16+x] == 1:
            Charge_Percent_curve_weekend[16+x] = Charge_Percent_current_afternoon_weekend+ 12.5
            Charge_Percent_current_afternoon_weekend= Charge_Percent_current_afternoon_weekend+ 12.5
            Cost_Mins_weekend_afternoon_weekend[16+x] = 0
            break
        else:
            continue
    for x in range(8):
        #print(x)
        if Cost_Mins_weekend_afternoon_weekend[16+x] == 1:
            Charge_Percent_curve_weekend[16+x] = Charge_Percent_current_afternoon_weekend+ 12.5
            Charge_Percent_current_afternoon_weekend= Charge_Percent_current_afternoon_weekend+ 12.5
            Cost_Mins_weekend_afternoon_weekend[16+x] = 0
            break
        else:
            continue
    for x in range(8):
        #print(x)
        if Cost_Mins_weekend_afternoon_weekend[x+16] == 1:
            Charge_Percent_curve_weekend[x+16] = Charge_Percent_current_afternoon_weekend+ 12.5
            Charge_Percent_current_afternoon_weekend= Charge_Percent_current_afternoon_weekend+ 12.5
            Cost_Mins_weekend_afternoon_weekend[x+16] = 0
            #print(Charge_Percent_curve_weekend)
            break
        else:
            continue
    for x in range(16):
        #print(x)
        if Cost_Mins_weekend_afternoon_weekend[x] == 1 and Charge_Percent_current_afternoon_weekend > 0:
            Charge_Percent_curve_weekend[x] = Charge_Percent_current_afternoon_weekend + 12.5
            Charge_Percent_current_afternoon_weekend= Charge_Percent_current_afternoon_weekend + 12.5
            Cost_Mins_weekend_afternoon_weekend[x] = 0
            #print(Charge_Percent_curve_weekend)
            break
        elif Cost_Mins_weekend_afternoon_weekend[x] == 1 and Charge_Percent_current_afternoon_weekend == 0:
            Charge_Percent_curve_weekend[x] = Charge_Percent_weekend + 12.5
            Charge_Percent_current_afternoon_weekend= Charge_Percent_weekend + 12.5
            Cost_Mins_weekend_afternoon_weekend[x] = 0
            break
        else:
            continue
    for x in range(16):
        if Cost_Mins_weekend_afternoon_weekend[x] == 1:
            Charge_Percent_curve_weekend[x] = Charge_Percent_current_afternoon_weekend+ 12.5
            Charge_Percent_current_afternoon_weekend= Charge_Percent_current_afternoon_weekend+ 12.5
            Cost_Mins_weekend_afternoon_weekend[x] = 0
            break
        else:
            continue
    for x in range(16):
        if Cost_Mins_weekend_afternoon_weekend[x] == 1:
            Charge_Percent_curve_weekend[x] = Charge_Percent_current_afternoon_weekend+ 12.5
            Charge_Percent_current_afternoon_weekend= Charge_Percent_current_afternoon_weekend+ 12.5
            Cost_Mins_weekend_afternoon_weekend[x] = 0
            break
        else:
            continue
    for x in range(16):
        if Cost_Mins_weekend_afternoon_weekend[x] == 1:
            Charge_Percent_curve_weekend[x] = Charge_Percent_current_afternoon_weekend+ 12.5
            Charge_Percent_current_afternoon_weekend= Charge_Percent_current_afternoon_weekend+ 12.5
            Cost_Mins_weekend_afternoon_weekend[x] = 0
            break
        else:
            continue
    for x in range(16):
        #print(x)
        if Cost_Mins_weekend_afternoon_weekend[x] == 1:
            Charge_Percent_curve_weekend[x] = Charge_Percent_current_afternoon_weekend+ 12.5
            Charge_Percent_current_afternoon_weekend= Charge_Percent_current_afternoon_weekend+ 12.5
            Cost_Mins_weekend_afternoon_weekend[x] = 0
            break
        else:
            continue
    for x in range(16):
        if Cost_Mins_weekend_afternoon_weekend[x] == 1:
            Charge_Percent_curve_weekend[x] = Charge_Percent_current_afternoon_weekend+ 12.5
            Charge_Percent_current_afternoon_weekend= Charge_Percent_current_afternoon_weekend+ 12.5
            Cost_Mins_weekend_afternoon_weekend[x] = 0
           # print(Charge_Percent_curve_weekend)
            break
        else:
            continue
    for x in range(16):
        if Cost_Mins_weekend_afternoon_weekend[x] == 1:
            Charge_Percent_curve_weekend[x] = Charge_Percent_current_afternoon_weekend+ 12.5
            Charge_Percent_current_afternoon_weekend= Charge_Percent_current_afternoon_weekend+ 12.5
            Cost_Mins_weekend_afternoon_weekend[x] = 0
            break
        else:
            continue
    for x in range(16):
        if Cost_Mins_weekend_afternoon_weekend[x] == 1:
            Charge_Percent_curve_weekend[x] = Charge_Percent_current_afternoon_weekend+ 12.5
            Charge_Percent_current_afternoon_weekend= Charge_Percent_current_afternoon_weekend+ 12.5
            Cost_Mins_weekend_afternoon_weekend[x] = 0
            break
        else:
            continue
    for x in range(16):
        if Cost_Mins_weekend_afternoon_weekend[x] == 1:
            Charge_Percent_curve_weekend[x] = Charge_Percent_current_afternoon_weekend+ 12.5
            Charge_Percent_current_afternoon_weekend= Charge_Percent_current_afternoon_weekend+ 12.5
            Cost_Mins_weekend_afternoon_weekend[x] = 0
            break
        else:
            continue
    for x in range(16):
        #print(x)
        if Cost_Mins_weekend_afternoon_weekend[x] == 1:
            Charge_Percent_curve_weekend[x] = Charge_Percent_current_afternoon_weekend+ 12.5
            Charge_Percent_current_afternoon_weekend= Charge_Percent_current_afternoon_weekend+ 12.5
            Cost_Mins_weekend_afternoon_weekend[x] = 0
            break
        else:
            continue
    for x in range(16):
        if Cost_Mins_weekend_afternoon_weekend[x] == 1:
            Charge_Percent_curve_weekend[x] = Charge_Percent_current_afternoon_weekend+ 12.5
            Charge_Percent_current_afternoon_weekend= Charge_Percent_current_afternoon_weekend + 12.5
            Cost_Mins_weekend_afternoon_weekend[x] = 0
            #print(Charge_Percent_curve_weekend)
            break
        else:
            continue
    for x in range(16):
        if Cost_Mins_weekend_afternoon_weekend[x] == 1:
            Charge_Percent_curve_weekend[x] = Charge_Percent_current_afternoon_weekend+ 12.5
            Charge_Percent_current_afternoon_weekend= Charge_Percent_current_afternoon_weekend+ 12.5
            Cost_Mins_weekend_afternoon_weekend[x] = 0
            break
        else:
            continue
    for x in range(16):
        if Cost_Mins_weekend_afternoon_weekend[x] == 1:
            Charge_Percent_curve_weekend[x] = Charge_Percent_current_afternoon_weekend+ 12.5
            Charge_Percent_current_afternoon_weekend= Charge_Percent_current_afternoon_weekend+ 12.5
            Cost_Mins_weekend_afternoon_weekend[x] = 0
            break
        else:
            continue
    for x in range(16):
        if Cost_Mins_weekend_afternoon_weekend[x] == 1:
            Charge_Percent_curve_weekend[x] = Charge_Percent_current_afternoon_weekend+ 12.5
            Charge_Percent_current_afternoon_weekend= Charge_Percent_current_afternoon_weekend+ 12.5
            Cost_Mins_weekend_afternoon_weekend[x] = 0
            break
        else:
            continue
    for x in range(16):
        #print(x)
        if Cost_Mins_weekend_afternoon_weekend[x] == 1:
            Charge_Percent_curve_weekend[x] = Charge_Percent_current_afternoon_weekend + 12.5
            Charge_Percent_current_afternoon_weekend= Charge_Percent_current_afternoon_weekend + 12.5
            Cost_Mins_weekend_afternoon_weekend[x] = 0
            break
        else:
            continue
            
            
#print(Charge_Percent)
#print(Charge_Percent_curve_weekend)

for x in range(len(isHome_weekend)):
    if isHome_weekend[x] == 0:
        Charge_Percent_curve_weekend[x] = Charge_Percent
        #print(x)
        #print(Charge_Percent_curve_weekend)
    else:
        continue
#print(Charge_Percent_curve_weekend)
for x in range(24):
    if Charge_Percent_curve_weekend[x] == 0 and Charge_Percent_curve_weekend[x-1] != 0:
        Charge_Percent_curve_weekend[x] = Charge_Percent_curve_weekend[x-1]
    else:
        continue
for x in range(24):
    if Charge_Percent_curve_weekend[x] == 0 and Charge_Percent_curve_weekend[23] != 0:
        Charge_Percent_curve_weekend[x] = Charge_Percent_curve_weekend[23]
    else:
        continue
        
#print(Charge_Percent_curve_weekend)
        
#for x in range(len(Charge_Percent_curve_weekend)):
#    if Charge_Percent_curve_weekend[x] == 0:
#        Charge_Percent_curve_weekend[x] = Charge_Percent_curve_weekend[x-1]
#    else:
#        continue

#for x in range(9):
#    Charge_Percent_curve.insert(0, Charge_Percent_curve.pop())
#print(Charge_Percent_current)
#print(Charge_Percent_curve)
#print(Charger_Power_Usage_weekend)


# In[13]:


#Cost Comparison

Cost_Optimized_CarCharger_weekend = sum(Charger_Power_Cost_weekend )

Total_Power_Usage_weekend  = [AcPower[i]+total_static_power_used_weekend[i] for i in range(len(AcPower))]
Total_Power_Costbefore_weekend  = [Total_Power_Usage_weekend[i]*Power_Cost_weekend[i] for i in range (len(Total_Power_Usage_weekend ))]


b_weekend = sum(Total_Power_Costbefore_weekend) + sum(Charger_Power_Cost_weekend)


#Consecutive days for unoptimized weekend cost
Charge_Periods_consecutive_weekend = math.ceil(Charge_TimeNeeded_weekend)

#Hours plugged in and not used in unoptimized variant
Hours_Unused_PluggedIn_consecutive_weekend = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Hours_used_PluggedIn_consecutive_weekend = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

Charge_Percent_before_consecutive_weekend = 100 - Charge_PercentNeeded_weekend*100

#print(Charge_Percent_before_consecutive)
Charge_Percent_Unoptimized_consecutive_weekend = [Charge_Percent_before_consecutive_weekend, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Charge_Percent_current_unopt_consecutive_weekend = Charge_Percent_before_consecutive_weekend


for x in range(len(Charge_Percent_Unoptimized_consecutive_weekend)):
    if Charge_Percent_Unoptimized_consecutive_weekend[x] < 100:
        if x == 0:
            Charge_Percent_Unoptimized_consecutive_weekend[x] = Charge_Percent_Unoptimized_consecutive_weekend[x]
        else:
            Charge_Percent_Unoptimized_consecutive_weekend[x] = Charge_Percent_current_unopt_consecutive_weekend + 12.5
            Charge_Percent_current_unopt_consecutive_weekend = Charge_Percent_current_unopt_consecutive_weekend + 12.5
    if Charge_Percent_Unoptimized_consecutive_weekend[x-1] > 100:
        Charge_Percent_Unoptimized_consecutive_weekend[x-1] = 100
    if Charge_Percent_Unoptimized_consecutive_weekend[x-1] == 100:
        Charge_Percent_Unoptimized_consecutive_weekend[x] = 100
    else:
        continue
        

Unoptimized_TotalPower_Usedpluggedin_consecutive_weekend = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Unoptimized_TotalPower_Unusedpluggedin_consecutive_weekend = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Unoptimized_TotalCost_consecutive_weekend = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 
Unoptimized_TotalPower_UsedpluggedinCost_consecutive_weekend = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 
PowerCost_charger_Unoptimized_UnusedPluggedin_consecutive_weekend = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


iterator_unoptimized_consecutive_weekend = round(Charge_Periods_consecutive_weekend)
for x in range(iterator_unoptimized_consecutive_weekend):
        if isHome_weekend[x+18] == 1:
            Hours_used_PluggedIn_consecutive_weekend[x+18] = 1
        else:
            if isHome_weekend[x+19] == 1:
                Hours_used_PluggedIn_consecutive_weekend[x+19] = 1
            else:
                if isHome_weekend[x+20] == 1:
                    Hours_used_PluggedIn_consecutive_weekend[x+20] = 1
                else: 
                    if isHome_weekend[x+21] == 1:
                        Hours_used_PluggedIn_consecutive_weekend[x+21] = 1
                    else:
                        if isHome_weekend[x+22] == 1:
                            Hours_used_PluggedIn_consecutive_weekend[x+22] = 1
                        else:
                            if isHome_weekend[x+23] == 1:
                                Hours_used_PluggedIn_consecutive_weekend[x+23] = 1
                            else:
                                if isHome_weekend[x+24] == 1:
                                    Hours_used_PluggedIn_consecutive_weekend[x+24] = 1
                                else:
                                    continue
                                    

#print(Hours_used_PluggedIn_consecutive)                                    
for x in range(len(Hours_Unused_PluggedIn_consecutive_weekend)):
    if Hours_used_PluggedIn_consecutive_weekend[x] == 1:
        Hours_Unused_PluggedIn_consecutive_weekend[x] = 0
    elif isHome_weekend[x] == 1 and Hours_Unused_PluggedIn_consecutive_weekend[x] == 0:
        Hours_Unused_PluggedIn_consecutive_weekend[x] = 1
    else:
        continue
        
for x in range(17):
    Charge_Percent_Unoptimized_consecutive_weekend.insert(0, Charge_Percent_Unoptimized_consecutive_weekend.pop())
for x in range(17):
    if Charge_Percent_Unoptimized_consecutive_weekend[x] == 100:
        Charge_Percent_Unoptimized_consecutive_weekend[x] = Charge_Percent_before_consecutive_weekend
    else:
        continue
        
for x in range(24):
    if Hours_used_PluggedIn_consecutive_weekend[x] == 1:
        Unoptimized_TotalPower_UsedpluggedinCost_consecutive_weekend[x] = Cost_Periodcost_weekend[x]
    else:
        continue

        
Unoptimized_TotalPower_Usedpluggedin_consecutive_weekend = [Hours_used_PluggedIn_consecutive_weekend[i]*7.2 for i in range (len(Hours_Unused_PluggedIn_consecutive_weekend))]


Unoptimized_TotalPower_Unusedpluggedin_consecutive_weekend = [Hours_Unused_PluggedIn_consecutive_weekend[i]*.030 for i in range (len(Hours_Unused_PluggedIn_consecutive_weekend))]


Unoptimized_TotalPower_consecutive_weekend = [Unoptimized_TotalPower_Usedpluggedin_consecutive_weekend[i]+Unoptimized_TotalPower_Unusedpluggedin_consecutive[i] for i in range (len(Unoptimized_TotalPower_Usedpluggedin_consecutive))]

PowerCost_charger_Unoptimized_UnusedPluggedin_consecutive_weekend = [Unoptimized_TotalPower_Unusedpluggedin_consecutive_weekend[i]*Power_Cost[i] for i in range (len(Unoptimized_TotalPower_consecutive_weekend))]
#print(PowerCost_charger_Unoptimized_UnusedPluggedin_consecutive_weekend)
PowerCost_charger_Unoptimized_consecutive_weekend = [Unoptimized_TotalPower_UsedpluggedinCost_consecutive_weekend[i]+PowerCost_charger_Unoptimized_UnusedPluggedin_consecutive_weekend[i] for i in range (len(Unoptimized_TotalPower_consecutive_weekend))]
#print(PowerCost_charger_Unoptimized_consecutive_weekend)
#print(PowerCost_charger_Unoptimized)
c_consecutive_weekend = sum(PowerCost_charger_Unoptimized_consecutive_weekend)        


x_Charger_Power_Usage_weekend = Charger_Power_Usage_weekend.copy()

a_consecutive_weekend = sum(Total_Power_Costbefore_weekend)+sum(PowerCost_charger_Unoptimized_consecutive_weekend)

i_consecutive_weekend = Unoptimized_TotalPower_consecutive_weekend


# In[14]:


x_Charger_Power_Usage_weekend_integral = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 
i_consecutive_weekend_integral = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

x_Charger_Power_Usage_weekend_integral = geek.cumsum(x_Charger_Power_Usage_weekend)  
#print(x_Charger_Power_Usage_weekend_integral)

i_consecutive_weekend_integral = geek.cumsum(i_consecutive_weekend)  
#print(i_consecutive_weekend_integral)

plt.plot(y, x_Charger_Power_Usage_weekend) 
plt.xlabel('Time of Day') 
plt.ylabel('Power Consumed (KWh)') 
plt.title('Weekend Optimized Vs Unoptimized Power Consumption') 
#plt.show() 

plt.plot(y, i_consecutive_weekend) 
plt.xlabel('Time of Day') 
plt.ylabel('Power Consumed (KWh)') 
orange_patch = mpatches.Patch(color='Orange', label='Unoptimized')
blue_patch = mpatches.Patch(color='Blue', label='Optimized')
plt.legend(handles=[blue_patch,orange_patch])
plt.show() 

plt.plot(y, x_Charger_Power_Usage_weekend_integral) 
plt.xlabel('Time of Day') 
plt.ylabel('Power Consumed (KW)') 
plt.title('Weekend Optimized Vs Unoptimized Total Power Consumption') 
#plt.show() 

plt.plot(y, i_consecutive_weekend_integral) 
plt.xlabel('Time of Day') 
plt.ylabel('Power Consumed (KW)') 
orange_patch = mpatches.Patch(color='Orange', label='Unoptimized')
blue_patch = mpatches.Patch(color='Blue', label='Optimized')
plt.legend(handles=[blue_patch,orange_patch])
plt.show() 


plt.plot(y, Charge_Percent_curve_weekend)
plt.xlabel('Time of Day') 
plt.ylabel('% Charged') 
plt.title('Weekend Optimized Vs Unoptimzied charge Curve') 
orange_patch = mpatches.Patch(color='Orange', label='Unoptimized')
blue_patch = mpatches.Patch(color='Blue', label='Optimized')
plt.legend(handles=[blue_patch,orange_patch])
#plt.show() 

plt.plot(y, Charge_Percent_Unoptimized_consecutive_weekend)
plt.xlabel('Time of Day') 
plt.ylabel('% Charged') 
plt.show() 


Monthly_Optimized_Carchargerpowercost = Cost_Optimized_CarCharger*22+Cost_Optimized_CarCharger_weekend*8

Monthly_Unoptimized_CarChargerPowerCost = (c*1) + (c_consecutive*21)+(c_consecutive_weekend*8)

Monthly_Optimized_Bill = (Monthly_Optimized_Carchargerpowercost)+(sum(Total_Power_Costbefore)*22)+(sum(Total_Power_Costbefore_weekend)*8)

Monthly_Unoptimized_Bill = (Monthly_Unoptimized_CarChargerPowerCost) + (sum(Total_Power_Costbefore)*22)+(sum(Total_Power_Costbefore_weekend)*8)

expected_weekendcost = (c_consecutive_weekend - Cost_Optimized_CarCharger_weekend)/(c_consecutive_weekend)


expected_weekcost = (c - Cost_Optimized_CarCharger)/(c)

#expected-actual/actual

print('\n')
print('The Optimized Weekend cost of the optimized car charger will be:$', round(Cost_Optimized_CarCharger_weekend,2))
print('The Unoptimized Weekend cost for the car charger is:$', round(c_consecutive_weekend,2))
print('\n')
print('The Optimized Monthly cost of the optimized car charger will be:$', round(Monthly_Optimized_Carchargerpowercost,2))
print('The Unoptimized Montly cost for the car charger is:$', round(Monthly_Unoptimized_CarChargerPowerCost,2))
print('\n')
print('The Optimized Monthly Utility Bill is:$', round(Monthly_Optimized_Bill,2))
print('The Unoptimized Monthy Utility bill is:$', round(Monthly_Unoptimized_Bill,2))
print('\n')
print('The % improvement of the weekday cost is', round(expected_weekcost*100,2),'%')

print('The % improvement of the weekend cost is', round(expected_weekendcost*100, 2),'%')


# In[ ]:




