import unittest
import requests
import json
import jsonpath
import time
import pytest
from pytest_check import check
from collections import defaultdict
pytest.lang_fails = defaultdict(int)

class Transliteration(unittest.TestCase):
    
      url = "https://revapi.reverieinc.com/"
    
      def test_68_Data_as_Number_for_Malayalam_Language(self):
        time.sleep(3)
        self.payload = "{\"data\": [\n \"123\"],\n\"convertNumber\" :true,\n\"ignoreTaggedEntities\": true,\n\"isBulk\" : false\n}"
        self.headers = {
            'Content-Type': 'application/json',
            'REV-API-KEY': '37c4ef57ed0d9d1803aaf6ff6cc4b7b39c0d2198',
            'REV-APP-ID': 'com.revqa',
            'src_lang': 'en',
            'tgt_lang': 'ml',
            'REV-APPNAME': 'transliteration'
                        }
        response = requests.request("POST", self.url, headers=self.headers, data = self.payload)
        res = response.json()
        print("Uppercase body Test Passed")
        self.assertEqual(response.status_code, 200)
        self.assertEqual((res['responseList'][0]['outString']),['൧൨൩'])
      
      def test_69_Data_as_Number_for_Tamil_Language(self):
        time.sleep(3)
        self.payload = "{\"data\": [\n \"123\"],\n\"convertNumber\" :true,\n\"ignoreTaggedEntities\": true,\n\"isBulk\" : false\n}"
        self.headers = {
            'Content-Type': 'application/json',
            'REV-API-KEY': '37c4ef57ed0d9d1803aaf6ff6cc4b7b39c0d2198',
            'REV-APP-ID': 'com.revqa',
            'src_lang': 'en',
            'tgt_lang': 'ta',
            'REV-APPNAME': 'transliteration'
                        }
        response = requests.request("POST", self.url, headers=self.headers, data = self.payload)
        res = response.json()
        print("Uppercase body Test Passed")
        self.assertEqual(response.status_code, 200)
        self.assertEqual((res['responseList'][0]['outString']),['௧௨௩'])


      
      
        
      
      

if __name__ == '__main__':
    unittest.main()
