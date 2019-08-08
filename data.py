import sys

# import numpy as np

#########################******************** Total Solar Power Generated **************################################

panelPower = 0.370  # Unique variable
numPanels = 3  # Unique variable

### Use a list instead ####
sunAvailable = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0]

totalSolarAvailable = [(sunAvailable[0] * numPanels * panelPower), (sunAvailable[1] * numPanels * panelPower),
                       (sunAvailable[2] * numPanels * panelPower), (sunAvailable[3] * numPanels * panelPower),
                       (sunAvailable[4] * numPanels * panelPower), (sunAvailable[5] * numPanels * panelPower),
                       (sunAvailable[6] * numPanels * panelPower), (sunAvailable[7] * numPanels * panelPower),
                       (sunAvailable[8] * numPanels * panelPower), (sunAvailable[9] * numPanels * panelPower),
                       (sunAvailable[10] * numPanels * panelPower), (sunAvailable[11] * numPanels * panelPower),
                       (sunAvailable[12] * numPanels * panelPower), (sunAvailable[13] * numPanels * panelPower),
                       (sunAvailable[14] * numPanels * panelPower), (sunAvailable[15] * numPanels * panelPower),
                       (sunAvailable[16] * numPanels * panelPower), (sunAvailable[17] * numPanels * panelPower),
                       (sunAvailable[18] * numPanels * panelPower), (sunAvailable[19] * numPanels * panelPower),
                       (sunAvailable[20] * numPanels * panelPower), (sunAvailable[21] * numPanels * panelPower),
                       (sunAvailable[22] * numPanels * panelPower), (sunAvailable[23] * numPanels * panelPower)]

# print(sunAvailable)                                                                                                    #### For debug only
# print(totalSolarAvailable)                                                                                             #### For debug only


#########################******************** Power cost in Dollars **************######################################

powerCostWeek = [.092, .092, .092, .096, .1, .128, .164, .164, .148, .14, .14, .128,
                 .12, .108, .104, .104, .104, .108, .124, .148, .128, .112, .104, .096]

powerCostWeekend = [.092, .092, .096, .096, .092, .096, .108, .108, .116, .112, .108, .104,
                    .096, .092, .092, .092, .096, .1, .112, .128, .116, .104, .096, .092]

print("PowerCostWeek", powerCostWeek)  #### For debug only
print("PowerCostWeekend", powerCostWeekend)  #### For debug only

#########################******************** Total static power used in kilowatts **************#######################
########## Assume 9-5 job with hour long commute

# ?????????????????????????????????????????????????? TO DO LIST ????????????????????????????????????????????????????????#
#                     Create function to dynamically enter customer parameter into list after getting input            #
#                     Those functions should look like isLightweek and isLightWeekend                                  #
# ??????????????????????????????????????????????????????????????????????????????????????????????????????????????????????#

#### ( 0 for not home and 1 for when he is home)
isHomeWeek = [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]

isSleepingWeek = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]

isHomeWeekend = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]

isSleepingWeekend = [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]

isLightWeek = [None] * 24  # Unique variable

isLightWeekend = [None] * 24  # Unique variable

n = 0
while n <= 23:
    if (isHomeWeek[n] == 1) and (isSleepingWeek[n] == 0):
        isLightWeek[n] = 1
    else:
        isLightWeek[n] = 0
    if (isHomeWeek[n] == 1) and (isSleepingWeekend[n] == 0):
        isLightWeekend[n] = 1
    else:
        isLightWeekend[n] = 0
    n = n + 1

print("isHomeWeek", isHomeWeek)  #### For debug only
print("isSleepingWeek", isSleepingWeek)  #### For debug only
print("isHomeWeekend", isHomeWeekend)  #### For debug only
print("isSleepingWeekend", isSleepingWeekend)  #### For debug only
print("isLightWeek", isLightWeek)  #### For debug only
print("isLightWeekend", isLightWeekend)  #### For debug only

