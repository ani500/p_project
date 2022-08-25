import unittest
from tests.Home.fangate_test import CreateFangateTests
from tests.Spotify_growth.ad_test import AdTests

tc1 = unittest.TestLoader().loadTestsFromTestCase(CreateFangateTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(AdTests)

test = unittest.TestSuite([tc1,tc2])

unittest.TextTestRunner(verbosity=2).run(test)



