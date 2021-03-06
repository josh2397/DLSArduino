from instructions import Instructions
import serial
import serial.tools.list_ports as port_list
import time
import sys

class SerialConnection:


    def __init__(self, port):

        """ Sets up the serial connection with the specified configuration.

            :param: port - the name of the port to be used within the serial configuration.

        """

        self.ser = serial.Serial(port=port.upper(), baudrate=9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_ODD, stopbits=serial.STOPBITS_TWO, xonxoff=False, timeout=200)

    def connectionTest(self):

        """ Sends two characters to the tiva and waits to receive them back to ensure that communication is ready to begin running the program.

        """

        print("Turn on the Tiva")
        g_byte = self.ser.read(1)
        o_byte = self.ser.read(1)

        if (g_byte.decode("ascii") != "G") | (o_byte.decode("ascii") != "O"):
            print("Unsuccessful Serial Connection to Tiva, Try Again")
        else:
            print("Successful Serial Connection to Tiva")

    def sendInstruction(self, instruction):
        # instruction = '!'
        """
            Send a single ascii character to inform the tiva of what task is should execute.

            :param: instruction - the instruction character to be sent to the tiva.
        """
        print(f'Sending: {instruction}')
        self.ser.write(instruction.encode("ascii"))
        self.ser.write('\n'.encode("ascii"))

        self.ser.reset_input_buffer()

        ser_bytes = self.ser.read(1)
        print(f'Receiving\nraw data: {ser_bytes}')

        # decoded_bytes = (ser_bytes.decode("ascii"))
        # print(f'Ascii Value: {decoded_bytes}', flush=True)

    def sendValue(self, value):

        """ Sends a value associated with an instruction.

            :param: value - The raw value to be sent to the tiva.
        """

        print(f'Sending: {value}\n')
        self.ser.write(bytes([value]))
        self.ser.write('\n'.encode("ascii"))

        self.ser.reset_input_buffer()
        ser_bytes = self.ser.read(1)
        print(f'Receiving\nraw data: {ser_bytes}')


        #decoded_bytes = (ser_bytes.decode("ascii"))

        #print(f'Ascii Value: {decoded_bytes}', flush=True)

    def readSample(self):

        """ Waits to receive samples from the Tiva and combines bytes from separated writes

            :return: combined bytes for whole sample value.
        """
        ser_bytes_sample1 = self.ser.read(1)
        print(f'byte 1: {ser_bytes_sample1}')
        ser_bytes_sample2 = self.ser.read(1)
        print(f'byte 1: {ser_bytes_sample2}')

        ser_bytes_total = int.from_bytes(ser_bytes_sample1, byteorder='little', signed=False) + (int.from_bytes(ser_bytes_sample2, byteorder='little', signed=False) << 8)

        return ser_bytes_total

    def readTime(self):
        ser_bytes_lower = self.ser.read(1)
        ser_bytes_mid = self.ser.read(1)
        ser_bytes_upper = self.ser.read(1)
        
        ser_bytes_total = int.from_bytes(ser_bytes_lower, byteorder='little', signed=False) + (int.from_bytes(ser_bytes_mid, byteorder='little', signed=False) << 8) + (int.from_bytes(ser_bytes_upper, byteorder='little', signed=False) << 16)
        return ser_bytes_total/1000

    def sendStopInstruction(self, instruction):

        """ Sends an '!' character so the Tiva will interrupt and stop running any task that's currently executing.

            :param: '!' instruction sent by the Stop Button handleStop function.
        """

        print(f'Sending: {instruction}\n')
        self.ser.write(instruction.encode("ascii"))
        self.ser.write('\n'.encode("ascii"))

        self.ser.reset_input_buffer()
        ser_bytes = self.ser.read(1)
        print(ser_bytes)
