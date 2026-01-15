def traffic_light_signal(currentSignal,isEmergencyVehicleApproach):
    if isEmergencyVehicleApproach==True:
        return "IMMEDIATE GREEN"
    
    if currentSignal=="RED":
        return "STOP"
    elif currentSignal=="YELLOW":
        return "PREPARE TO STOP"
    elif currentSignal=="GREEN":
        return "GO"
    else:
        return "INVALID SIGNAL"

print(traffic_light_signal("RED",False))
print(traffic_light_signal("RED",True))
print(traffic_light_signal("YELLOW",False))
print(traffic_light_signal("GREEN",True))
print(traffic_light_signal("ERR",True))
   