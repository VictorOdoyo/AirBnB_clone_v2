#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
from models.base_model import BaseModel
from datetime import datetime
from unittest.mock import patch
from time import sleep
from os import getenv
import pycodestyle
import inspect
import unittest
storage_t = getenv("HBNB_TYPE_STORAGE")

class test_Amenity(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)


class Test_PEP8(unittest.TestCase):
    """test User"""
    def test_pep8_user(self):
        """test pep8 style"""
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class test_inherit_basemodel(unittest.TestCase):
    """Test if user inherit from BaseModel"""
    def test_instance(self):
        """check if user is an instance of BaseModel"""
        user = Amenity()
        self.assertIsInstance(user, Amenity)
        self.assertTrue(issubclass(type(user), BaseModel))
        self.assertEqual(str(type(user)), "<class 'models.amenity.Amenity'>")


class test_Amenity_BaseModel(unittest.TestCase):
    """Testing user class"""
    def test_instances(self):
        with patch('models.amenity'):
            instance = Amenity()
            self.assertEqual(type(instance), Amenity)
            instance.name = "Barbie"
            expectec_attrs_types = {
                    "id": str,
                    "created_at": datetime,
                    "updated_at": datetime,
                    "name": str,
                    }
            inst_dict = instance.to_dict()
            expected_dict_attrs = [
                    "id",
                    "created_at",
                    "updated_at",
                    "name",
                    "__class__"
                    ]
            self.assertCountEqual(inst_dict.keys(), expected_dict_attrs)
            self.assertEqual(inst_dict['name'], 'Barbie')
            self.assertEqual(inst_dict['__class__'], 'Amenity')

            for attr, types in expectec_attrs_types.items():
                with self.subTest(attr=attr, typ=types):
                    self.assertIn(attr, instance.__dict__)
                    self.assertIs(type(instance.__dict__[attr]), types)
            self.assertEqual(instance.name, "Barbie")

    def test_user_id_and_createat(self):
        """testing id for every user"""
        user_1 = Amenity()
        sleep(2)
        user_2 = Amenity()
        sleep(2)
        user_3 = Amenity()
        sleep(2)
        list_users = [user_1, user_2, user_3]
        for instance in list_users:
            user_id = instance.id
            with self.subTest(user_id=user_id):
                self.assertIs(type(user_id), str)
        self.assertNotEqual(user_1.id, user_2.id)
        self.assertNotEqual(user_1.id, user_3.id)
        self.assertNotEqual(user_2.id, user_3.id)
        self.assertTrue(user_1.created_at <= user_2.created_at)
        self.assertTrue(user_2.created_at <= user_3.created_at)
        self.assertNotEqual(user_1.created_at, user_2.created_at)
        self.assertNotEqual(user_1.created_at, user_3.created_at)
        self.assertNotEqual(user_3.created_at, user_2.created_at)

    def test_str_method(self):
        """
        Testin str magic method

