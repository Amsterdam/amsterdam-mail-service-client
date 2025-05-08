from unittest.async_case import IsolatedAsyncioTestCase

from amsterdam_mail_service_client import Configuration, ApiClient, DefaultApi, PreviewRequest


class TestPreview(IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        self.configuration = Configuration(host="http://amsterdam-mail-service:8003")

    async def test_preview(self) -> None:
        async with ApiClient(self.configuration) as api_client:
            api = DefaultApi(api_client)
            request = PreviewRequest(
                title="Test Preview",
                preview_text="Preview Text",
                body_text="Body Text",
            )

            response = await api.preview(request)

        self.assertIsInstance(response, str)
