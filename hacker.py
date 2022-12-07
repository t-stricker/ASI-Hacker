
#!/usr/bin/env python3.8
from pymodbus.client import ModbusSerialClient as ModbusClient
client = ModbusClient(port='/dev/ttyUSB0', method='rtu', startbits=1, stopbits=1, bytesize=8, parity='N', baudrate=115200)
client.connect()

code = 0

while code <= 65535:
        code += 1
        print(code)
        client.write_registers(498, code, slave=1)
        #speed_reg = client.read_holding_registers(address = 124 ,count=1, slave=1)
        #speed = speed_reg.registers[0]/256
        diameter = client.read_holding_registers(address = 227 ,count=1, slave=1).registers[0]
        if(diameter == 0):
                print("still locked")
        else:
                print("job done! code: ",code)
                break

client.close()
