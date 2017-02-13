import unittest
import linkcheck


class TestLinkCheck(unittest.TestCase):
	def test_good_link(self):
		"""
		Good links should not return any output
		"""
		results = linkcheck.check_links(['http://www.google.com'])
		self.assertEqual(len(results), 0, "There were unexpected failures")

	def test_bad_link(self):
		"""
		A bad link is any link that does not start with http/https
		"""
		results = linkcheck.check_links(['hdfafdsafsaflsadfjl;ka'])
		self.assertEqual(len(results), 1, "There were more/less failures than expected")

	def test_nonexistent_link(self):
		"""
		A well-formed link that should not exist
		"""
		results = linkcheck.check_links(['http://wafjeiaofjeafewaiof.com'])
		self.assertEqual(len(results), 1, "There were more/less failures than expected")

	def test_string_input(self):
		"""
		Can accept a list or a str
		"""
		results = linkcheck.check_links("http://www.cnn.com")
		self.assertEqual(len(results), 0, "There were unexpected failures")

	def test_bad_input(self):
		with self.assertRaises(ValueError):
			linkcheck.check_links(0)

if __name__ == "__main__":
	unittest.main()
