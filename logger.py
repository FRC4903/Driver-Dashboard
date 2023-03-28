from networktables import NetworkTables
import json

# To see messages from networktables, you must setup logging
import logging

logging.basicConfig(level=logging.DEBUG)

ip = '10.49.3.2'

NetworkTables.initialize(server=ip)

table = NetworkTables.getTable("SmartDashboard")

while True:

    print(table.getNumber('colorState', 0))

    arm = {
        'arm1Angle': table.getNumber('arm1Angle', 0),
        'arm2Angle': table.getNumber('arm2Angle', 0)
    }
    balance = {
        'balanceAngle': table.getNumber('balanceAngle', 0)
    }
    LED = {
        'colorState': table.getNumber('colorState', 0)
    }
    swerve = {
        'FLAngle': table.getNumber('FLCC',0),
        'FRAngle': table.getNumber('FRCC', 0),
        'BLAngle': table.getNumber('BLCC', 0),
        'BRAngle': table.getNumber('BRCC', 0),
        'FLPow': table.getNumber('FLWM', 0),
        'FRPow': table.getNumber('FRWM', 0),
        'BLPow': table.getNumber('BLWM', 0),
        'BRPow': table.getNumber('BRWM', 0)
    }

    json_object = json.dumps(arm, indent=4)
    
    with open("NetworkTables/arm.json", "w") as outfile:
        outfile.write(json_object)

    json_object = json.dumps(balance, indent=4)
    
    with open("NetworkTables/balance.json", "w") as outfile:
        outfile.write(json_object)

    json_object = json.dumps(LED, indent=4)
    
    with open("NetworkTables/LED.json", "w") as outfile:
        outfile.write(json_object)
    
    json_object = json.dumps(swerve, indent=4)
    
    with open("NetworkTables/swerve.json", "w") as outfile:
        outfile.write(json_object)