from unittest.async_case import IsolatedAsyncioTestCase

from amsterdam_mail_service_client import Configuration, ApiClient, DefaultApi, SendRequest


class TestSend(IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        self.configuration = Configuration(host="http://amsterdam-mail-service:8003")

    async def test_send(self) -> None:
        async with ApiClient(self.configuration) as api_client:
            api = DefaultApi(api_client)
            request = SendRequest(
                title="Test Send",
                preview_text="Preview Text",
                body_text="Body Text",
                var_from="me@example.com",
                to="you@example.com",
                subject="Subject",
            )

            response = await api.send(request)

        self.assertEqual(response.message, "Mail sent successfully!")
