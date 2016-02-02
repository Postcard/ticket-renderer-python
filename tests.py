import unittest
from datetime import datetime

from ticketrenderer import TicketRenderer


class TestTicketRenderer(unittest.TestCase):

    def setUp(self):
        html = '{{picture}} {{code}} {{datetime | datetimeformat}} ' \
               '{{textvariable_1}} {{imagevariable_2}} ' \
               '{{image_3}}'
        texts = ['Titi', 'Vicky', 'Benni']
        text_variables = [{'id': '1', 'items': texts}]

        items = [
            {
                'id': '1',
                'name': 'image1'

            },
            {
                'id': '2',
                'name': 'image2'
            }
        ]

        image_variables = [{'id': '2', 'items': items}]
        images = [{'id': '3', 'name': 'image3'}]

        self.template = {
            'html': html,
            'images': images,
            'image_variables': image_variables,
            'text_variables': text_variables,
            'title': 'title',
            'subtitle': 'subtitle'
        }

        self.media_url = 'http://media'
        self.css_url = 'http://static/ticket.css'
        self.ticket_renderer = TicketRenderer(self.template, self.media_url, self.css_url)


    def test_render(self):
        code = 'SJ98H'
        date = datetime(2016, 01, 01)
        picture = 'http://path/to/picture'
        rendered = self.ticket_renderer.render(code=code, date=date, picture=picture)
        self.assertIn("http://path/to/picture", rendered)
        self.assertIn(code, rendered)
        self.assertIn("http://static/ticket.css", rendered)
        self.assertTrue("Titi" in rendered or "Vicky" in rendered or "Benni" in rendered)
        self.assertTrue("http://media/images/image1" in rendered or "http://media/images/image2" in rendered)
        self.assertTrue("http://media/images/image3" in rendered)


if __name__ == '__main__':
    unittest.main()




