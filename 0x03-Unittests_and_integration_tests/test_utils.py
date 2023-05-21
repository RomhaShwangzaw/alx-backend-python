#!/usr/bin/env python3
"""Unittest Module"""

import unittest
from parameterized import parameterized
from typing import Dict, Tuple, Union
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """A Test Class for utils.access_nested_map function"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map: Dict, path: Tuple[str],
                               expected: Union[Dict, int]) -> None:
        """method to test utils.access_nested_map function"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map: Dict,
                                         path: Tuple[str]) -> None:
        """
        method to test wrong input for
        utils.access_nested_map function
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)
