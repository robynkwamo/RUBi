#!/usr/bin/env python
# coding: utf-8

# In[27]:


#Total Solar 
Panel_power = .370 #Kilowatts 
numPanels = 3
sun_available = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:1, 7:1, 8:1, 9:1, 10:1, 11:1, 12:1, 
                13:1, 14:1, 15:1, 16:1, 17:1, 18:1, 19:1, 20:1, 21:0, 22:0, 23:0}

total_solar_available = {0:(sun_available[0]*numPanels*Panel_power), 1:(sun_available[1]*numPanels*Panel_power), 
                        2:(sun_available[2]*numPanels*Panel_power), 3:(sun_available[3]*numPanels*Panel_power), 
                        4:(sun_available[4]*numPanels*Panel_power), 5:(sun_available[5]*numPanels*Panel_power), 
                        6:(sun_available[6]*numPanels*Panel_power), 7:(sun_available[7]*numPanels*Panel_power),
                        8:(sun_available[8]*numPanels*Panel_power), 9:(sun_available[9]*numPanels*Panel_power),
                        10:(sun_available[10]*numPanels*Panel_power), 11:(sun_available[11]*numPanels*Panel_power),
                        12:(sun_available[12]*numPanels*Panel_power), 13:(sun_available[13]*numPanels*Panel_power),
                        14:(sun_available[14]*numPanels*Panel_power), 15:(sun_available[15]*numPanels*Panel_power), 
                        16:(sun_available[16]*numPanels*Panel_power), 17:(sun_available[17]*numPanels*Panel_power),
                        18:(sun_available[18]*numPanels*Panel_power), 19:(sun_available[19]*numPanels*Panel_power),
                        20:(sun_available[20]*numPanels*Panel_power), 21:(sun_available[21]*numPanels*Panel_power),
                        22:(sun_available[22]*numPanels*Panel_power), 23:(sun_available[23]*numPanels*Panel_power)}

#Power cost in dollars
power_cost_week = {0:.092, 1:.092, 2:.092, 3:.096, 4:.1, 5:.128, 6:.164, 7:.164, 8:.148, 9:.14, 10:.14, 11:.128,
                   12:.12, 13:.108, 14:.104, 15:.104, 16:.104, 17:.108, 18:.124, 19:.148, 20:.128, 21:.112, 22:.104, 23:.096}

power_cost_weekend = {0:.092, 1:.092, 2:.096, 3:.096, 4:.092, 5:.096, 6:.108, 7:.108, 8:.116, 9:.112, 10:.108, 11:.104,
                      12:.096, 13:.092, 14:.092, 15:.092, 16:.096, 17:.1, 18:.112, 19:.128, 20:.116, 21:.104, 22:.096, 23:.092}

#Total static power used in kilowatss (many assumptions) 
#Assume 9-5 job with hour long commute 
isHome_week = {0:1, 1:1, 2:1, 3:1, 4:1, 5:1, 6:1, 7:1, 8:0, 9:0, 10:0, 11:0, 12:0, 
               13:0, 14:0, 15:0, 16:0, 17:0, 18:1, 19:1, 20:1, 21:1, 22:1, 23:1}
isSleeping_week = {0:1, 1:1, 2:1, 3:1, 4:1, 5:1, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 
               13:0, 14:0, 15:0, 16:0, 17:0, 18:0, 19:0, 20:0, 21:0, 22:1, 23:1}
isHome_weekend = {0:1, 1:1, 2:1, 3:1, 4:1, 5:1, 6:1, 7:1, 8:1, 9:1, 10:1, 11:1, 12:1, 
               13:1, 14:0, 15:0, 16:0, 17:0, 18:1, 19:1, 20:1, 21:1, 22:1, 23:1}
isSleeping_weekend = {0:1, 1:1, 2:1, 3:1, 4:1, 5:1, 6:1, 7:1, 8:0, 9:0, 10:0, 11:0, 12:0, 
               13:0, 14:0, 15:0, 16:0, 17:0, 18:0, 19:0, 20:0, 21:0, 22:0, 23:1}