# use water heater 2 hours before work, sleep in 2 hours on weekends (3 kWh)

WaterheaterPowerWeek = [0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0]

WaterheaterPowerWeekend = [0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0]

FridgePower = [0, .1, 0, 0, .07, 0, 0, .15, 0, .08, 0, 0, .1, 0, .09, 0, 0, .15, .1, 0, 0, .08, 0, .075]

numLights = 20  # Unique variable
oneLightPower = .06  # Unique variable

LightPowerWeek = [(numLights * isLightWeek[0] * oneLightPower), (numLights * isLightWeek[1] * oneLightPower),
                  (numLights * isLightWeek[2] * oneLightPower), (numLights * isLightWeek[3] * oneLightPower),
                  (numLights * isLightWeek[4] * oneLightPower), (numLights * isLightWeek[5] * oneLightPower),
                  (numLights * isLightWeek[6] * oneLightPower), (numLights * isLightWeek[7] * oneLightPower),
                  (numLights * isLightWeek[8] * oneLightPower), (numLights * isLightWeek[9] * oneLightPower),
                  (numLights * isLightWeek[10] * oneLightPower), (numLights * isLightWeek[11] * oneLightPower),
                  (numLights * isLightWeek[12] * oneLightPower), (numLights * isLightWeek[13] * oneLightPower),
                  (numLights * isLightWeek[14] * oneLightPower), (numLights * isLightWeek[15] * oneLightPower),
                  (numLights * isLightWeek[16] * oneLightPower), (numLights * isLightWeek[17] * oneLightPower),
                  (numLights * isLightWeek[18] * oneLightPower), (numLights * isLightWeek[19] * oneLightPower),
                  (numLights * isLightWeek[20] * oneLightPower), (numLights * isLightWeek[21] * oneLightPower),
                  (numLights * isLightWeek[22] * oneLightPower), (numLights * isLightWeek[23] * oneLightPower)]

LightPowerWeekend = [(numLights * isLightWeekend[0] * oneLightPower), (numLights * isLightWeekend[1] * oneLightPower),
                     (numLights * isLightWeekend[2] * oneLightPower), (numLights * isLightWeekend[3] * oneLightPower),
                     (numLights * isLightWeekend[4] * oneLightPower), (numLights * isLightWeekend[5] * oneLightPower),
                     (numLights * isLightWeekend[6] * oneLightPower), (numLights * isLightWeekend[7] * oneLightPower),
                     (numLights * isLightWeekend[8] * oneLightPower), (numLights * isLightWeekend[9] * oneLightPower),
                     (numLights * isLightWeekend[10] * oneLightPower), (numLights * isLightWeekend[11] * oneLightPower),
                     (numLights * isLightWeekend[12] * oneLightPower), (numLights * isLightWeekend[13] * oneLightPower),
                     (numLights * isLightWeekend[14] * oneLightPower), (numLights * isLightWeekend[15] * oneLightPower),
                     (numLights * isLightWeekend[16] * oneLightPower), (numLights * isLightWeekend[17] * oneLightPower),
                     (numLights * isLightWeekend[18] * oneLightPower), (numLights * isLightWeekend[19] * oneLightPower),
                     (numLights * isLightWeekend[20] * oneLightPower), (numLights * isLightWeekend[21] * oneLightPower),
                     (numLights * isLightWeekend[22] * oneLightPower), (numLights * isLightWeekend[23] * oneLightPower)]

