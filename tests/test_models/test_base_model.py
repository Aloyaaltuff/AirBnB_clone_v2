#!/usr/bin/python3
"""
Module for BaseModel unittest
"""
import os
from models.base_model import BaseModel
import unittest


class TestBasemodel(unittest.TestCase):

    """
    Unittest for BaseModel
    """
    def test_save(self):
        """
        save method test
        """
        instanc = BaseModel()

        ins_updated_at = instanc.updated_at

        current_updated_at = instanc.save()

        self.assertNotEqual(ins_updated_at, current_updated_at)

    def test_to_dict(self):
        """
        Test for to_dict method
        """
        instan = BaseModel()

        ins_dict = instan.to_dict()

        self.assertIsInstance(ins_dict, dict)

        self.assertEqual(ins_dict["__class__"], 'BaseModel')
        self.assertEqual(ins_dict['id'], instan.id)
        self.assertEqual(ins_dict['created_at'], instan.created_at.isoformat())
        self.assertEqual(ins_dict["updated_at"], instan.created_at.isoformat())

    def test_str(self):
        """
        string representation test
        """
        instanc = BaseModel()

        self.assertTrue(str(instanc).startswith('[BaseModel]'))

        self.assertIn(str(instanc.__dict__), str(instanc))

        self.assertIn(instanc.id, str(instanc))

    def tearDown(self):
        """
        Tear down for temporary file path
        """
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("tmp.json", "file.json")
        except FileNotFoundError:
            pass

    def setUp(self):
        """
        Setup for temporary file path
        """
        try:
            os.rename("file.json", "tmp.json")
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    unittest.main()
