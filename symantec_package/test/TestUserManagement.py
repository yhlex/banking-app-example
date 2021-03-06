import unittest
from unittest.mock import Mock, patch
from suds.client import Client
import sys
import symantec_package

sys.path.append("/home/gabriel/Projects/PythonProjects/Symantec/Securitas/symantec_package/lib/managementService")

from symantec_package.lib.managementService.SymantecManagementServices import SymantecManagementServices

from symantec_package.HTTPHandler import setConnection, HTTPSClientAuthHandler, HTTPSClientCertTransport


class TestUserManagement(unittest.TestCase):
    def setUp(self):
        # the URLs for now which will have the WSDL files and the XSD file
        managementservices_url = 'http://webdev.cse.msu.edu/~huynhall/vipuserservices-mgmt-1.7.wsdl'

        # initializing the Suds clients for each url, with the client certificate youll have in the same dir as this file
        self.management_client = Client(managementservices_url,
                                        transport=HTTPSClientCertTransport('vip_certificate.crt',
                                                                           'vip_certificate.crt'))

        self.test_management_services_object = SymantecManagementServices(self.management_client)
        pass


    @patch('symantec_package.lib.managementService.SymantecManagementServices')
    def test_mock_create_user(self, mock_managementservices):
        reply = \
        """
        {'requestId': create_123, 'status': 0000, 'statusMessage': Success}
        """
        # Configure the mock to return a response with an OK status code. Also, the mock should have
        # a `json()` method that returns a list of todos.
        mock_managementservices.createUser.return_value = Mock()
        mock_managementservices.createUser.return_value.json.return_value = reply

        # Call the service, which will send a request to the server.
        response = symantec_package.lib.managementService.SymantecManagementServices.createUser("create_123",
                                                                                                "new_user3")

        print(response.json())
        # If the request is sent successfully, then I expect a response to be returned.
        self.assertTrue((response.json()) == reply)
        pass

    @patch('symantec_package.lib.managementService.SymantecManagementServices')
    def test_mock_delete_user(self, mock_managementservices):
        reply = \
        """
        {'requestId': delete_123, 'status': 0000, 'statusMessage': Success}
        """
        # Configure the mock to return a response with an OK status code. Also, the mock should have
        # a `json()` method that returns a list of todos.
        mock_managementservices.deleteUser.return_value = Mock()
        mock_managementservices.deleteUser.return_value.json.return_value = reply

        # Call the service, which will send a request to the server.
        response = symantec_package.lib.managementService.SymantecManagementServices.deleteUser("delete_123",
                                                                                                "new_user3")

        print(response.json())
        # If the request is sent successfully, then I expect a response to be returned.
        self.assertTrue((response.json()) == reply)
        pass

    @patch('symantec_package.lib.managementService.SymantecManagementServices')
    def test_mock_add_STANDARDOTP_credential(self, mock_managementservices):
        reply = \
        """
        {'statusMessage': Success, 'requestId': add_otp_cred, 'status': 0000}
        """
        # Configure the mock to return a response with an OK status code. Also, the mock should have
        # a `json()` method that returns a list of todos.
        mock_managementservices.addCredentialOtp.return_value = Mock()
        mock_managementservices.addCredentialOtp.return_value.json.return_value = reply

        response = symantec_package.lib.managementService.SymantecManagementServices.addCredentialOtp("add_otp_cred", "new_user3",
                                                                               "VSMT16833399", "STANDARD_OTP", \
                                                                               "678066")  # change with what's on your device
        print(response.json())
        # If the request is sent successfully, then I expect a response to be returned.
        self.assertTrue((response.json()) == reply)
        pass

    @patch('symantec_package.lib.managementService.SymantecManagementServices')
    def test_mock_delete_STANDARDOTP_credential(self, mock_managementservices):
        reply = \
            """
            {'status': 0000, 'requestId': remove_123, 'statusMessage': Success}
            """
        # Configure the mock to return a response with an OK status code. Also, the mock should have
        # a `json()` method that returns a list of todos.
        mock_managementservices.removeCredential.return_value = Mock()
        mock_managementservices.removeCredential.return_value.json.return_value = reply

        response = symantec_package.lib.managementService.SymantecManagementServices.removeCredential("remove_123", "new_user3",
                                                                                                      "VSMT16833399", "STANDARD_OTP")
        print(response.json())
        # If the request is sent successfully, then I expect a response to be returned.
        self.assertTrue((response.json()) == reply)
        pass


if __name__ == '__main__':
    unittest.main()