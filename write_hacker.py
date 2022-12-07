
#!/usr/bin/env python3.8
from pymodbus.client import ModbusSerialClient as ModbusClient
client = ModbusClient(port='/dev/ttyUSB0', method='rtu', startbits=1, stopbits=1, bytesize=8, parity='N', baudrate=115200)
client.connect()

read_code = 8546
client.write_registers(read_code, read_code, slave=1)

code = 0
while code <= 65535:
        code += 1
        print(code)
        client.write_registers(130, code, slave=1)
        #227 = Diameter setting is 518.0 default  set to 100
        client.write_registers(227, 100, slave=1)
        diameter = client.read_holding_registers(address = 227 ,count=1, slave=1).registers[0]
        if(diameter == 100):
                print("job done! code: ",code)
                break
        else:
                print("write mode: still locked, diameter: ", diameter)

client.close()