isLight_week = {}
isLight_weekend = {}
n = 0
while n <= 23:
    if (isHome_week[n] == 1) and (isSleeping_week[n] == 0):
        isLight_week[n] = 1
    else:
        isLight_week[n] = 0
    if (isHome_weekend[n] == 1) and (isSleeping_weekend[n] == 0):
        isLight_weekend[n] = 1
    else:
        isLight_weekend[n] = 0
    n=n+1
    
#use waterheater 2 hours before work, sleep in 2 hours on weekends (3 kWh)
Waterheater_power_week = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:3, 7:3, 8:0, 9:0, 10:0, 11:0, 12:0, 
                         13:0, 14:0, 15:0, 16:0, 17:0, 18:0, 19:0, 20:3, 21:0, 22:0, 23:0}
Waterheater_power_weekend = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:3, 9:3, 10:0, 11:0, 12:0, 
                         13:0, 14:0, 15:0, 16:0, 17:0, 18:0, 19:0, 20:0, 21:3, 22:0, 23:0}
Fridge_power = {0:0, 1:.1, 2:0, 3:0, 4:.07, 5:0, 6:0, 7:.15, 8:0, 9:.08, 10:0, 11:0, 12:.1, 
                13:0, 14:.09, 15:0, 16:0, 17:.15, 18:.1, 19:0, 20:0, 21:.08, 22:0, 23:.075}

numLights = 20
onelight_power = .06 
Light_power_week = {0:(numLights*isLight_week[0]*onelight_power), 1:(numLights*isLight_week[1]*onelight_power),
                    2:(numLights*isLight_week[2]*onelight_power), 3:(numLights*isLight_week[3]*onelight_power),
                    4:(numLights*isLight_week[4]*onelight_power), 5:(numLights*isLight_week[5]*onelight_power), 
                    6:(numLights*isLight_week[6]*onelight_power), 7:(numLights*isLight_week[7]*onelight_power),
                    8:(numLights*isLight_week[8]*onelight_power), 9:(numLights*isLight_week[9]*onelight_power), 
                    10:(numLights*isLight_week[10]*onelight_power), 11:(numLights*isLight_week[11]*onelight_power),
                    12:(numLights*isLight_week[12]*onelight_power), 13:(numLights*isLight_week[13]*onelight_power),
                    14:(numLights*isLight_week[14]*onelight_power), 15:(numLights*isLight_week[15]*onelight_power), 
                    16:(numLights*isLight_week[16]*onelight_power), 17:(numLights*isLight_week[17]*onelight_power),
                    18:(numLights*isLight_week[18]*onelight_power), 19:(numLights*isLight_week[19]*onelight_power),
                    20:(numLights*isLight_week[20]*onelight_power), 21:(numLights*isLight_week[21]*onelight_power), 
                    22:(numLights*isLight_week[22]*onelight_power), 23:(numLights*isLight_week[23]*onelight_power)}

Light_power_weekend = {0:(numLights*isLight_weekend[0]*onelight_power), 1:(numLights*isLight_weekend[1]*onelight_power),
                    2:(numLights*isLight_weekend[2]*onelight_power), 3:(numLights*isLight_weekend[3]*onelight_power),
                    4:(numLights*isLight_weekend[4]*onelight_power), 5:(numLights*isLight_weekend[5]*onelight_power), 
                    6:(numLights*isLight_weekend[6]*onelight_power), 7:(numLights*isLight_weekend[7]*onelight_power),
                    8:(numLights*isLight_weekend[8]*onelight_power), 9:(numLights*isLight_weekend[9]*onelight_power), 
                    10:(numLights*isLight_weekend[10]*onelight_power), 11:(numLights*isLight_weekend[11]*onelight_power),
                    12:(numLights*isLight_weekend[12]*onelight_power), 13:(numLights*isLight_weekend[13]*onelight_power),
                    14:(numLights*isLight_weekend[14]*onelight_power), 15:(numLights*isLight_weekend[15]*onelight_power), 
                    16:(numLights*isLight_weekend[16]*onelight_power), 17:(numLights*isLight_weekend[17]*onelight_power),
                    18:(numLights*isLight_weekend[18]*onelight_power), 19:(numLights*isLight_weekend[19]*onelight_power),
                    20:(numLights*isLight_weekend[20]*onelight_power), 21:(numLights*isLight_weekend[21]*onelight_power), 
                    22:(numLights*isLight_weekend[22]*onelight_power), 23:(numLights*isLight_weekend[23]*onelight_power)}