totalStaticPowerUsedWeek = [(WaterheaterPowerWeek[0] + FridgePower[0] + LightPowerWeek[0]),
                            (WaterheaterPowerWeek[1] + FridgePower[1] + LightPowerWeek[1]),
                            (WaterheaterPowerWeek[2] + FridgePower[2] + LightPowerWeek[2]),
                            (WaterheaterPowerWeek[3] + FridgePower[3] + LightPowerWeek[3]),
                            (WaterheaterPowerWeek[4] + FridgePower[4] + LightPowerWeek[4]),
                            (WaterheaterPowerWeek[5] + FridgePower[5] + LightPowerWeek[5]),
                            (WaterheaterPowerWeek[6] + FridgePower[6] + LightPowerWeek[6]),
                            (WaterheaterPowerWeek[7] + FridgePower[7] + LightPowerWeek[7]),
                            (WaterheaterPowerWeek[8] + FridgePower[8] + LightPowerWeek[8]),
                            (WaterheaterPowerWeek[9] + FridgePower[9] + LightPowerWeek[9]),
                            (WaterheaterPowerWeek[10] + FridgePower[10] + LightPowerWeek[10]),
                            (WaterheaterPowerWeek[11] + FridgePower[11] + LightPowerWeek[11]),
                            (WaterheaterPowerWeek[12] + FridgePower[12] + LightPowerWeek[12]),
                            (WaterheaterPowerWeek[13] + FridgePower[13] + LightPowerWeek[13]),
                            (WaterheaterPowerWeek[14] + FridgePower[14] + LightPowerWeek[14]),
                            (WaterheaterPowerWeek[15] + FridgePower[15] + LightPowerWeek[15]),
                            (WaterheaterPowerWeek[16] + FridgePower[16] + LightPowerWeek[16]),
                            (WaterheaterPowerWeek[17] + FridgePower[17] + LightPowerWeek[17]),
                            (WaterheaterPowerWeek[18] + FridgePower[18] + LightPowerWeek[18]),
                            (WaterheaterPowerWeek[19] + FridgePower[19] + LightPowerWeek[19]),
                            (WaterheaterPowerWeek[20] + FridgePower[20] + LightPowerWeek[20]),
                            (WaterheaterPowerWeek[21] + FridgePower[21] + LightPowerWeek[21]),
                            (WaterheaterPowerWeek[22] + FridgePower[22] + LightPowerWeek[22]),
                            (WaterheaterPowerWeek[23] + FridgePower[23] + LightPowerWeek[23])]

totalStaticPowerUsedWeekend = [(WaterheaterPowerWeekend[0] + FridgePower[0] + LightPowerWeekend[0]),
                               (WaterheaterPowerWeekend[1] + FridgePower[1] + LightPowerWeekend[1]),
                               (WaterheaterPowerWeekend[2] + FridgePower[2] + LightPowerWeekend[2]),
                               (WaterheaterPowerWeekend[3] + FridgePower[3] + LightPowerWeekend[3]),
                               (WaterheaterPowerWeekend[4] + FridgePower[4] + LightPowerWeekend[4]),
                               (WaterheaterPowerWeekend[5] + FridgePower[5] + LightPowerWeekend[5]),
                               (WaterheaterPowerWeekend[6] + FridgePower[6] + LightPowerWeekend[6]),
                               (WaterheaterPowerWeekend[7] + FridgePower[7] + LightPowerWeekend[7]),
                               (WaterheaterPowerWeekend[8] + FridgePower[8] + LightPowerWeekend[8]),
                               (WaterheaterPowerWeekend[9] + FridgePower[9] + LightPowerWeekend[9]),
                               (WaterheaterPowerWeekend[10] + FridgePower[10] + LightPowerWeekend[10]),
                               (WaterheaterPowerWeekend[11] + FridgePower[11] + LightPowerWeekend[11]),
                               (WaterheaterPowerWeekend[12] + FridgePower[12] + LightPowerWeekend[12]),
                               (WaterheaterPowerWeekend[13] + FridgePower[13] + LightPowerWeekend[13]),
                               (WaterheaterPowerWeekend[14] + FridgePower[14] + LightPowerWeekend[14]),
                               (WaterheaterPowerWeekend[15] + FridgePower[15] + LightPowerWeekend[15]),
                               (WaterheaterPowerWeekend[16] + FridgePower[16] + LightPowerWeekend[16]),
                               (WaterheaterPowerWeekend[17] + FridgePower[17] + LightPowerWeekend[17]),
                               (WaterheaterPowerWeekend[18] + FridgePower[18] + LightPowerWeekend[18]),
                               (WaterheaterPowerWeekend[19] + FridgePower[19] + LightPowerWeekend[19]),
                               (WaterheaterPowerWeekend[20] + FridgePower[20] + LightPowerWeekend[20]),
                               (WaterheaterPowerWeekend[21] + FridgePower[21] + LightPowerWeekend[21]),
                               (WaterheaterPowerWeekend[22] + FridgePower[22] + LightPowerWeekend[22]),
                               (WaterheaterPowerWeekend[23] + FridgePower[23] + LightPowerWeekend[23])]

