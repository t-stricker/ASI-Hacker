from pymodbus.client import ModbusSerialClient as ModbusClient
client = ModbusClient(port='/dev/ttyUSB0', method='rtu', startbits=1, stopbits=1, bytesize=8, parity='N', baudrate=115200)
client.connect()

adress = 227
scale = 1
value = client.read_holding_registers(address = adress ,count=1, slave=1).registers[0]/scale
print(value)

code=8546
client.write_registers(498, code, slave=1)

client.close()
