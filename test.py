# -*- coding: utf-8 -*-
import unittest
from pypromptpay import qr_code
class TestUM(unittest.TestCase):
    def test_qrcode(self):
        self.assertIsNotNone(qr_code(account="0000000000000",one_time=True,path_qr_code="",country="TH",money="",currency="THB"))
