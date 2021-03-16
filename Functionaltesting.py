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
    
    def test_1_statuscode(self):
        time.sleep(3)
        self.payload = "{\"data\": [\n \"is this www.url2221.com\"],\n\"isBulk\" :false,\n\"contentLanguage\" : \"en\",\n\"ignoreTaggedEntities\" : true\n}"
        self.headers = {
                     'Content-Type': 'application/json',
                     'REV-API-KEY': '37c4ef57ed0d9d1803aaf6ff6cc4b7b39c0d2198',
                     'REV-APP-ID': 'com.revqa',
                     'src_lang': 'en',
                     'tgt_lang': 'hi',
                     'REV-APPNAME': 'transliteration'
                    }
        self.response = requests.request("POST", self.url, headers=self.headers, data = self.payload)
        self.assertEqual(self.response.status_code, 200)
        print("Status Code 200")
        

    def test_2_without_Contenttype(self):
        time.sleep(3)
        self.payload = "{\"data\": [\n \"is this www.url2221.com\"],\n\"isBulk\" :false,\n\"contentLanguage\" : \"en\",\n\"ignoreTaggedEntities\" : true\n}"
        self.headers = {
                     'REV-API-KEY': '37c4ef57ed0d9d1803aaf6ff6cc4b7b39c0d2198',
                     'REV-APP-ID': 'com.revqa',
                     'src_lang': 'en',
                     'tgt_lang': 'hi',
                     'REV-APPNAME': 'transliteration'
                    }
        self.response = requests.request("POST", self.url, headers=self.headers, data = self.payload)
        self.assertEqual(self.response.status_code, 415)
        print("Reponse Code 415")
    

    def test_3_Without_API_Key(self):
        time.sleep(3)
        self.payload = "{\"data\": [\n \"is this www.url2221.com\"],\n\"isBulk\" :false,\n\"contentLanguage\" : \"en\",\n\"ignoreTaggedEntities\" : true\n}"
        self.headers = {
                     'Content-Type': 'application/json',
                     'REV-APP-ID': 'com.revqa',
                     'src_lang': 'en',
                     'tgt_lang': 'hi',
                     'REV-APPNAME': 'transliteration'
                    }
        self.response = requests.request("POST", self.url, headers=self.headers, data = self.payload)
        self.assertEqual(self.response.status_code, 403)
        print("Status Code 403")
        self.assertEqual((self.response.text.encode('utf8')),b'{"message":"Invalid REV-API-KEY or REV-APP-ID","status":403}\n')
        print("Invalid REV-API-KEY or REV-APP-ID")
    

    def test_4_Invalid_API_Key(self):
        time.sleep(3)
        self.payload = "{\"data\": [\n \"is this www.url2221.com\"],\n\"isBulk\" :false,\n\"contentLanguage\" : \"en\",\n\"ignoreTaggedEntities\" : true\n}"
        self.headers = {
                     'Content-Type': 'application/json',
                     'REV-API-KEY': '37c4ef57ed0d9d1803aaf6ff6cc4b7b39c0d21982',
                     'REV-APP-ID': 'com.revqa',
                     'src_lang': 'en',
                     'tgt_lang': 'hi',
                     'REV-APPNAME': 'transliteration'
                    }
        self.response = requests.request("POST", self.url, headers=self.headers, data = self.payload)
        self.assertEqual(self.response.status_code, 403)
        print("Status Code 403")
        self.assertEqual((self.response.text.encode('utf8')),b'{"message":"Invalid REV-API-KEY or REV-APP-ID","status":403}\n')
        print("Invalid REV-API-KEY or REV-APP-ID")
    

    def test_5_Without_API_ID(self):
        time.sleep(3)
        self.payload = "{\"data\": [\n \"is this www.url2221.com\"],\n\"isBulk\" :false,\n\"contentLanguage\" : \"en\",\n\"ignoreTaggedEntities\" : true\n}"
        self.headers = {
                     'Content-Type': 'application/json',
                     'REV-API-KEY': '37c4ef57ed0d9d1803aaf6ff6cc4b7b39c0d2198',
                     'src_lang': 'en',
                     'tgt_lang': 'hi',
                     'REV-APPNAME': 'transliteration'
                    }
        self.response = requests.request("POST", self.url, headers=self.headers, data = self.payload)
        self.assertEqual(self.response.status_code, 403)
        print("Status Code 403")
        self.assertEqual((self.response.text.encode('utf8')),b'{"message":"Invalid REV-API-KEY or REV-APP-ID","status":403}\n')
        print("Invalid REV-API-KEY or REV-APP-ID")


    def test_6_Invalid_API_Id(self):
        time.sleep(3)
        self.payload = "{\"data\": [\n \"is this www.url2221.com\"],\n\"isBulk\" :false,\n\"contentLanguage\" : \"en\",\n\"ignoreTaggedEntities\" : true\n}"
        self.headers = {
                     'Content-Type': 'application/json',
                     'REV-API-KEY': '37c4ef57ed0d9d1803aaf6ff6cc4b7b39c0d2198',
                     'REV-APP-ID': 'com.revqa2',
                     'src_lang': 'en',
                     'tgt_lang': 'hi',
                     'REV-APPNAME': 'transliteration'
                    }
        self.response = requests.request("POST", self.url, headers=self.headers, data = self.payload)
        self.assertEqual(self.response.status_code, 403)
        print("Status Code 403")
        self.assertEqual((self.response.text.encode('utf8')),b'{"message":"Invalid REV-API-KEY or REV-APP-ID","status":403}\n')
        print("Invalid REV-API-KEY or REV-APP-ID")


    def test_7_Without_API_Name(self):
        time.sleep(3)
        self.payload = "{\"data\": [\n \"is this www.url2221.com\"],\n\"isBulk\" :false,\n\"contentLanguage\" : \"en\",\n\"ignoreTaggedEntities\" : true\n}"
        self.headers = {
                     'Content-Type': 'application/json',
                     'REV-API-KEY': '37c4ef57ed0d9d1803aaf6ff6cc4b7b39c0d2198',
                     'REV-APP-ID': 'com.revqa',
                     'src_lang': 'en',
                     'tgt_lang': 'hi',
                    }
        self.response = requests.request("POST", self.url, headers=self.headers, data = self.payload)
        self.assertEqual(self.response.status_code, 403)
        print("Status Code 403")
        res = self.response.json()
        self.assertEqual((res['message']),'Invalid REV-APP-NAME')
    

    def test_8_Invalid_API_Name(self):
        time.sleep(3)
        self.payload = "{\"data\": [\n \"is this www.url2221.com\"],\n\"isBulk\" :false,\n\"contentLanguage\" : \"en\",\n\"ignoreTaggedEntities\" : true\n}"
        self.headers = {
                     'Content-Type': 'application/json',
                     'REV-API-KEY': '37c4ef57ed0d9d1803aaf6ff6cc4b7b39c0d2198',
                     'REV-APP-ID': 'com.revqa',
                     'src_lang': 'en',
                     'tgt_lang': 'hi',
                     'REV-APPNAME': 'transliteration2'
                    }
        self.response = requests.request("POST", self.url, headers=self.headers, data = self.payload)
        self.assertEqual(self.response.status_code, 403)
        print("Status Code 403")
        res = self.response.json()
        self.assertEqual((res['message']),'Invalid REV-APP-NAME')
    

    def test_9_Without_Source_Language(self):
        time.sleep(3)
        self.payload = "{\"data\": [\n \"is this www.url2221.com\"],\n\"isBulk\" :false,\n\"contentLanguage\" : \"en\",\n\"ignoreTaggedEntities\" : true\n}"
        self.headers = {
                     'Content-Type': 'application/json',
                     'REV-API-KEY': '37c4ef57ed0d9d1803aaf6ff6cc4b7b39c0d2198',
                     'REV-APP-ID': 'com.revqa',
                     'tgt_lang': 'hi',
                     'REV-APPNAME': 'transliteration'
                    }
        self.response = requests.request("POST", self.url, headers=self.headers, data = self.payload)
        self.assertEqual(self.response.status_code, 400)
        print("Status Code 400")
        self.assertEqual((self.response.text.encode('utf8')),b'{"message":"Oops! Something wrong happened","error_cause":"Source Language is mandatory","status":"BAD_REQUEST"}')
        print("Source Language is mandatory")
    

    def test_10_Invalid_Source_Language(self):
        time.sleep(3)
        self.payload = "{\"data\": [\n \"is this www.url2221.com\"],\n\"isBulk\" :false,\n\"contentLanguage\" : \"en\",\n\"ignoreTaggedEntities\" : true\n}"
        self.headers = {
                     'Content-Type': 'application/json',
                     'REV-API-KEY': '37c4ef57ed0d9d1803aaf6ff6cc4b7b39c0d2198',
                     'REV-APP-ID': 'com.revqa',
                     'src_lang': 'en2',
                     'tgt_lang': 'hi',
                     'REV-APPNAME': 'transliteration'
                    }
        self.response = requests.request("POST", self.url, headers=self.headers, data = self.payload)
        self.assertEqual(self.response.status_code, 403)
        print("Status Code 403")
        self.assertEqual((self.response.text.encode('utf8')),b'{"message":"unauthorized to use this src/tgt language","status":403}\n')
        print("Unauthorized to use this src/tgt language")
    

    def test_11_Without_Target_Language(self):
        time.sleep(3)
        self.payload = "{\"data\": [\n \"is this www.url2221.com\"],\n\"isBulk\" :false,\n\"contentLanguage\" : \"en\",\n\"ignoreTaggedEntities\" : true\n}"
        self.headers = {
                     'Content-Type': 'application/json',
                     'REV-API-KEY': '37c4ef57ed0d9d1803aaf6ff6cc4b7b39c0d2198',
                     'REV-APP-ID': 'com.revqa',
                     'src_lang': 'en',
                     'REV-APPNAME': 'transliteration'
                    }
        self.response = requests.request("POST", self.url, headers=self.headers, data = self.payload)
        self.assertEqual(self.response.status_code, 400)
        print("Status Code 400")
        self.assertEqual((self.response.text.encode('utf8')),b'{"message":"Oops! Something wrong happened","error_cause":"Target Language is mandatory","status":"BAD_REQUEST"}')
        print("Target Language is mandatory")
    

    def test_12_Invalid_Target_Language(self):
        time.sleep(3)
        self.payload = "{\"data\": [\n \"is this www.url2221.com\"],\n\"isBulk\" :false,\n\"contentLanguage\" : \"en\",\n\"ignoreTaggedEntities\" : true\n}"
        self.headers = {
                     'Content-Type': 'application/json',
                     'REV-API-KEY': '37c4ef57ed0d9d1803aaf6ff6cc4b7b39c0d2198',
                     'REV-APP-ID': 'com.revqa',
                     'src_lang': 'en',
                     'tgt_lang': 'hi2',
                     'REV-APPNAME': 'transliteration'
                    }
        self.response = requests.request("POST", self.url, headers=self.headers, data = self.payload)
        self.assertEqual(self.response.status_code, 403)
        print("Status Code 403")
        self.assertEqual((self.response.text.encode('utf8')),b'{"message":"unauthorized to use this src/tgt language","status":403}\n')
        print("Unauthorized to use this src/tgt language")


    def test_13_Request_without_body(self):
        time.sleep(3)
        self.payload = ""
        self.headers = {
                     'Content-Type': 'application/json',
                     'REV-API-KEY': '37c4ef57ed0d9d1803aaf6ff6cc4b7b39c0d2198',
                     'REV-APP-ID': 'com.revqa',
                     'src_lang': 'en',
                     'tgt_lang': 'hi',
                     'REV-APPNAME': 'transliteration'
                    }
        self.response = requests.request("POST", self.url, headers=self.headers, data = self.payload)
        self.assertEqual(self.response.status_code, 500)
        print("Status Code 500")
    

    def test_14_Request_Invalid_body(self):
        time.sleep(3)
        self.payload = "{\"data\": [\n \"is this www.url2221.com\"],\n\"isBulk\" :false,\ns\n\"contentLanguage\" : \"en\",\n\"ignoreTaggedEntities\" : true\n}\n"
        self.headers = {
                     'Content-Type': 'application/json',
                     'REV-API-KEY': '37c4ef57ed0d9d1803aaf6ff6cc4b7b39c0d2198',
                     'REV-APP-ID': 'com.revqa',
                     'src_lang': 'en',
                     'tgt_lang': 'hi',
                     'REV-APPNAME': 'transliteration'
                    }
        self.response = requests.request("POST", self.url, headers=self.headers, data = self.payload)
        self.assertEqual(self.response.status_code, 400)
        print("Status Code 400")
        print("Bad Request")
    

    def test_15_Request_with_GET(self):
        time.sleep(3)
        self.payload = "{\"data\": [\n \"is this www.url2221.com\"],\n\"isBulk\" :false,\n\"contentLanguage\" : \"en\",\n\"ignoreTaggedEntities\" : true\n}"
        self.headers = {
                     'Content-Type': 'application/json',
                     'REV-API-KEY': '37c4ef57ed0d9d1803aaf6ff6cc4b7b39c0d2198',
                     'REV-APP-ID': 'com.revqa',
                     'src_lang': 'en',
                     'tgt_lang': 'hi',
                     'REV-APPNAME': 'transliteration'
                    }
        self.response = requests.request("GET", self.url, headers=self.headers, data = self.payload)
        self.assertEqual(self.response.status_code, 405)
        print("Status Code 405")
        print("Method Not Allowed")
    

    def test_16_Request_without_Data(self):
        time.sleep(3)
        self.payload = "{\"isBulk\" :false,\n\"contentLanguage\" : \"en\",\n\"ignoreTaggedEntities\" : true\n}"
        self.headers = {
                     'Content-Type': 'application/json',
                     'REV-API-KEY': '37c4ef57ed0d9d1803aaf6ff6cc4b7b39c0d2198',
                     'REV-APP-ID': 'com.revqa',
                     'src_lang': 'en',
                     'tgt_lang': 'hi',
                     'REV-APPNAME': 'transliteration'
                    }
        self.response = requests.request("POST", self.url, headers=self.headers, data = self.payload)
        self.assertEqual(self.response.status_code, 400)
        print("Status Code 400")
        self.assertEqual((self.response.text.encode('utf8')),b'{"message":"Oops! Something wrong happened","error_cause":"Please provide data string","status":"BAD_REQUEST"}')
        print("Data string is Mandatory")
    

    def test_17_Request_Data_without_quotes(self):
        time.sleep(3)
        self.payload = "{\"data\": [\n hello],\n\"isBulk\" :false,\n\"contentLanguage\" : \"en\",\n\"ignoreTaggedEntities\" : true\n}\n"
        self.headers = {
                     'Content-Type': 'application/json',
                     'REV-API-KEY': '37c4ef57ed0d9d1803aaf6ff6cc4b7b39c0d2198',
                     'REV-APP-ID': 'com.revqa',
                     'src_lang': 'en',
                     'tgt_lang': 'hi',
                     'REV-APPNAME': 'transliteration'
                    }
        self.response = requests.request("POST", self.url, headers=self.headers, data = self.payload)
        self.assertEqual(self.response.status_code, 400)
        print("Status Code 400")
        print("Bad Request")
    

    def test_18_Request_with_multiple_Data(self):
        time.sleep(3)
        self.payload = "{\"data\": [\n \"is this www.url2221.com\",\"Chandan\"],\n\"isBulk\" :false,\n\"contentLanguage\" : \"en\",\n\"ignoreTaggedEntities\" : true\n}\n"
        self.headers = {
                     'Content-Type': 'application/json',
                     'REV-API-KEY': '37c4ef57ed0d9d1803aaf6ff6cc4b7b39c0d2198',
                     'REV-APP-ID': 'com.revqa',
                     'src_lang': 'en',
                     'tgt_lang': 'hi',
                     'REV-APPNAME': 'transliteration'
                    }
        self.response = requests.request("POST", self.url, headers=self.headers, data = self.payload)
        self.assertEqual(self.response.status_code, 200)
        print("Status Code 200")
    

    def test_19_Request_bulk_as_Invalid(self):
        time.sleep(3)
        self.payload = "{\"data\": [\n \"is this www.url2221.com\"],\n\"isBulk\" :qdqw,\n\"contentLanguage\" : \"en\",\n\"ignoreTaggedEntities\" : true\n}\n"
        self.headers = {
                     'Content-Type': 'application/json',
                     'REV-API-KEY': '37c4ef57ed0d9d1803aaf6ff6cc4b7b39c0d2198',
                     'REV-APP-ID': 'com.revqa',
                     'src_lang': 'en',
                     'tgt_lang': 'hi',
                     'REV-APPNAME': 'transliteration'
                    }
        self.response = requests.request("POST", self.url, headers=self.headers, data = self.payload)
        self.assertEqual(self.response.status_code, 400)
        print("Status Code 400")
        print("Bad Request")


    def test_20_Request_with_bulk_as_Empty(self):
        time.sleep(3)
        self.payload = "{\"data\": [\n \"is this www.url2221.com\"],\n\"isBulk\" :\n\"contentLanguage\" : \"en\",\n\"ignoreTaggedEntities\" : true\n}\n"
        self.headers = {
                     'Content-Type': 'application/json',
                     'REV-API-KEY': '37c4ef57ed0d9d1803aaf6ff6cc4b7b39c0d2198',
                     'REV-APP-ID': 'com.revqa',
                     'src_lang': 'en',
                     'tgt_lang': 'hi',
                     'REV-APPNAME': 'transliteration'
                    }
        self.response = requests.request("POST", self.url, headers=self.headers, data = self.payload)
        self.assertEqual(self.response.status_code, 400)
        print("Status Code 400")
        print("Bad Request")


    def test_21_Request_with_ignoretag_as_True_and_bulk_as_False(self):
        time.sleep(3)
        self.payload = "{\n \"data\": [\n \"is this www.url2221.com\"],\n\"contentLanguage\" : \"en\",\n\"ignoreTaggedEntities\" : true,\n\"isBulk\" :false\n}"
        self.headers = {
                     'Content-Type': 'application/json',
                     'REV-API-KEY': '37c4ef57ed0d9d1803aaf6ff6cc4b7b39c0d2198',
                     'REV-APP-ID': 'com.revqa',
                     'src_lang': 'en',
                     'tgt_lang': 'hi',
                     'REV-APPNAME': 'transliteration'
                    }
        response = requests.request("POST", self.url, headers=self.headers, data = self.payload)
        res = response.json()
        print("Status Code 200")
        self.assertEqual((res['responseList'][0]['outString']),['इज़ दिस डब्ल्युडब्ल्युडब्ल्यु.यूआरएल2221.कॉम'])


    def test_22_Request_with_ignoretag_as_False_and_bulk_as_True(self):
        time.sleep(3)
        self.payload = "{\n \"data\": [\n \"is this www.url2221.com\"],\n\"contentLanguage\" : \"en\",\n\"ignoreTaggedEntities\" : false,\n\"isBulk\" :true\n}"
        self.headers = {
                     'Content-Type': 'application/json',
                     'REV-API-KEY': '37c4ef57ed0d9d1803aaf6ff6cc4b7b39c0d2198',
                     'REV-APP-ID': 'com.revqa',
                     'src_lang': 'en',
                     'tgt_lang': 'hi',
                     'REV-APPNAME': 'transliteration'
                    }
        response = requests.request("POST", self.url, headers=self.headers, data = self.payload)
        res = response.json()
        print("Status Code 200")
        self.assertEqual((res['responseList'][0]['outString']),['इज़ दिस डब्ल्युडब्ल्युडब्ल्यु.यूआरएल2221.कॉम'])
    

    def test_23_Request_with_ignoretag_as_True_and_bulk_as_True(self):
        time.sleep(3)
        self.payload = "{\n \"data\": [\n \"is this www.url2221.com\"],\n\"contentLanguage\" : \"en\",\n\"ignoreTaggedEntities\" : true,\n\"isBulk\" :true\n}"
        self.headers = {
                     'Content-Type': 'application/json',
                     'REV-API-KEY': '37c4ef57ed0d9d1803aaf6ff6cc4b7b39c0d2198',
                     'REV-APP-ID': 'com.revqa',
                     'src_lang': 'en',
                     'tgt_lang': 'hi',
                     'REV-APPNAME': 'transliteration'
                    }
        response = requests.request("POST", self.url, headers=self.headers, data = self.payload)
        res = response.json()
        print("Status Code 200")
        self.assertEqual((res['responseList'][0]['outString']),['इज़ दिस डब्ल्युडब्ल्युडब्ल्यु.यूआरएल2221.कॉम'])
    

    def test_24_Request_with_ignoretag_as_False_and_bulk_as_False(self):
        time.sleep(3)
        self.payload = "{\n \"data\": [\n \"is this www.url2221.com\"],\n\"contentLanguage\" : \"en\",\n\"ignoreTaggedEntities\" : false,\n\"isBulk\" :false\n}"
        self.headers = {
                     'Content-Type': 'application/json',
                     'REV-API-KEY': '37c4ef57ed0d9d1803aaf6ff6cc4b7b39c0d2198',
                     'REV-APP-ID': 'com.revqa',
                     'src_lang': 'en',
                     'tgt_lang': 'hi',
                     'REV-APPNAME': 'transliteration'
                    }
        response = requests.request("POST", self.url, headers=self.headers, data = self.payload)
        res = response.json()
        print("Status Code 200")
        self.assertEqual((res['responseList'][0]['outString']),['इज़ दिस www.url2221.com'])
    

    def test_25_Request__with_ignoretag_and_Bulk_as_False_with_Convertnumber_as_True(self):
        time.sleep(3)
        self.payload = "{\n \"data\": [\n \"is this www.url2221.com\",\"is this www.wonderlal2221.com\"],\n\"contentLanguage\" : \"en\",\n\"ignoreTaggedEntities\" : false,\n\"isBulk\" :false,\n\"convertNumber\" :true\n}"
        self.headers = {
                     'Content-Type': 'application/json',
                     'REV-API-KEY': '37c4ef57ed0d9d1803aaf6ff6cc4b7b39c0d2198',
                     'REV-APP-ID': 'com.revqa',
                     'src_lang': 'en',
                     'tgt_lang': 'hi',
                     'REV-APPNAME': 'transliteration'
                    }
        response = requests.request("POST", self.url, headers=self.headers, data = self.payload)
        res = response.json()
        print("Status Code 200")
        self.assertEqual((res['responseList'][0]['outString']),['इज़ दिस www.url२२२१.com'])
    

    def test_26_Request_No_of_suggestion_One(self):
        time.sleep(3)
        self.payload = "{\"data\": [\n \"GOLD\"],\n\"noOfSuggestions\" :1,\n\"ignoreTaggedEntities\": true,\n\"isBulk\" : false\n}"
        self.headers = {
                     'Content-Type': 'application/json',
                     'REV-API-KEY': '37c4ef57ed0d9d1803aaf6ff6cc4b7b39c0d2198',
                     'REV-APP-ID': 'com.revqa',
                     'src_lang': 'en',
                     'tgt_lang': 'hi',
                     'REV-APPNAME': 'transliteration'
                    }
        response = requests.request("POST", self.url, headers=self.headers, data = self.payload)
        res = response.json()
        print("Status Code 200")
        self.assertEqual((res['responseList'][0]['outString']),['गोल्ड'])
    

    def test_27_Reverse_Hi(self):
        time.sleep(3)
        self.payload = "{\"data\": [\n \"टेस्टिंग\"],\n\"noOfsuggestions\" :1,\n\"ignoreTaggedEntities\": true,\n\"isBulk\" : false\n}"
        self.headers = {
            'Content-Type': 'application/json',
            'REV-API-KEY': '37c4ef57ed0d9d1803aaf6ff6cc4b7b39c0d2198',
            'REV-APP-ID': 'com.revqa',
            'src_lang': 'hi',
            'tgt_lang': 'en',
            'REV-APPNAME': 'transliteration'
                        }
        response = requests.request("POST", self.url, headers=self.headers, data = self.payload.encode('utf-8'))
        res = response.json()
        print("Hindi Test Passed")
        self.assertEqual(response.status_code, 200)
        self.assertEqual((res['responseList'][0]['outString']),['testing'])


    def test_28_Reverse_Mr(self):
        time.sleep(3)
        self.payload = "{\"data\": [\n \"टेस्टिंग\"],\n\"noOfsuggestions\" :1,\n\"ignoreTaggedEntities\": true,\n\"isBulk\" : false\n}"
        self.headers = {
            'Content-Type': 'application/json',
            'REV-API-KEY': '37c4ef57ed0d9d1803aaf6ff6cc4b7b39c0d2198',
            'REV-APP-ID': 'com.revqa',
            'src_lang': 'mr',
            'tgt_lang': 'en',
            'REV-APPNAME': 'transliteration'
                        }
        response = requests.request("POST", self.url, headers=self.headers, data = self.payload.encode('utf-8'))
        res = response.json()
        print("Marathi Test Passed")
        self.assertEqual(response.status_code, 200)
        self.assertEqual((res['responseList'][0]['outString']),['testing'])


    def test_29_Reverse_Pa(self):
        time.sleep(3)
        self.payload = "{\"data\": [\n \"ਟੇਸਟਿੰਗ\"],\n\"noOfsuggestions\" :1,\n\"ignoreTaggedEntities\": true,\n\"isBulk\" : false\n}"
        self.headers = {
            'Content-Type': 'application/json',
            'REV-API-KEY': '37c4ef57ed0d9d1803aaf6ff6cc4b7b39c0d2198',
            'REV-APP-ID': 'com.revqa',
            'src_lang': 'pa',
            'tgt_lang': 'en',
            'REV-APPNAME': 'transliteration'
                        }
        response = requests.request("POST", self.url, headers=self.headers, data = self.payload.encode('utf-8'))
        res = response.json()
        print("Punjabi Test Passed")
        self.assertEqual(response.status_code, 200)
        self.assertEqual((res['responseList'][0]['outString']),['testing'])


    def test_30_Reverse_Gu(self):
        time.sleep(3)
        self.payload = "{\"data\": [\n \"ટેસ્ટિંગ\"],\n\"noOfsuggestions\" :1,\n\"ignoreTaggedEntities\": true,\n\"isBulk\" : false\n}"
        self.headers = {
            'Content-Type': 'application/json',
            'REV-API-KEY': '37c4ef57ed0d9d1803aaf6ff6cc4b7b39c0d2198',
            'REV-APP-ID': 'com.revqa',
            'src_lang': 'gu',
            'tgt_lang': 'en',
            'REV-APPNAME': 'transliteration'
                        }
        response = requests.request("POST", self.url, headers=self.headers, data = self.payload.encode('utf-8'))
        res = response.json()
        print("Gujarati Test Passed")
        self.assertEqual(response.status_code, 200)
        self.assertEqual((res['responseList'][0]['outString']),['testing'])


    def test_31_Reverse_bn(self):
        time.sleep(3)
        self.payload = "{\"data\": [\n \"টেস্টিং\"],\n\"noOfsuggestions\" :1,\n\"ignoreTaggedEntities\": true,\n\"isBulk\" : false\n}"
        self.headers = {
            'Content-Type': 'application/json',
            'REV-API-KEY': '37c4ef57ed0d9d1803aaf6ff6cc4b7b39c0d2198',
            'REV-APP-ID': 'com.revqa',
            'src_lang': 'bn',
            'tgt_lang': 'en',
            'REV-APPNAME': 'transliteration'
                        }
        response = requests.request("POST", self.url, headers=self.headers, data = self.payload.encode('utf-8'))
        res = response.json()
        print("Bengali Test Passed")
        self.assertEqual(response.status_code, 200)
        self.assertEqual((res['responseList'][0]['outString']),['testing'])


    def test_32_Reverse_Or(self):
        time.sleep(3)
        self.payload = "{\"data\": [\n \"ଟେଷ୍ଟିଙ୍ଗ୍\"],\n\"noOfsuggestions\" :1,\n\"ignoreTaggedEntities\": true,\n\"isBulk\" : false\n}"
        self.headers = {
            'Content-Type': 'application/json',
            'REV-API-KEY': '37c4ef57ed0d9d1803aaf6ff6cc4b7b39c0d2198',
            'REV-APP-ID': 'com.revqa',
            'src_lang': 'or',
            'tgt_lang': 'en',
            'REV-APPNAME': 'transliteration'
                        }
        response = requests.request("POST", self.url, headers=self.headers, data = self.payload.encode('utf-8'))
        res = response.json()
        print("Odia Test Passed")
        self.assertEqual(response.status_code, 200)
        self.assertEqual((res['responseList'][0]['outString']),['testing'])


    def test_33_Reverse_te(self):
        time.sleep(3)
        self.payload = "{\"data\": [\n \"టెస్టింగ్\"],\n\"noOfsuggestions\" :1,\n\"ignoreTaggedEntities\": true,\n\"isBulk\" : false\n}"
        self.headers = {
            'Content-Type': 'application/json',
            'REV-API-KEY': '37c4ef57ed0d9d1803aaf6ff6cc4b7b39c0d2198',
            'REV-APP-ID': 'com.revqa',
            'src_lang': 'te',
            'tgt_lang': 'en',
            'REV-APPNAME': 'transliteration'
                        }
        response = requests.request("POST", self.url, headers=self.headers, data = self.payload.encode('utf-8'))
        res = response.json()
        print("Telugu Test Passed")
        self.assertEqual(response.status_code, 200)
        self.assertEqual((res['responseList'][0]['outString']),['testing'])


    def test_34_Reverse_ta(self):
        time.sleep(3)
        self.payload = "{\"data\": [\n \"டெஸ்டிங்\"],\n\"noOfsuggestions\" :1,\n\"ignoreTaggedEntities\": true,\n\"isBulk\" : false\n}"
        self.headers = {
            'Content-Type': 'application/json',
            'REV-API-KEY': '37c4ef57ed0d9d1803aaf6ff6cc4b7b39c0d2198',
            'REV-APP-ID': 'com.revqa',
            'src_lang': 'ta',
            'tgt_lang': 'en',
            'REV-APPNAME': 'transliteration'
                        }
        response = requests.request("POST", self.url, headers=self.headers, data = self.payload.encode('utf-8'))
        res = response.json()
        print("Tamil Test Passed")
        self.assertEqual(response.status_code, 200)
        self.assertEqual((res['responseList'][0]['outString']),['testing'])


    def test_35_Reverse_Kn(self):
        time.sleep(3)
        self.payload = "{\"data\": [\n \"ಟೆಸ್ಟಿಂಗ್\"],\n\"noOfsuggestions\" :1,\n\"ignoreTaggedEntities\": true,\n\"isBulk\" : false\n}"
        self.headers = {
            'Content-Type': 'application/json',
            'REV-API-KEY': '37c4ef57ed0d9d1803aaf6ff6cc4b7b39c0d2198',
            'REV-APP-ID': 'com.revqa',
            'src_lang': 'kn',
            'tgt_lang': 'en',
            'REV-APPNAME': 'transliteration'
                        }
        response = requests.request("POST", self.url, headers=self.headers, data = self.payload.encode('utf-8'))
        res = response.json()
        print("Kannada Test Passed")
        self.assertEqual(response.status_code, 200)
        self.assertEqual((res['responseList'][0]['outString']),['tasting'])


    def test_36_Reverse_Ml(self):
        time.sleep(3)
        self.payload = "{\"data\": [\n \"ടെസ്റ്റിംഗ്\"],\n\"noOfsuggestions\" :1,\n\"ignoreTaggedEntities\": true,\n\"isBulk\" : false\n}"
        self.headers = {
            'Content-Type': 'application/json',
            'REV-API-KEY': '37c4ef57ed0d9d1803aaf6ff6cc4b7b39c0d2198',
            'REV-APP-ID': 'com.revqa',
            'src_lang': 'ml',
            'tgt_lang': 'en',
            'REV-APPNAME': 'transliteration'
                        }
        response = requests.request("POST", self.url, headers=self.headers, data = self.payload.encode('utf-8'))
        res = response.json()
        print("Malayalam Test Passed")
        self.assertEqual(response.status_code, 200)
        self.assertEqual((res['responseList'][0]['outString']),['testing'])


    def test_37_Reverse_As(self):
        time.sleep(3)
        self.payload = "{\"data\": [\n \"টেস্টিং\"],\n\"noOfsuggestions\" :1,\n\"ignoreTaggedEntities\": true,\n\"isBulk\" : false\n}"
        self.headers = {
            'Content-Type': 'application/json',
            'REV-API-KEY': '37c4ef57ed0d9d1803aaf6ff6cc4b7b39c0d2198',
            'REV-APP-ID': 'com.revqa',
            'src_lang': 'as',
            'tgt_lang': 'en',
            'REV-APPNAME': 'transliteration'
                        }
        response = requests.request("POST", self.url, headers=self.headers, data = self.payload.encode('utf-8'))
        res = response.json()
        print("Assamese Test Passed")
        self.assertEqual(response.status_code, 200)
        self.assertEqual((res['responseList'][0]['outString']),['testing'])


    def test_38_Forward_Hi(self):
        time.sleep(3)
        self.payload = "{\"data\": [\n \"testing\"],\n\"noOfsuggestions\" :1,\n\"ignoreTaggedEntities\": true,\n\"isBulk\" : false\n}"
        self.headers = {
            'Content-Type': 'application/json',
            'REV-API-KEY': '37c4ef57ed0d9d1803aaf6ff6cc4b7b39c0d2198',
            'REV-APP-ID': 'com.revqa',
            'src_lang': 'en',
            'tgt_lang': 'hi',
            'REV-APPNAME': 'transliteration'
                        }
        response = requests.request("POST", self.url, headers=self.headers, data = self.payload)
        res = response.json()
        print("Hindi Test Passed")
        self.assertEqual(response.status_code, 200)
        self.assertEqual((res['responseList'][0]['outString']),['टेस्टिंग'])


    def test_39_Forward_Mr(self):
        time.sleep(3)
        self.payload = "{\"data\": [\n \"testing\"],\n\"noOfsuggestions\" :1,\n\"ignoreTaggedEntities\": true,\n\"isBulk\" : false\n}"
        self.headers = {
            'Content-Type': 'application/json',
            'REV-API-KEY': '37c4ef57ed0d9d1803aaf6ff6cc4b7b39c0d2198',
            'REV-APP-ID': 'com.revqa',
            'src_lang': 'en',
            'tgt_lang': 'mr',
            'REV-APPNAME': 'transliteration'
                        }
        response = requests.request("POST", self.url, headers=self.headers, data = self.payload)
        res = response.json()
        print("Marathi Test Passed")
        self.assertEqual(response.status_code, 200)
        self.assertEqual((res['responseList'][0]['outString']),['टेस्टिंग'])

    def test_40_Forward_Pa(self):
        time.sleep(3)
        self.payload = "{\"data\": [\n \"testing\"],\n\"noOfsuggestions\" :1,\n\"ignoreTaggedEntities\": true,\n\"isBulk\" : false\n}"
        self.headers = {
            'Content-Type': 'application/json',
            'REV-API-KEY': '37c4ef57ed0d9d1803aaf6ff6cc4b7b39c0d2198',
            'REV-APP-ID': 'com.revqa',
            'src_lang': 'en',
            'tgt_lang': 'pa',
            'REV-APPNAME': 'transliteration'
                        }
        response = requests.request("POST", self.url, headers=self.headers, data = self.payload)
        res = response.json()
        print("Punjabi Test Passed")
        self.assertEqual(response.status_code, 200)
        self.assertEqual((res['responseList'][0]['outString']),['ਟੇਸਟਿੰਗ'])

    def test_41_Forward_Gu(self):
        time.sleep(3)
        self.payload = "{\"data\": [\n \"testing\"],\n\"noOfsuggestions\" :1,\n\"ignoreTaggedEntities\": true,\n\"isBulk\" : false\n}"
        self.headers = {
            'Content-Type': 'application/json',
            'REV-API-KEY': '37c4ef57ed0d9d1803aaf6ff6cc4b7b39c0d2198',
            'REV-APP-ID': 'com.revqa',
            'src_lang': 'en',
            'tgt_lang': 'gu',
            'REV-APPNAME': 'transliteration'
                        }
        response = requests.request("POST", self.url, headers=self.headers, data = self.payload)
        res = response.json()
        print("Gujarati Test Passed")
        self.assertEqual(response.status_code, 200)
        self.assertEqual((res['responseList'][0]['outString']),['ટેસ્ટિંગ'])

    def test_42_forward_bn(self):
        time.sleep(3)
        self.payload = "{\"data\": [\n \"testing\"],\n\"noOfsuggestions\" :1,\n\"ignoreTaggedEntities\": true,\n\"isBulk\" : false\n}"
        self.headers = {
            'Content-Type': 'application/json',
            'REV-API-KEY': '37c4ef57ed0d9d1803aaf6ff6cc4b7b39c0d2198',
            'REV-APP-ID': 'com.revqa',
            'src_lang': 'en',
            'tgt_lang': 'bn',
            'REV-APPNAME': 'transliteration'
                        }
        response = requests.request("POST", self.url, headers=self.headers, data = self.payload)
        res = response.json()
        print("Bengali Test Passed")
        self.assertEqual(response.status_code, 200)
        self.assertEqual((res['responseList'][0]['outString']),['টেস্টিং'])

    def test_43_Reverse_Or(self):
        time.sleep(3)
        self.payload = "{\"data\": [\n \"testing\"],\n\"noOfsuggestions\" :1,\n\"ignoreTaggedEntities\": true,\n\"isBulk\" : false\n}"
        self.headers = {
            'Content-Type': 'application/json',
            'REV-API-KEY': '37c4ef57ed0d9d1803aaf6ff6cc4b7b39c0d2198',
            'REV-APP-ID': 'com.revqa',
            'src_lang': 'en',
            'tgt_lang': 'or',
            'REV-APPNAME': 'transliteration'
                        }
        response = requests.request("POST", self.url, headers=self.headers, data = self.payload)
        res = response.json()
        print("Odia Test Passed")
        self.assertEqual(response.status_code, 200)
        self.assertEqual((res['responseList'][0]['outString']),['ଟେଷ୍ଟିଙ୍ଗ୍'])

    def test_44_Forward_te(self):
        time.sleep(3)
        self.payload = "{\"data\": [\n \"testing\"],\n\"noOfsuggestions\" :1,\n\"ignoreTaggedEntities\": true,\n\"isBulk\" : false\n}"
        self.headers = {
            'Content-Type': 'application/json',
            'REV-API-KEY': '37c4ef57ed0d9d1803aaf6ff6cc4b7b39c0d2198',
            'REV-APP-ID': 'com.revqa',
            'src_lang': 'en',
            'tgt_lang': 'te',
            'REV-APPNAME': 'transliteration'
                        }
        response = requests.request("POST", self.url, headers=self.headers, data = self.payload)
        res = response.json()
        print("Telugu Test Passed")
        self.assertEqual(response.status_code, 200)
        self.assertEqual((res['responseList'][0]['outString']),['టెస్టింగ్'])

    def test_45_Forward_ta(self):
        time.sleep(3)
        self.payload = "{\"data\": [\n \"testing\"],\n\"noOfsuggestions\" :1,\n\"ignoreTaggedEntities\": true,\n\"isBulk\" : false\n}"
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
        print("Tamil Test Passed")
        self.assertEqual(response.status_code, 200)
        self.assertEqual((res['responseList'][0]['outString']),['டெஸ்டிங்'])

    def test_46_Forward_Kn(self):
        time.sleep(3)
        self.payload = "{\"data\": [\n \"testing\"],\n\"noOfsuggestions\" :1,\n\"ignoreTaggedEntities\": true,\n\"isBulk\" : false\n}"
        self.headers = {
            'Content-Type': 'application/json',
            'REV-API-KEY': '37c4ef57ed0d9d1803aaf6ff6cc4b7b39c0d2198',
            'REV-APP-ID': 'com.revqa',
            'src_lang': 'en',
            'tgt_lang': 'kn',
            'REV-APPNAME': 'transliteration'
                        }
        response = requests.request("POST", self.url, headers=self.headers, data = self.payload)
        res = response.json()
        print("Kannada Test Passed")
        self.assertEqual(response.status_code, 200)
        self.assertEqual((res['responseList'][0]['outString']),['ಟೆಸ್ಟಿಂಗ್'])

    def test_47_Forward_Ml(self):
        time.sleep(3)
        self.payload = "{\"data\": [\n \"testing\"],\n\"noOfsuggestions\" :1,\n\"ignoreTaggedEntities\": true,\n\"isBulk\" : false\n}"
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
        print("Malayalam Test Passed")
        self.assertEqual(response.status_code, 200)
        self.assertEqual((res['responseList'][0]['outString']),['ടെസ്റ്റിംഗ്'])

    def test_48_Forward_As(self):
        time.sleep(3)
        self.payload = "{\"data\": [\n \"testing\"],\n\"noOfsuggestions\" :1,\n\"ignoreTaggedEntities\": true,\n\"isBulk\" : false\n}"
        self.headers = {
            'Content-Type': 'application/json',
            'REV-API-KEY': '37c4ef57ed0d9d1803aaf6ff6cc4b7b39c0d2198',
            'REV-APP-ID': 'com.revqa',
            'src_lang': 'en',
            'tgt_lang': 'as',
            'REV-APPNAME': 'transliteration'
                        }
        response = requests.request("POST", self.url, headers=self.headers, data = self.payload)
        res = response.json()
        print("Assamese Test Passed")
        self.assertEqual(response.status_code, 200)
        self.assertEqual((res['responseList'][0]['outString']),['টেস্টিং'])
    
    def test_49_Request_No_of_suggestion_as_Five(self):
        time.sleep(3)
        self.payload = "{\"data\": [\n \"GOLD\"],\n\"noOfSuggestions\" :5,\n\"ignoreTaggedEntities\": true,\n\"isBulk\" : false\n}"
        self.headers = {
                     'Content-Type': 'application/json',
                     'REV-API-KEY': '37c4ef57ed0d9d1803aaf6ff6cc4b7b39c0d2198',
                     'REV-APP-ID': 'com.revqa',
                     'src_lang': 'en',
                     'tgt_lang': 'hi',
                     'REV-APPNAME': 'transliteration'
                    }
        response = requests.request("POST", self.url, headers=self.headers, data = self.payload)
        res = response.json()
        print("Status Code 200")
        self.assertEqual((res['responseList'][0]['outString'][0]),'गोल्ड')
        self.assertEqual((res['responseList'][0]['outString'][1]),'जी.ओ.एल.डी.')
        self.assertEqual((res['responseList'][0]['outString'][2]),'गोलड')
        self.assertEqual((res['responseList'][0]['outString'][3]),'गोल्द')
        self.assertEqual((res['responseList'][0]['outString'][4]),'गोलद')

    def test_50_Request_without_No_of_suggestion(self):
        time.sleep(3)
        self.payload = "{\"data\": [\n \"GOLD\"],\n\"ignoreTaggedEntities\": true,\n\"isBulk\" : false\n}"
        self.headers = {
                     'Content-Type': 'application/json',
                     'REV-API-KEY': '37c4ef57ed0d9d1803aaf6ff6cc4b7b39c0d2198',
                     'REV-APP-ID': 'com.revqa',
                     'src_lang': 'en',
                     'tgt_lang': 'hi',
                     'REV-APPNAME': 'transliteration'
                    }
        response = requests.request("POST", self.url, headers=self.headers, data = self.payload)
        res = response.json()
        print("Status Code 200")
        self.assertEqual((res['responseList'][0]['outString'][0]),'गोल्ड')
    
    def test_51_Request_No_of_suggestion_as_four_with_special_characters(self):
        time.sleep(3)
        self.payload = "{\"data\": [\n \"gold!.p123\"],\n\"noOfSuggestions\" :4,\n\"ignoreTaggedEntities\": true,\n\"isBulk\" : false\n}"
        self.headers = {
                     'Content-Type': 'application/json',
                     'REV-API-KEY': '37c4ef57ed0d9d1803aaf6ff6cc4b7b39c0d2198',
                     'REV-APP-ID': 'com.revqa',
                     'src_lang': 'en',
                     'tgt_lang': 'hi',
                     'REV-APPNAME': 'transliteration'
                    }
        response = requests.request("POST", self.url, headers=self.headers, data = self.payload)
        res = response.json()
        print("Status Code 200")
        self.assertEqual((res['responseList'][0]['outString'][0]),'गोल्ड!.पी123')
        self.assertEqual((res['responseList'][0]['outString'][1]),'गोल्ड!.प123')
        self.assertEqual((res['responseList'][0]['outString'][2]),'गोलड!.पी123')
        self.assertEqual((res['responseList'][0]['outString'][3]),'गोलड!.प123')
    
    def test_52_Request_No_of_suggestion_as_Six_with_Capital_Letters(self):
        time.sleep(3)
        self.payload = "{\"data\": [\n \"GOLD\"],\n\"noOfSuggestions\" :6,\n\"ignoreTaggedEntities\": true,\n\"isBulk\" : false\n}"
        self.headers = {
                     'Content-Type': 'application/json',
                     'REV-API-KEY': '37c4ef57ed0d9d1803aaf6ff6cc4b7b39c0d2198',
                     'REV-APP-ID': 'com.revqa',
                     'src_lang': 'en',
                     'tgt_lang': 'hi',
                     'REV-APPNAME': 'transliteration'
                    }
        response = requests.request("POST", self.url, headers=self.headers, data = self.payload)
        res = response.json()
        print("Status Code 200")
        self.assertEqual((res['responseList'][0]['outString'][0]),'गोल्ड')
        self.assertEqual((res['responseList'][0]['outString'][1]),'जी.ओ.एल.डी.')
        self.assertEqual((res['responseList'][0]['outString'][2]),'गोलड')
        self.assertEqual((res['responseList'][0]['outString'][3]),'गोल्द')
        self.assertEqual((res['responseList'][0]['outString'][4]),'गोलद')
        self.assertEqual((res['responseList'][0]['outString'][5]),'गॉल्ड')
    
    def test_53_Request_No_of_suggestion_as_Two_with_Data_as_Address(self):
        time.sleep(3)
        self.payload = "{\"data\": [\n \"206, casa royale, windtunnel road, bangalore-500016\"],\n\"noOfSuggestions\" :2,\n\"ignoreTaggedEntities\": true,\n\"isBulk\" : false\n}"
        self.headers = {
                     'Content-Type': 'application/json',
                     'REV-API-KEY': '37c4ef57ed0d9d1803aaf6ff6cc4b7b39c0d2198',
                     'REV-APP-ID': 'com.revqa',
                     'src_lang': 'en',
                     'tgt_lang': 'hi',
                     'REV-APPNAME': 'transliteration'
                    }
        response = requests.request("POST", self.url, headers=self.headers, data = self.payload)
        res = response.json()
        print("Status Code 200")
        self.assertEqual((res['responseList'][0]['outString'][0]),'206, कासा रोयाल, वीन्द्तुन्नेल रोड, बैंगलोर-500016')
        self.assertEqual((res['responseList'][0]['outString'][1]),'206, कासा रोयाल, वीन्द्तुन्नेल रोड, बंगलोरे-500016')
    
    def test_54_Uppercase_Body(self):
        time.sleep(3)
        self.payload = "{\"data\": [\n \"TESTING\"],\n\"noOfsuggestions\" :1,\n\"ignoreTaggedEntities\": true,\n\"isBulk\" : false\n}"
        self.headers = {
            'Content-Type': 'application/json',
            'REV-API-KEY': '37c4ef57ed0d9d1803aaf6ff6cc4b7b39c0d2198',
            'REV-APP-ID': 'com.revqa',
            'src_lang': 'en',
            'tgt_lang': 'gu',
            'REV-APPNAME': 'transliteration'
                        }
        response = requests.request("POST", self.url, headers=self.headers, data = self.payload)
        res = response.json()
        print("Uppercase body Test Passed")
        self.assertEqual(response.status_code, 200)
        self.assertEqual((res['responseList'][0]['outString']),['ટેસ્ટિંગ'])

    def test_55_tagged_entity_false_convertnumber_true(self):
        time.sleep(3)
        self.payload = "{\"data\": [\n \"is this www.ur.com,  zalak2306@gmail.com , 2567D near rameshwar\"],\n\"contentLanguage\" : \"en\",\n\"ignoreTaggedEntities\" : false,\n\"isBulk\" :false,\n\"convertNumber\": true\n}"
        self.headers = {
            'Content-Type': 'application/json',
            'REV-API-KEY': '37c4ef57ed0d9d1803aaf6ff6cc4b7b39c0d2198',
            'REV-APP-ID': 'com.revqa',
            'src_lang': 'en',
            'tgt_lang': 'gu',
            'REV-APPNAME': 'transliteration'
                        }
        response = requests.request("POST", self.url, headers=self.headers, data = self.payload)
        res = response.json()
        print("Test Passed")
        self.assertEqual(response.status_code, 200)
        self.assertEqual((res['responseList'][0]['outString']),['ઈઝ ધીસ www.ur.com,  zalak2306@gmail.com , ૨૫૬૭ડી નિઅર રામેશ્વર'])

    def test_56_tagged_entity_false_convertnumber_false_email_URL(self):
        time.sleep(3)
        self.payload = "{\"data\": [\n \"share the data to suhana123@gmail.com is this www.url2221.com\"],\n\"ignoreTaggedEntities\" : false,\n\"isBulk\" :false,\n\"convertNumber\": false\n}"
        self.headers = {
            'Content-Type': 'application/json',
            'REV-API-KEY': '37c4ef57ed0d9d1803aaf6ff6cc4b7b39c0d2198',
            'REV-APP-ID': 'com.revqa',
            'src_lang': 'en',
            'tgt_lang': 'gu',
            'REV-APPNAME': 'transliteration'
                        }
        response = requests.request("POST", self.url, headers=self.headers, data = self.payload)
        res = response.json()
        print("Test Passed")
        self.assertEqual(response.status_code, 200)
        self.assertEqual((res['responseList'][0]['outString']),['શેઅર ધ ડેટા ટુ suhana123@gmail.com ઈઝ ધીસ www.url2221.com'])

    def test_57_taggedEntity_false_UpperCase(self):
        time.sleep(3)
        self.payload = "{\"data\": [\n \"IS THIS WWW.URL2221.COM and ZALAK2306@GMAIL.COM\"],\n\"ignoreTaggedEntities\" : false,\n\"isBulk\" :false\n}"
        self.headers = {
            'Content-Type': 'application/json',
            'REV-API-KEY': '37c4ef57ed0d9d1803aaf6ff6cc4b7b39c0d2198',
            'REV-APP-ID': 'com.revqa',
            'src_lang': 'en',
            'tgt_lang': 'gu',
            'REV-APPNAME': 'transliteration'
                        }
        response = requests.request("POST", self.url, headers=self.headers, data = self.payload)
        res = response.json()
        print("Test Passed")
        self.assertEqual(response.status_code, 200)
        self.assertEqual((res['responseList'][0]['outString']),['ઈઝ ધીસ ડબ્લ્યુડબ્લ્યુડબ્લ્યુ.યૂ.આર.એલ.2221.કોમ એન્ડ ઝલક2306@જીમેઈલ.કોમ'])

    def test_58_invalid_data_string(self):
        time.sleep(3)
        self.payload = "{\"data\": [\n 'Hello']\n}"
        self.headers = {
            'Content-Type': 'application/json',
            'REV-API-KEY': '37c4ef57ed0d9d1803aaf6ff6cc4b7b39c0d2198',
            'REV-APP-ID': 'com.revqa',
            'src_lang': 'en',
            'tgt_lang': 'gu',
            'REV-APPNAME': 'transliteration'
                        }
        response = requests.request("POST", self.url, headers=self.headers, data = self.payload)
        #res = response.json()
        print("Test Passed")
        self.assertEqual(response.status_code, 400)
        #self.assertEqual((res['responseList'][0]['outString']),['ઈઝ ધીસ ડબ્લ્યુડબ્લ્યુડબ્લ્યુ.યૂ.આર.એલ.2221.કોમ એન્ડ ઝલક2306@જીમેઈલ.કોમ'])

    def test_59_combination_special_characters(self):
        time.sleep(3)
        self.payload = "{\"data\": [\n \"a,b,9282=-!!==\"]\n}"
        self.headers = {
            'Content-Type': 'application/json',
            'REV-API-KEY': '37c4ef57ed0d9d1803aaf6ff6cc4b7b39c0d2198',
            'REV-APP-ID': 'com.revqa',
            'src_lang': 'en',
            'tgt_lang': 'gu',
            'REV-APPNAME': 'transliteration'
                        }
        response = requests.request("POST", self.url, headers=self.headers, data = self.payload)
        res = response.json()
        print("Test Passed")
        self.assertEqual(response.status_code, 200)
        self.assertEqual((res['responseList'][0]['outString']),['એ,બી,9282=-!!=='])

    def test_60_both_english(self):
        time.sleep(3)
        self.payload = "{\"data\": [\n \"is this www.url2221.com\"]\n}"
        self.headers = {
            'Content-Type': 'application/json',
            'REV-API-KEY': '37c4ef57ed0d9d1803aaf6ff6cc4b7b39c0d2198',
            'REV-APP-ID': 'com.revqa',
            'src_lang': 'en',
            'tgt_lang': 'en',
            'REV-APPNAME': 'transliteration'
                        }
        response = requests.request("POST", self.url, headers=self.headers, data = self.payload)
        res = response.json()
        print("Test Passed")
        self.assertEqual(response.status_code, 200)
        self.assertEqual((res['responseList'][0]['outString']),['is this www.url2221.com'])

    def test_61_convert_number_false(self):
        time.sleep(3)
        self.payload = "{\"data\": [\n \"206, CASA ROYALE, WINDTUNNEL ROAD, BANGALORE-500016\"],\n\"convertNumber\" :false,\n\"ignoreTaggedEntities\": true,\n\"isBulk\" : false\n}"
        self.headers = {
            'Content-Type': 'application/json',
            'REV-API-KEY': '37c4ef57ed0d9d1803aaf6ff6cc4b7b39c0d2198',
            'REV-APP-ID': 'com.revqa',
            'src_lang': 'en',
            'tgt_lang': 'hi',
            'REV-APPNAME': 'transliteration'
                        }
        response = requests.request("POST", self.url, headers=self.headers, data = self.payload)
        res = response.json()
        print("Test Passed")
        self.assertEqual(response.status_code, 200)
        self.assertEqual((res['responseList'][0]['outString']),['206, कासा रोयाल, डब्ल्यू.आई.एन.डी.टी.यू.एन.एन.ई.एल. रोड, बैंगलोर-500016'])

    def test_62_convert_number_true(self):
        time.sleep(3)
        self.payload = "{\"data\": [\n \"206, CASA ROYALE, WINDTUNNEL ROAD, BANGALORE-500016\"],\n\"convertNumber\" :true,\n\"ignoreTaggedEntities\": true,\n\"isBulk\" : false\n}"
        self.headers = {
            'Content-Type': 'application/json',
            'REV-API-KEY': '37c4ef57ed0d9d1803aaf6ff6cc4b7b39c0d2198',
            'REV-APP-ID': 'com.revqa',
            'src_lang': 'en',
            'tgt_lang': 'hi',
            'REV-APPNAME': 'transliteration'
                        }
        response = requests.request("POST", self.url, headers=self.headers, data = self.payload)
        res = response.json()
        print("Test Passed")
        self.assertEqual(response.status_code, 200)
        self.assertEqual((res['responseList'][0]['outString']),['२०६, कासा रोयाल, डब्ल्यू.आई.एन.डी.टी.यू.एन.एन.ई.एल. रोड, बैंगलोर-५०००१६'])

    def test_63_convert_number_defualt(self):
        time.sleep(3)
        self.payload = "{\"data\": [\n \"206, CASA ROYALE, WINDTUNNEL ROAD, BANGALORE-500016\"],\n\"ignoreTaggedEntities\": true,\n\"isBulk\" : false\n}"
        self.headers = {
            'Content-Type': 'application/json',
            'REV-API-KEY': '37c4ef57ed0d9d1803aaf6ff6cc4b7b39c0d2198',
            'REV-APP-ID': 'com.revqa',
            'src_lang': 'en',
            'tgt_lang': 'hi',
            'REV-APPNAME': 'transliteration'
                        }
        response = requests.request("POST", self.url, headers=self.headers, data = self.payload)
        res = response.json()
        print("Test Passed")
        self.assertEqual(response.status_code, 200)
        self.assertEqual((res['responseList'][0]['outString']),['206, कासा रोयाल, डब्ल्यू.आई.एन.डी.टी.यू.एन.एन.ई.एल. रोड, बैंगलोर-500016'])

    def test_64_suggestion_alpha(self):
        time.sleep(3)
        self.payload = "{\n\"data\": [\n \"namaste\"],\n\"noOfsuggestions\" : rr\n}"
        self.headers = {
            'Content-Type': 'application/json',
            'REV-API-KEY': '37c4ef57ed0d9d1803aaf6ff6cc4b7b39c0d2198',
            'REV-APP-ID': 'com.revqa',
            'src_lang': 'en',
            'tgt_lang': 'hi',
            'REV-APPNAME': 'transliteration'
                        }
        response = requests.request("POST", self.url, headers=self.headers, data = self.payload)
        #res = response.json()
        print("Test Passed")
        self.assertEqual(response.status_code, 400)
        #self.assertEqual((res['responseList'][0]['outString']),['206, कासा रोयाल, डब्ल्यू.आई.एन.डी.टी.यू.एन.एन.ई.एल. रोड, बैंगलोर-500016'])

    def test_65_suggestion_empty(self):
        time.sleep(3)
        self.payload = "{\n\"data\": [\n \"namaste\"],\n\"noOfsuggestions\" : \n}"
        self.headers = {
            'Content-Type': 'application/json',
            'REV-API-KEY': '37c4ef57ed0d9d1803aaf6ff6cc4b7b39c0d2198',
            'REV-APP-ID': 'com.revqa',
            'src_lang': 'en',
            'tgt_lang': 'hi',
            'REV-APPNAME': 'transliteration'
                        }
        response = requests.request("POST", self.url, headers=self.headers, data = self.payload)
        #res = response.json()
        print("Test Passed")
        self.assertEqual(response.status_code, 400)
        #self.assertEqual((res['responseList'][0]['outString']),['206, कासा रोयाल, डब्ल्यू.आई.एन.डी.टी.यू.एन.एन.ई.एल. रोड, बैंगलोर-500016'])


    def test_66_suggestion_taggedentity_true(self):
        time.sleep(3)
        self.payload = "{\n\"data\": [\n \"is this www.url2221.com zalak306@gmail.com\", \"206, CASA ROYALE, WINDTUNNEL ROAD, BANGALORE-500016\"],\n\"ignoreTaggedEntities\" : false,\n\"isBulk\": false,\n\"noOfSuggestions\": 2\n}"
        self.headers = {
            'Content-Type': 'application/json',
            'REV-API-KEY': '37c4ef57ed0d9d1803aaf6ff6cc4b7b39c0d2198',
            'REV-APP-ID': 'com.revqa',
            'src_lang': 'en',
            'tgt_lang': 'hi',
            'REV-APPNAME': 'transliteration'
                        }
        response = requests.request("POST", self.url, headers=self.headers, data = self.payload)
        res = response.json()
        print("Test Passed")
        self.assertEqual(response.status_code, 200)
        self.assertEqual((res['responseList'][0]['outString']),['इज़ दिस www.url2221.com zalak306@gmail.com'])

    def test_67_suggestion_five_uppercase(self):
        time.sleep(3)
        self.payload = "{\"data\": [\n \"206, CASA ROYALE, WINDTUNNEL ROAD, BANGALORE-500016\"],\n \"noOfSuggestions\": 5,\n\"isBulk\" : false\n}"
        self.headers = {
            'Content-Type': 'application/json',
            'REV-API-KEY': '37c4ef57ed0d9d1803aaf6ff6cc4b7b39c0d2198',
            'REV-APP-ID': 'com.revqa',
            'src_lang': 'en',
            'tgt_lang': 'hi',
            'REV-APPNAME': 'transliteration'
                        }
        response = requests.request("POST", self.url, headers=self.headers, data = self.payload)
        res = response.json()
        print("Test Passed")
       
        self.assertEqual(response.status_code, 200)
        self.assertEqual((res['responseList'][0]['outString'][0]),'206, कासा रोयाल, डब्ल्यू.आई.एन.डी.टी.यू.एन.एन.ई.एल. रोड, बैंगलोर-500016')
        self.assertEqual((res['responseList'][0]['outString'][1]),'206, कासा रोयाल, डब्ल्यू.आई.एन.डी.टी.यू.एन.एन.ई.एल. रोड, बंगलोरे-500016')
        self.assertEqual((res['responseList'][0]['outString'][2]),'206, कासा रोयाल, डब्ल्यू.आई.एन.डी.टी.यू.एन.एन.ई.एल. रोद, बैंगलोर-500016')
        self.assertEqual((res['responseList'][0]['outString'][3]),'206, कासा रोयाल, डब्ल्यू.आई.एन.डी.टी.यू.एन.एन.ई.एल. रोद, बंगलोरे-500016')
        self.assertEqual((res['responseList'][0]['outString'][4]),'206, कासा रोयाल, वीन्द्तुन्नेल रोड, बैंगलोर-500016')

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
