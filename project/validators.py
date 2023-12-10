from rest_framework.serializers import ValidationError
import re


class YouTubeLinksOnly:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        args = dict(value).get(self.field)

        link = r'https?://\S+|www\.\S+'
        url = r'(?:https?://)?(?:www\.)?youtube\.com'

        full_links = re.findall(link, args)

        for link in full_links:
            if not bool(re.match(url, link)):
                raise ValidationError("Используются недопустимая ссылка")
