'Unit test Program for packet loss'
import unittest
from code_packet import Packetloss


class Testpacketloss(unittest.TestCase):
    "Class defined for Unit test"

    def setUp(self):
        self.packet_loss1 = Packetloss(
            r'C:\Users\ksame\Downloads\FBE963FC6C39_vSens_PackeIDLog.txt', 2500, 200, 5, 5)
        self.packet_loss1.read_file()
        self.packet_loss2 = Packetloss(
            r'C:\Users\ksame\Downloads\EB44310BFD3A_vSens_PackeIDLog (1).txt', 2500, -200, 5, -5)
        with self.assertRaises(ValueError):
            self.packet_loss2.read_file()

    def tearDown(self):
        pass

    def test_read_file(self):
        "Test fun for read file"
        self.assertEqual(self.packet_loss1.acc_count, 716475)
        self.assertEqual(self.packet_loss1.temp_count, 472)
        self.assertEqual(self.packet_loss1.battery_count, 472)
        self.assertEqual(self.packet_loss1.connect, 4)
        self.assertEqual(self.packet_loss1.disconnect, 1)
        self.assertEqual(self.packet_loss1.connect_time, 2492.20875)

    def test_accelerometer_packet_rate(self):
        "Test fun for accelerometer packate rate "
        self.assertEqual(self.packet_loss1.accelerometer_packet_rate(), 300.0)

    def test_accelerator_packet_loss(self):
        "Test fun for accelerometer packate loss"
        self.packet_loss1.accelerator_packet_loss()
        self.assertEqual(self.packet_loss1.expected, 747662.6249999999)

    def test_temperature_packet_loss(self):
        "Test fun for temperature packate loss"
        self.packet_loss1.temperature_packet_loss()
        self.assertEqual(self.packet_loss1.expected, 498.44174999999996)

    def test_battery_packet_loss(self):
        "Test fun for battery packate loss"
        self.packet_loss1.battery_packet_loss()
        self.assertEqual(self.packet_loss1.expected, 498.44174999999996)

    def test_calculation(self):
        "Test fun for calculation"
        self.assertEqual(self.packet_loss1.calculation(
            716475, 747662.6249999999), 4.17)
        self.assertEqual(self.packet_loss1.calculation(
            472, 498.44174999999996), 5.3)
        self.assertEqual(self.packet_loss1.calculation(
            472, 498.44174999999996), 5.3)

        with self.assertRaises(ValueError):
            self.packet_loss1.calculation(716475, 0)

        with self.assertRaises(ValueError):
            self.packet_loss1.calculation(-716475, 7476)


if __name__ == '__main__':
    unittest.main()
