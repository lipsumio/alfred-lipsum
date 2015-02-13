# encoding: utf-8

import unittest
from workflow import web


TARGET_URL = "http://lipsum.com/feed/json?what=paras&amount=1&start=no"


class LipsumTest(unittest.TestCase):
    def setUp(self):
        self.response = web.get(TARGET_URL)

    def test_request_should_return_status_code_200(self):
        self.assertEqual(
            self.response.status_code,
            200
        )

    def test_request_should_return_valid_json(self):
        # {
        #   "feed": {
        #     "lipsum": "Sed enim nibh, eleifend quis orci non ..."
        #     "generated":
        #       "Generated 1 paragraph, 132 words, 859 bytes of Lorem Ipsum",
        #     "donatelink": "http://www.lipsum.com/donate",
        #     "creditlink": "http://www.lipsum.com/",
        #     "creditname": "James Wilson"
        #   }
        # }

        result = self.response.json()
        self.assertTrue(
            "feed" in result
            and "lipsum" in result["feed"]
            and "generated" in result["feed"]
        )