total_static_power_used_week = {0:(Waterheater_power_week[0]+Fridge_power[0]+Light_power_week[0]), 
                                1:(Waterheater_power_week[1]+Fridge_power[1]+Light_power_week[1]), 
                                2:(Waterheater_power_week[2]+Fridge_power[2]+Light_power_week[2]), 
                                3:(Waterheater_power_week[3]+Fridge_power[3]+Light_power_week[3]), 
                                4:(Waterheater_power_week[4]+Fridge_power[4]+Light_power_week[4]), 
                                5:(Waterheater_power_week[5]+Fridge_power[5]+Light_power_week[5]),
                                6:(Waterheater_power_week[6]+Fridge_power[6]+Light_power_week[6]), 
                                7:(Waterheater_power_week[7]+Fridge_power[7]+Light_power_week[7]),
                                8:(Waterheater_power_week[8]+Fridge_power[8]+Light_power_week[8]),
                                9:(Waterheater_power_week[9]+Fridge_power[9]+Light_power_week[9]),
                                10:(Waterheater_power_week[10]+Fridge_power[10]+Light_power_week[10]),
                                11:(Waterheater_power_week[11]+Fridge_power[11]+Light_power_week[11]),
                                12:(Waterheater_power_week[12]+Fridge_power[12]+Light_power_week[12]),
                                13:(Waterheater_power_week[13]+Fridge_power[13]+Light_power_week[13]),
                                14:(Waterheater_power_week[14]+Fridge_power[14]+Light_power_week[14]),
                                15:(Waterheater_power_week[15]+Fridge_power[15]+Light_power_week[15]), 
                                16:(Waterheater_power_week[16]+Fridge_power[16]+Light_power_week[16]), 
                                17:(Waterheater_power_week[17]+Fridge_power[17]+Light_power_week[17]),
                                18:(Waterheater_power_week[18]+Fridge_power[18]+Light_power_week[18]),
                                19:(Waterheater_power_week[19]+Fridge_power[19]+Light_power_week[19]),
                                20:(Waterheater_power_week[20]+Fridge_power[20]+Light_power_week[20]),
                                21:(Waterheater_power_week[21]+Fridge_power[21]+Light_power_week[21]),
                                22:(Waterheater_power_week[22]+Fridge_power[22]+Light_power_week[22]),
                                23:(Waterheater_power_week[23]+Fridge_power[23]+Light_power_week[23])}

