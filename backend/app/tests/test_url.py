import json

from .base import BaseTestCase

class UrlsViewTest(BaseTestCase):

    def test_shortlink_creation(self):

        with self.client:

            test_url = {
                "url": "http://google.com"
            }

            response = self.client.post('/api/v1/shorturl', json=test_url)
            data = json.loads(response.data.decode())

            self.assertEqual(response.status_code, 201)
            self.assertEqual(data["data"]["slug"], "1")
            self.assertEqual(data["data"]["shortlink"], "http://localhost/1")
            self.assertEqual(data["status"], "success")
            self.assertEqual(data["data"]["url"], "http://google.com")

    def test_shortlink_exists(self):

        with self.client:

            test_url = {
                "url": "http://google.com"
            }

            response_1 = self.client.post('/api/v1/shorturl', json=test_url)

            self.assertEqual(response_1.status_code, 201)

            response_2 = self.client.post('/api/v1/shorturl', json=test_url)
            data  = json.loads(response_2.data.decode())
            
            self.assertEqual(response_2.status_code, 200)
            self.assertEqual(data["data"]["slug"], "1")
            self.assertEqual(data["data"]["shortlink"], "http://localhost/1")
            self.assertEqual(data["status"], "success")
            self.assertEqual(data["data"]["url"], "http://google.com")

    def test_creation_no_scheme(self):

        with self.client:
            
            test_url = {
                "url": "google.com"
            }
            
            response = self.client.post('/api/v1/shorturl', json=test_url)
            data = json.loads(response.data.decode())

            self.assertEqual(response.status_code, 400)
            self.assertEqual(data["message"], "Not a valid URL.")
            self.assertEqual(data["status"], 'fail')

    def test_creation_unsupported_scheme(self):

        with self.client:

            test_url = {
                "url": "ftp://innocent.co.ug/files"
            }

            response = self.client.post('/api/v1/shorturl', json=test_url)
            data = json.loads(response.data.decode())

            self.assertEqual(response.status_code, 400)
            self.assertEqual(data["message"], "Not a valid URL.")
            self.assertEqual(data["status"], 'fail')

    def test_creation_Invalid_domain(self):

        with self.client:

            test_url = {
                "url": "http://google"
            }

            response = self.client.post('/api/v1/shorturl', json=test_url)
            data = json.loads(response.data.decode())

            self.assertEqual(response.status_code, 400)
            self.assertEqual(data["status"], 'fail')
            self.assertEqual(data["message"], "Not a valid URL.")

    def test_creation_failure_no_url(self):

        with self.client:

            test_url = {
                
            }

            response = self.client.post('/api/v1/shorturl', json=test_url)
            data = json.loads(response.data.decode())

            self.assertEqual(response.status_code, 400)
            self.assertEqual(data["status"], 'fail')
            self.assertIn("Missing data", data['message'])


    def test_get_all_urls_success(self):

        with self.client:

            test_url_1 = {
                "url": "http://google.com/"
            }

            test_url_2 = {
                "url": "https://innocent.co.ug/very_long"
            }

            response_1 = self.client.post('/api/v1/shorturl', json=test_url_1)
            response_2 = self.client.post('/api/v1/shorturl', json=test_url_2)

            self.assertEqual(response_1.status_code, 201)
            self.assertEqual(response_1.status_code, 201)

            get_response = self.client.get('/api/v1/shorturl')
            data = json.loads(get_response.data.decode())

            self.assertEqual(get_response.status_code, 200)
            self.assertEqual(data["status"], "success")
            self.assertIsInstance(data["data"], list)
            self.assertEqual(len(data["data"]), 2)
            self.assertIn('shortlink', data["data"][0])
            self.assertIn('url', data["data"][0])
            










