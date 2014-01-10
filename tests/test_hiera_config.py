import sys, os
from chai import Chai
from hierapy import HieraPy

sys.path.insert(1, os.path.dirname(os.path.dirname(__file__)))


single_config = {
    ':hierarchy': ['base'],
}
overriden_config = {
    ':hierarchy': ['override', 'base'],
}
config_base = {
    'login': 'username',
    'password': 'secret',
}
config_override = {
    'login': 'username',
    'password': 'overridden',
    'extra': 'extra-value',
}

class TestHieraConfig(Chai):

    def test_getWithSingleConfig(self):
        loader = mock()
        expect(loader).args('single.yaml').returns(single_config)
        expect(loader).args('folder/base.yaml').returns(config_base)

        config = HieraPy('single.yaml', 'folder')
        config._HieraPy__load = loader

        assert_equals('username', config.get('login'))
        assert_equals('secret', config.get('password'))
        assert_false(config.get('extra'))

    def test_getWithOverriddenConfig(self):
        loader = mock()
        expect(loader).args('overriden.yaml').returns(overriden_config)
        expect(loader).args('folder/base.yaml').returns(config_base)
        expect(loader).args('folder/override.yaml').returns(config_override)

        config = HieraPy('overriden.yaml', 'folder')
        config._HieraPy__load = loader

        assert_equals('username', config.get('login'))
        assert_equals('overridden', config.get('password'))
        assert_equals('extra-value', config.get('extra'))

    def test_getGetDefaultValues(self):
        loader = mock()
        expect(loader).args('single.yaml').returns(single_config)
        expect(loader).args('folder/base.yaml').returns(config_base)

        config = HieraPy('single.yaml', 'folder')
        config._HieraPy__load = loader

        assert_false(config.get('non-existent'))
        assert_equals('expected-default', config.get('non-existent', 'expected-default'))

if __name__ == '__main__':
    import unittest2
    unittest2.main()
