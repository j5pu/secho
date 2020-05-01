#!/usr/bin/env python

"""Tests for `secho` package."""

colors = ['black', 'red', 'green', 'yellow', 'cyan', 'white', 'bblack', 'bred', 'bgreen', 'byellow', 'bblue', 'bmagenta', 'bcyan', 'bwhite', 'reset']
modes = ['bold', 'underline', 'underline', 'blink']
import unittest
import secho
from secho import *
red()

class TestSecho(unittest.TestCase):
    """Tests for `secho` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""
        for color in colors:
            getattr(secho, color)(color)
            for var1 in [True, False]:
                for var2 in [True, False]:
                    for var3 in [True, False]:
                        getattr(secho, color)(f'{color}', bold=var1, underline=var2, blink=var3)



