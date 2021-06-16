'''program to calculate packet loss'''
import ast


class Packetloss:
    '''class defined'''
    # pylint: disable=too-many-instance-attributes
    # Twelve is reasonable in this case.
    # pylint: disable=too-many-arguments
    # six is reasonable in this case.

    def __init__(self, file_name, test_time1, sample_rate1, temp_packet_time,
                 battery_packet_time1):

        self.file_name = file_name
        self.test_time1 = test_time1
        self.sample_rate1 = sample_rate1
        self.temp_packet_time = temp_packet_time
        self.battery_packet_time1 = battery_packet_time1
        self.disconnect = 0
        self.connect = 0
        self.acc_count = 0
        self.temp_count = 0
        self.battery_count = 0
        self.connect_time = 0
        self.expected = 0

    def read_file(self):
        ''' function to read file'''
        self.file_name = open(self.file_name)
        flag = 0
        totaldisconnect = 0

        if self.test_time1| self.sample_rate1| self.temp_packet_time| self.battery_packet_time1 < 0:
            raise ValueError('Invalid Input')

        for line in self.file_name:
            data = ast.literal_eval(line)
            if int(data['PID']) == 0:
                self.acc_count = self.acc_count + 1
            elif int(data['PID']) == 1:
                self.temp_count = self.temp_count + 1
            elif int(data['PID']) == 2:
                self.battery_count = self.battery_count + 1
            elif int(data['PID']) == 999:
                self.connect = self.connect + 1
                if flag == 1:
                    timeofconnect = data['TS']
                    totaldisconnect = totaldisconnect + \
                        (timeofconnect - timeofdisconnect)
                    flag = 0
            elif int(data['PID']) == 998:
                self.disconnect = self.disconnect + 1
                if flag == 0:
                    timeofdisconnect = data['TS']
                    flag = 1
        print("number of times its disconnected: ", self.disconnect)
        self.connect_time = self.test_time1 - \
            (totaldisconnect / 60000)
        self.file_name.close()

    def accelerometer_packet_rate(self):
        '''function to calculate accelerometer packet rate per min'''
        sample_time = 1000/self.sample_rate1
        each_packet_time = sample_time * 40
        acc_packet_persec = 1000 / each_packet_time
        acc_packet_rate_permin = acc_packet_persec * 60
        #print(type(acc_packet_rate_permin), acc_packet_rate_permin)
        return acc_packet_rate_permin

    def accelerator_packet_loss(self):
        '''function to calculate accelerometer packet loss percentage '''
        self.expected = self.connect_time * self.accelerometer_packet_rate()
        #self.actual = self.acc_count
        print("Accelerometer packet loss:", self.calculation(
            self.acc_count, self.expected), "%")

    def temperature_packet_loss(self):
        '''function to calculate temperature packet loss percentage '''
        self.expected = self.connect_time/self.temp_packet_time
        #self.actual = self.temp_count
        print("Temperature packet loss:", self.calculation(
            self.temp_count, self.expected), "%")

    def battery_packet_loss(self):
        '''function to calculate battery packet loss percentage '''
        self.expected = self.connect_time/self.battery_packet_time1
        #self.actual = self.battery_count
        print("Battery packet loss:", self.calculation(
            self.battery_count, self.expected), "%")

     # pylint: disable=no-self-use
    def calculation(self, actual, expected):
        '''funtion to calculate packet loss'''
        if expected == 0:
            raise ValueError('Can not divide by zero')
        if(actual < 0 or expected < 0):
            raise ValueError('Can not be negative Number')

        return round(((expected - actual) / (expected)) * 100, 2)


FILE_NAME = input("Enter File name:")
SENSOR_TESTING_TIME = int(input("Enter Total Time in min:"))
SAMPLE_RATE = int(input("Enter sampling rate in Hz :"))
TEMP_PACKET_TIME = int(
    input("Enter time expected for each temperature packet in min :"))
BATTERY_PACKET_TIME = int(
    input("Enter time expected for each Battery packet in min :"))


PACKET_LOSS1 = Packetloss(FILE_NAME, SENSOR_TESTING_TIME,
                          SAMPLE_RATE, TEMP_PACKET_TIME, BATTERY_PACKET_TIME)
PACKET_LOSS1.read_file()
PACKET_LOSS1.accelerator_packet_loss()
PACKET_LOSS1.temperature_packet_loss()
PACKET_LOSS1.battery_packet_loss()
