# -*- coding: utf-8 -*-

from raspyedge import config

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_config(self):
        config.aws_iot_endpoint()


if __name__ == '__main__':
    unittest.main()