total_static_power_used_weekend = {0:(Waterheater_power_weekend[0]+Fridge_power[0]+Light_power_weekend[0]), 
                                1:(Waterheater_power_weekend[1]+Fridge_power[1]+Light_power_weekend[1]), 
                                2:(Waterheater_power_weekend[2]+Fridge_power[2]+Light_power_weekend[2]), 
                                3:(Waterheater_power_weekend[3]+Fridge_power[3]+Light_power_weekend[3]), 
                                4:(Waterheater_power_weekend[4]+Fridge_power[4]+Light_power_weekend[4]), 
                                5:(Waterheater_power_weekend[5]+Fridge_power[5]+Light_power_weekend[5]),
                                6:(Waterheater_power_weekend[6]+Fridge_power[6]+Light_power_weekend[6]), 
                                7:(Waterheater_power_weekend[7]+Fridge_power[7]+Light_power_weekend[7]),
                                8:(Waterheater_power_weekend[8]+Fridge_power[8]+Light_power_weekend[8]),
                                9:(Waterheater_power_weekend[9]+Fridge_power[9]+Light_power_weekend[9]),
                                10:(Waterheater_power_weekend[10]+Fridge_power[10]+Light_power_weekend[10]),
                                11:(Waterheater_power_weekend[11]+Fridge_power[11]+Light_power_weekend[11]),
                                12:(Waterheater_power_weekend[12]+Fridge_power[12]+Light_power_weekend[12]),
                                13:(Waterheater_power_weekend[13]+Fridge_power[13]+Light_power_weekend[13]),
                                14:(Waterheater_power_weekend[14]+Fridge_power[14]+Light_power_weekend[14]),
                                15:(Waterheater_power_weekend[15]+Fridge_power[15]+Light_power_weekend[15]), 
                                16:(Waterheater_power_weekend[16]+Fridge_power[16]+Light_power_weekend[16]), 
                                17:(Waterheater_power_weekend[17]+Fridge_power[17]+Light_power_weekend[17]),
                                18:(Waterheater_power_weekend[18]+Fridge_power[18]+Light_power_weekend[18]),
                                19:(Waterheater_power_weekend[19]+Fridge_power[19]+Light_power_weekend[19]),
                                20:(Waterheater_power_weekend[20]+Fridge_power[20]+Light_power_weekend[20]),
                                21:(Waterheater_power_weekend[21]+Fridge_power[21]+Light_power_weekend[21]),
                                22:(Waterheater_power_weekend[22]+Fridge_power[22]+Light_power_weekend[22]),
                                23:(Waterheater_power_weekend[23]+Fridge_power[23]+Light_power_weekend[23])}


#Temperature 
outsideTemp = 75
indoorTemp = 70
sleepingTemp = 68


temp_pref_simple0 = {0:indoorTemp, 1:indoorTemp, 2:indoorTemp, 3:indoorTemp, 4:indoorTemp, 5:indoorTemp, 6:indoorTemp,
                     7:indoorTemp, 8:indoorTemp, 9:indoorTemp, 10:indoorTemp, 11:indoorTemp, 12:indoorTemp, 13:indoorTemp,
                     14:indoorTemp, 15:indoorTemp, 16:indoorTemp, 17:indoorTemp, 18:indoorTemp, 19:indoorTemp, 20:indoorTemp,
                     21:indoorTemp, 22:indoorTemp, 23:indoorTemp}

temp_pref_week0 = {}
temp_pref_weekend0 = {}
i = 0
while i <=23:
    if (isSleeping_week[i] == 1):
        temp_pref_week0[i] = sleepingTemp
    elif (isSleeping_week[i] == 0) and (isHome_week[i] == 1):
        temp_pref_week0[i] = indoorTemp
    else:
        temp_pref_week0[i] = outside_temp
    if (isSleeping_weekend[i] == 1):
        temp_pref_weekend0[i] = sleepingTemp
    elif (isSleeping_weekend[i] == 0) and (isHome_weekend[i] == 1):
        temp_pref_weekend0[i] = indoorTemp
    else:
        temp_pref_weekend0[i] = outside_temp
    i=i+1

temp_pref_simple = {}
temp_pref_week = {}
temp_pref_weekend = {}
y=0
while y<=95:       #check every 15 minutes  
    temp_pref_week[y] = temp_pref_week0[int(y/4)]
    temp_pref_weekend[y] = temp_pref_weekend0[int(y/4)]
    temp_pref_simple[y] = temp_pref_simple0[int(y/4)]
    y=y+1
    


# In[26]:


print(total_static_power_used_week)
print(sum(total_static_power_used_week.values()))
print(total_static_power_used_weekend)
print(sum(total_static_power_used_weekend.values()))

#print(temp_pref_week)
#print(temp_pref_weekend)


# In[22]:



AC_power_usage_week = {}
AC_power_usage_weekend = {}
indoor_temp_week = {}
indoor_temp_week[0] = 70 #Assume AC is not on at the start 
indoor_temp_weekend = {}
indoor_temp_weekend[0] = 70
temp_increase_rate = 1 #degrees per 15 minute 
temp_decrease_rate = 1 #degrees per 15 minutes 
sqFootage = 640
EER = 2.7 # 3 star 



