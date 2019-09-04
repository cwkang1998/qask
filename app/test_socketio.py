# import unittest
# import coverage
# from app import create_app, create_socketio
# from app.config import Config
#
# cov = coverage.coverage(branch=True)
# cov.start()
#
# app = create_app(Config)
# socketio = create_socketio(app)
#
#
# class TestSocketIO(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         pass
#
#     @classmethod
#     def tearDownClass(cls):
#         cov.stop()
#         cov.report(include="app/*", show_missing=True)
#
#     def setUp(self):
#         pass
#
#     def tearDown(self):
#         pass
#
#     def test_connect(self):
#         connect_header = {
#             "room": 2,
#             "session_hash": 5
#         }
#         client = socketio.test_client(app, namespace="/message/socket", headers=connect_header)
#         self.assertTrue(client.is_connected)
#         received = client.get_received()
#         print(received)
#         self.assertEqual(len(received), 1)
#         client.disconnect()
#
# if __name__ == '__main__':
#     unittest.main()
