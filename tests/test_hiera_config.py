import unittest
import sys, os

sys.path.insert(1, os.path.dirname(os.path.dirname(__file__)))

fixtures = '%s/fixtures' % os.path.dirname(__file__)

from hierapy import HieraPy

class TestHieraConfig(unittest.TestCase):

    def test_getWithSetOne(self):
        config = HieraPy(fixtures + '/hiera1.yaml', fixtures + '/configdata')
        self.assertEquals(
            {'login': 'username', 'password': 'overridden-password'},
            config.get('user')
        )
        self.assertEquals(
            {'value': 'only-in-set-1'},
            config.get('extra')
        )

    def test_getWithSetTwo(self):
        config = HieraPy(fixtures + '/hiera2.yaml', fixtures + '/configdata')
        self.assertEquals(
            {'login': 'username', 'password': 'password'},
            config.get('user')
        )
        self.assertFalse(config.get('doesnt-exist'))
        self.assertEquals(
            'non-existent-should-return-default',
            config.get('extra', 'non-existent-should-return-default')
        )

if __name__ == '__main__':
    unittest.main()
