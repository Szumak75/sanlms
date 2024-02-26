# -*- coding: utf-8 -*-
"""
  routes_test.py
  Author : Jacek 'Szumak' Kotlarski --<szumak@virthost.pl>
  Created: 25.02.2024, 10:05:14
  
  Purpose: 
"""

import unittest

from flask import Flask

from sanlms.routes import app


class RoutesTest(unittest.TestCase):
    """docstring for RoutesTest."""

    def test_01_app_object(self) -> None:
        self.assertIsNotNone(app)
        self.assertTrue(isinstance(app, Flask))

    def test_02_index(self) -> None:
        if app:
            tester = app.test_client()
            response = tester.get("/hello", content_type="html/text")

            self.assertTrue(response.status_code == 200)
            self.assertTrue(response.data == b"Hello, World!")


# #[EOF]#######################################################################
