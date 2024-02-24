# -*- coding: utf-8 -*-
"""
  app_test.py
  Author : Jacek 'Szumak' Kotlarski --<szumak@virthost.pl>
  Created: 24.02.2024, 20:18:34
  
  Purpose: 
"""

from unittest import TestCase

from sanlms.app import SanConfig


class TestSanConfig(TestCase):
    """docstring for TestSanConfig."""

    def setUp(self) -> None:
        self.conf = SanConfig()

    def test_check_errors(self) -> None:
        self.assertFalse(self.conf.errors)


# #[EOF]#######################################################################
