import unittest
from unittest.mock import patch
from utils.api_client import CerebrasClient

class TestAPI(unittest.TestCase):
    @patch('requests.post')
    def test_api_call(self, mock_post):
        mock_post.return_value.json.return_value = {"choices": [{"text": "test"}]}
        client = CerebrasClient()
        response = client.generate_text("test")
        self.assertIn("choices", response)