print("WaterheaterPowerWeek", WaterheaterPowerWeek)
print("WaterheaterPowerWeekend", WaterheaterPowerWeekend)
print("FridgePower", FridgePower)  #### For debug only
print("LightPowerWeek", LightPowerWeek)  #### For Debug only
print("LightPowerWeekend", LightPowerWeekend)  #### For debug only
print("totalStaticPowerUsedWeek", totalStaticPowerUsedWeek)  #### For debug only
print("totalStaticPowerUsedWeekend", totalStaticPowerUsedWeekend)  #### For debug only

#########################******************** Temperature Preference **************#####################################
########## Assume 9-5 job and home 6-8

# ?????????????????????????????????????????????????? TO DO LIST ????????????????????????????????????????????????????????#
#                                 #
#                                                        #
# ??????????????????????????????????????????????????????????????????????????????????????????????????????????????????????#

# Temperature
outsideTemp = 75  # Unique variable
indoorTemp = 70  # Unique variable
sleepingTemp = 68  # Unique variable

# Preferred temperature inside
tempPrefSimple0 = [indoorTemp, indoorTemp, indoorTemp, indoorTemp, indoorTemp, indoorTemp, indoorTemp,
                   indoorTemp, indoorTemp, indoorTemp, indoorTemp, indoorTemp, indoorTemp, indoorTemp,
                   indoorTemp, indoorTemp, indoorTemp, indoorTemp, indoorTemp, indoorTemp, indoorTemp,
                   indoorTemp, indoorTemp,
                   indoorTemp]

tempPrefWeek1 = [None] * 95
tempPrefWeekend1 = [None] * 95
i = 0
while i <= 23:
    if isSleepingWeek[i] == 1:
        tempPrefWeek1[i] = sleepingTemp
    elif (isSleepingWeek[i] == 0) and (isHomeWeek[i] == 1):
        tempPrefWeek1[i] = indoorTemp
    else:
        tempPrefWeek1[i] = outsideTemp
    if isSleepingWeekend[i] == 1:
        tempPrefWeekend1[i] = sleepingTemp
    elif (isSleepingWeekend[i] == 0) and (isHomeWeekend[i] == 1):
        tempPrefWeekend1[i] = indoorTemp
    else:
        tempPrefWeekend1[i] = outsideTemp
    i = i + 1

print("tempPrefSimple0", tempPrefSimple0)  #### For debug only
print("tempPrefWeek1", tempPrefWeek1)  #### For debug only
print("tempPrefWeekend1", tempPrefWeekend1)  #### For debug only

tempPrefSimple = [None] * 95
tempPrefWeek = [None] * 95
tempPrefWeekend = [None] * 95

# AC power consumption
acPowerWeek = [0, .1, 0, 0, .07, 0, 0, .15, 0, .08, 0, 0, .1, 0, .09, 0, 0, .15, .1, 0, 0, .08, 0, .075]
acPowerWeekend = [0, .1, 0, 0, .07, 0, 0, .15, 0, .08, 0, 0, .1, 0, .09, 0, 0, .15, .1, 0, 0, .08, 0, .075]

