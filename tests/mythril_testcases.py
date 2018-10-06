import unittest
import requests
import json

bytecode_with_no_issues = '6080604052348015600f57600080fd5b50600160005560358060226000396000f3006080604052600080fd00a165627a7a7230582091fc0b23ac6b63784947c5f7727abf4984fac2d56aa76b382d059119700a816a0029'
bytecode_with_issues = '6060604052341561000c57fe5b5b6102f98061001c6000396000f3006060604052361561004a576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff168063354284f2146100e75780634a3f17e7146100f9575b6100e55b34600060003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008282540192505081905550343373ffffffffffffffffffffffffffffffffffffffff167f115522125a340a348d82c36b243d9dcbb357931a24824ddbe1d13179155e309160405180905060405180910390a35b565b005b34156100ef57fe5b6100f7610143565b005b341561010157fe5b61012d600480803573ffffffffffffffffffffffffffffffffffffffff169060200190919050506102b5565b6040518082815260200191505060405180910390f35b6000635f220d804211801561019757506000600060003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002054115b15156101a35760006000fd5b600060003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000205490506000600060003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020819055503373ffffffffffffffffffffffffffffffffffffffff166108fc829081150290604051809050600060405180830381858888f19350505050151561026a57fe5b803373ffffffffffffffffffffffffffffffffffffffff167f0dc8f43545dbeec87c6f54e44dac2d8889f2a4b3bf0f62683cd7e1c6346128e760405180905060405180910390a35b50565b600060205280600052604060002060009150905054815600a165627a7a72305820ff37ab4aec94c93a993cc8874bf94a6d3d706d3eeb6b5b5df89d7c23a75227310029'


class MythrilTests(unittest.TestCase):
    def test_firing_lasers_using_bytecodes(self):
        payload = {
            'module': 'controllers',
            'file': 'service',
            'method': 'security'
        }

        data = {
            'bytecode': bytecode_with_no_issues
        }
        response = requests.post('%s/ajax' % self.base_uri,
                                 params=payload, json=data)
        content = json.loads(response.content)
        message = content['data']
        self.assertEqual(message, 'The analysis was completed successfully. No issues were detected.\n')

    def test_firing_lasers_has_issues(self):
        payload = {
            'module': 'controllers',
            'file': 'service',
            'method': 'security',
        }

        data = {
            'bytecode': bytecode_with_issues
        }
        response = requests.post('%s/ajax' % self.base_uri,
                                 params=payload, json=data)
        content = json.loads(response.content)
        message = content['data']
        self.assertNotEqual(message, 'The analysis was completed successfully. No issues were detected.')


class MythrilIntegrationTests(MythrilTests):
    pass
