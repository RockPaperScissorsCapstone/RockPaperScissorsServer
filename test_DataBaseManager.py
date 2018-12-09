import unittest
from DataBaseManager import DBManager
dbm = DBManager()

class DatabaseManagerTestCase(unittest.TestCase):
	def test_getPlayerIDFromUserName(self):
		self.assertNotEqual(dbm.updateCurrency(["15", "17"]), "0")

if __name__ == '__main__':
	unittest.main()