# y = 0
# while y <= 90:       #check every 15 minutes
#     tempPrefWeek[y] = tempPrefWeek1[int(y/4)]
#     tempPrefWeekend[y] = tempPrefWeekend1[int(y/4)]
#     tempPrefSimple[y] = tempPrefSimple0[int(y/4)]
#
#     y = y + 1
#
# print("tempPrefWeek", tempPrefWeek[y])                                                                                  #### For debug only
# print("tempPrefWeekend", tempPrefWeekend[y])                                                                            #### For debug only
# print("tempPrefSimple", tempPrefSimple[y])                                                                              #### For debug only


#########################******************** Car Charger data **************###########################################

# ?????????????????????????????????????????????????? TO DO LIST ????????????????????????????????????????????????????????#
#                                                                                                                       #
#                                                                                                                       #
# ??????????????????????????????????????????????????????????????????????????????????????????????????????????????????????#

# Car charger power consumption
carChargerPowerWeek = [0, .1, 0, 0, .07, 0, 0, .15, 0, .08, 0, 0, .1, 0, .09, 0, 0, .15, .1, 0, 0, .08, 0, .075]
carChargerPowerWeekend = [0, .1, 0, 0, .07, 0, 0, .15, 0, .08, 0, 0, .1, 0, .09, 0, 0, .15, .1, 0, 0, .08, 0, .075]

#########################******************** Returned data **************##############################################

# ?????????????????????????????????????????????????? TO DO LIST ????????????????????????????????????????????????????????#
#                                                                                                                       #
#                                                                                                                       #
# ??????????????????????????????????????????????????????????????????????????????????????????????????????????????????????#

totalPowerConsumedWeek = [totalStaticPowerUsedWeek[0] + acPowerWeek[0] + carChargerPowerWeek[0],
                          totalStaticPowerUsedWeek[1] + acPowerWeek[1] + carChargerPowerWeek[1],
                          totalStaticPowerUsedWeek[2] + acPowerWeek[2] + carChargerPowerWeek[2],
                          totalStaticPowerUsedWeek[3] + acPowerWeek[3] + carChargerPowerWeek[3],
                          totalStaticPowerUsedWeek[4] + acPowerWeek[4] + carChargerPowerWeek[4],
                          totalStaticPowerUsedWeek[5] + acPowerWeek[5] + carChargerPowerWeek[5],
                          totalStaticPowerUsedWeek[6] + acPowerWeek[6] + carChargerPowerWeek[6],
                          totalStaticPowerUsedWeek[7] + acPowerWeek[7] + carChargerPowerWeek[7],
                          totalStaticPowerUsedWeek[8] + acPowerWeek[8] + carChargerPowerWeek[8],
                          totalStaticPowerUsedWeek[9] + acPowerWeek[9] + carChargerPowerWeek[9],
                          totalStaticPowerUsedWeek[10] + acPowerWeek[10] + carChargerPowerWeek[10],
                          totalStaticPowerUsedWeek[11] + acPowerWeek[11] + carChargerPowerWeek[11],
                          totalStaticPowerUsedWeek[12] + acPowerWeek[12] + carChargerPowerWeek[12],
                          totalStaticPowerUsedWeek[13] + acPowerWeek[13] + carChargerPowerWeek[13],
                          totalStaticPowerUsedWeek[14] + acPowerWeek[14] + carChargerPowerWeek[14],
                          totalStaticPowerUsedWeek[15] + acPowerWeek[15] + carChargerPowerWeek[15],
                          totalStaticPowerUsedWeek[16] + acPowerWeek[16] + carChargerPowerWeek[16],
                          totalStaticPowerUsedWeek[17] + acPowerWeek[17] + carChargerPowerWeek[17],
                          totalStaticPowerUsedWeek[18] + acPowerWeek[18] + carChargerPowerWeek[18],
                          totalStaticPowerUsedWeek[19] + acPowerWeek[19] + carChargerPowerWeek[19],
                          totalStaticPowerUsedWeek[20] + acPowerWeek[20] + carChargerPowerWeek[20],
                          totalStaticPowerUsedWeek[21] + acPowerWeek[21] + carChargerPowerWeek[21],
                          totalStaticPowerUsedWeek[22] + acPowerWeek[22] + carChargerPowerWeek[22],
                          totalStaticPowerUsedWeek[23] + acPowerWeek[23] + carChargerPowerWeek[23]]

