import unittest

from app import build_response


class TestApp(unittest.TestCase):
    def test_health(self):
        self.assertEqual(build_response("/health"), (200, {"status": "ok"}))

    def test_version_default(self):
        status, body = build_response("/version")
        self.assertEqual(status, 200)
        self.assertIn("version", body)

    def test_unknown(self):
        self.assertEqual(build_response("/nope")[0], 404)


if __name__ == "__main__":
    unittest.main()