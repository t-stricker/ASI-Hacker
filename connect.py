#!/usr/bin/env python3.8
from pymodbus.client import ModbusSerialClient as ModbusClient

#import pymodbus
#from pymodbus import ModbusSerialClient
#from pymodbus.payload import BinaryPayloadDecoder
#from pymodbus.constants import Endian
#import six

client = ModbusClient(port='/dev/ttyUSB0', method='rtu', startbits=1, stopbits=1, bytesize=8, parity='N', baudrate=115200)

client.connect()
#print(client)

speed_reg = client.read_holding_registers(address = 124 ,count=1, slave=1)
speed = speed_reg.registers[0]/256
if(speed == 0.0):
	print("lock")
	code = 65535
	print("try code: ", code)
	test_code = client.write_registers(498, code, slave=1)
	print(test_code)

	speed_reg = client.read_holding_registers(address = 124 ,count=1, slave=1)
	print(speed_reg.registers[0]/256)
	if(speed_reg.registers[0]/256 == 0.0):
		print("still lock")

else:
	print("unlock!")

code = client.read_holding_registers(address = 498, count=1, slave=1)
print(code.registers[0])

client.close()


