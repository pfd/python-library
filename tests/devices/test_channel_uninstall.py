import unittest
import mock
import json
import requests
import urbanairship as ua


class TestChannelUninstall(unittest.TestCase):
    def test_channel_uninstall(self):
        with mock.patch.object(ua.Airship, '_request') as mock_request:
            response = requests.Response()
            response._content = ('{"ok": true}')
            mock_request.return_value = response
            airship = ua.Airship('key', 'secret')

            cu = ua.ChannelUninstall(airship)

            chans = [
                {
                    "channel_id": "01000001-01010000-01010000-01001100",
                    "device_type": "ios"
                },
                {
                    "channel_id": "01000111-01001111-01001111-01000111",
                    "device_type": "android"
                }
            ]

            cu_response = json.loads(cu.uninstall(chans).content)
            print cu_response
            self.assertEqual(cu_response["ok"], True)