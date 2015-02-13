# encoding: utf-8

import unittest
from workflow import web
from lipsum import BASE_URL


class LipsumTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_request_should_return_status_code_200(self):
        response = web.get(BASE_URL)
        self.assertEqual(
            response.status_code,
            200
        )
