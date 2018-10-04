import unittest
from tests import mythril_testcases


class LocalTestHandler(object):
    base_uri = 'http://localhost:5000'


class LocalMythrilTests(mythril_testcases.MythrilIntegrationTests,
                        LocalTestHandler):
    pass


if __name__ == '__main__':
    unittest.main(verbosity=4)