totalPowerConsumedWeekend = [totalStaticPowerUsedWeekend[0] + acPowerWeekend[0] + carChargerPowerWeekend[0],
                             totalStaticPowerUsedWeekend[1] + acPowerWeekend[1] + carChargerPowerWeekend[1],
                             totalStaticPowerUsedWeekend[2] + acPowerWeekend[2] + carChargerPowerWeekend[2],
                             totalStaticPowerUsedWeekend[3] + acPowerWeekend[3] + carChargerPowerWeekend[3],
                             totalStaticPowerUsedWeekend[4] + acPowerWeekend[4] + carChargerPowerWeekend[4],
                             totalStaticPowerUsedWeekend[5] + acPowerWeekend[5] + carChargerPowerWeekend[5],
                             totalStaticPowerUsedWeekend[6] + acPowerWeekend[6] + carChargerPowerWeekend[6],
                             totalStaticPowerUsedWeekend[7] + acPowerWeekend[7] + carChargerPowerWeekend[7],
                             totalStaticPowerUsedWeekend[8] + acPowerWeekend[8] + carChargerPowerWeekend[8],
                             totalStaticPowerUsedWeekend[9] + acPowerWeekend[9] + carChargerPowerWeekend[9],
                             totalStaticPowerUsedWeekend[10] + acPowerWeekend[10] + carChargerPowerWeekend[10],
                             totalStaticPowerUsedWeekend[11] + acPowerWeekend[11] + carChargerPowerWeekend[11],
                             totalStaticPowerUsedWeekend[12] + acPowerWeekend[12] + carChargerPowerWeekend[12],
                             totalStaticPowerUsedWeekend[13] + acPowerWeekend[13] + carChargerPowerWeekend[13],
                             totalStaticPowerUsedWeekend[14] + acPowerWeekend[14] + carChargerPowerWeekend[14],
                             totalStaticPowerUsedWeekend[15] + acPowerWeekend[15] + carChargerPowerWeekend[15],
                             totalStaticPowerUsedWeekend[16] + acPowerWeekend[16] + carChargerPowerWeekend[16],
                             totalStaticPowerUsedWeekend[17] + acPowerWeekend[17] + carChargerPowerWeekend[17],
                             totalStaticPowerUsedWeekend[18] + acPowerWeekend[18] + carChargerPowerWeekend[18],
                             totalStaticPowerUsedWeekend[19] + acPowerWeekend[19] + carChargerPowerWeekend[19],
                             totalStaticPowerUsedWeekend[20] + acPowerWeekend[20] + carChargerPowerWeekend[20],
                             totalStaticPowerUsedWeekend[21] + acPowerWeekend[21] + carChargerPowerWeekend[21],
                             totalStaticPowerUsedWeekend[22] + acPowerWeekend[22] + carChargerPowerWeekend[22],
                             totalStaticPowerUsedWeekend[23] + acPowerWeekend[23] + carChargerPowerWeekend[23]]

creditGeneratedWeek = [None] * 24
creditGeneratedWeekend = [None] * 24
energyToBuyWeek = [None] * 24
energyToBuyWeekend = [None] * 24


print("totalPowerConsumedWeek", totalPowerConsumedWeek)                                                                 #### For debug only
print("totalPowerConsumedWeekend", totalPowerConsumedWeekend)                                                           #### For debug only
