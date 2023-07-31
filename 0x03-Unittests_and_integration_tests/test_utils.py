#!/usr/bin/env python3
"""Unittests for utils.access_nested_map
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Test class"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self, nested_map,
                                         path, expected_exception_message):
        """Test exception"""
        with self.assertRaises(expected_exception_message) as context:
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Test class for get_json function"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch("utils.requests.get")
    def test_get_json(self, test_url, test_payload, mock_requests_get):
        """tests for get_json ftn"""
        mock_response = mock_requests_get.return_value
        mock_response.json.return_value = test_payload

        result = get_json(test_url)

        mock_requests_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


class TestClass:
    """Test class"""
    def a_method(self):
        return 42

    @memoize
    def a_property(self):
        return self.a_method()


class TestMemoize(unittest.TestCase):
    """Test class for memoize decorator"""

    def test_memoize(self):
        # Create an instance of TestClass
        test_instance = TestClass()

        # Patch a_method in the TestClass instance
        with patch.object(TestClass, 'a_method') as mock_a_method:
            # Set the return value of a_method to 42
            mock_a_method.return_value = 42

            # Call a_property twice
            result1 = test_instance.a_property
            result2 = test_instance.a_property

            # Assert that a_method was only called once
            mock_a_method.assert_called_once()

            # Assert that the results are correct
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)


if __name__ == '__main__':
    unittest.main()
