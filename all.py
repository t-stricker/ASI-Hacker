from pymodbus.client import ModbusSerialClient as ModbusClient
client = ModbusClient(port='/dev/ttyUSB0', method='rtu', startbits=1, stopbits=1, bytesize=8, parity='N', baudrate=115200)
client.connect()


value = client.read_holding_registers(address=1 ,count=125, slave=1)
print(value.registers)


client.close()