def Basic_AC(outsideTemp, indoorTemp, setTemp, AC_power):
    
    for x in range(96):
        if (indoorTemp[x] > setTemp[x]): # AC on 
            AC_power[x] = (((sqFootage/500)*(.87925)/EER))
            indoorTemp[x+1] = indoorTemp[x] - temp_decrease_rate
        elif (indoorTemp[x] == outside_temp):
            AC_power[x] = 0
            indoorTemp[x+1] = indoorTemp[x]
        else: #AC off
            AC_power[x] = 0
            indoorTemp[x+1] = indoorTemp[x] + temp_increase_rate 
               
            
    return ({0: AC_power, 1:indoorTemp})

def getAC_power(AC_power):
    k=0
    n=0
    r={}
    while k<=92:        
        r[n] = AC_power[k]+AC_power[k+1]+AC_power[k+2]+AC_power[k+3]        
        n=n+1
        k=k+4
    return r
        
def getCost(price, usage):
    n=0
    cost = {}
    while n<=23:
        cost[n] = price[n]*usage[n]
        n=n+1
    return cost 


# In[23]:


print("total basic AC power per weekday, const 70 inside (kW): ",sum(getAC_power(Basic_AC(outside_temp, indoor_temp_week, temp_pref_simple, AC_power_usage_week)[0]).values()))

print("total cost of basic AC per weekday, const 70 inside ($): ",sum(getCost(power_cost_week, getAC_power(Basic_AC(outside_temp, indoor_temp_week, temp_pref_simple, AC_power_usage_week)[0])).values()))

print("total basic AC power per weekday (kW): ",sum(getAC_power(Basic_AC(outside_temp, indoor_temp_week, temp_pref_week, AC_power_usage_week)[0]).values()))

print("total cost of basic AC per weekday ($): ",sum(getCost(power_cost_week, getAC_power(Basic_AC(outside_temp, indoor_temp_week, temp_pref_week, AC_power_usage_week)[0])).values()))

print("total basic AC power per weekend (kW): ",sum(getAC_power(Basic_AC(outside_temp, indoor_temp_weekend, temp_pref_weekend, AC_power_usage_weekend)[0]).values()))

print("total cost of basic AC per weekday ($): ",sum(getCost(power_cost_weekend, getAC_power(Basic_AC(outside_temp, indoor_temp_weekend, temp_pref_weekend, AC_power_usage_weekend)[0])).values()))

#print(Basic_AC(outside_temp, indoor_temp_week, temp_pref_week, AC_power_usage_week)[1])
#print(Basic_AC(outside_temp, indoor_temp_weekend, temp_pref_weekend, AC_power_usage_weekend)[1])


# In[9]:


from gurobipy import*
m = Model()

AC_usage = []
z=0
while z<=23:
    AC_usage = getCost(power_cost_week, getAC_power(Basic_AC(outside_temp, indoor_temp_week, temp_pref_week, AC_power_usage_week)[0]))
    AC_usage = m.addVar()
    
    prefTemp = temp_pref_week[z] 
    prefTemp = m.addVar()
    
    real_temp = Basic_AC(outside_temp, indoor_temp_weekend, temp_pref_weekend, AC_power_usage_weekend)[1]
    #realTemp = real_temp[z].values() 
    real_Temp = m.addVar()
    
    m.update()
    m.addConstr(real_Temp - prefTemp <= 2)
    m.addConstr(prefTemp - real_Temp <= 2)
    m.setObjective(AC_usage, GRB.MINIMIZE)
    m.params.outputflag = 0

    m.optimize()
    
    z=z+1


# In[10]:


AC_usage


# In[17]:


getCost(power_cost_week, getAC_power(Basic_AC(outside_temp, indoor_temp_week, temp_pref_week, AC_power_usage_week)[0]))

#Basic_AC(outside_temp, indoor_temp_weekend, temp_pref_weekend, AC_power_usage_weekend)[1]
#getCost(power_cost_week, getAC_power(Basic_AC(outside_temp, indoor_temp_week, temp_pref_week, AC_power_usage_week)[0]))

