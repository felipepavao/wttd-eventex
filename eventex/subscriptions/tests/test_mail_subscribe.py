from django.core import mail
from django.test import TestCase

class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Felipe Pavão', cpf='12345678901',
            email='contact@felipepavao.com', phone='21-98369-5365')
        self.resp = self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'contact@felipepavao.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Felipe Pavão',
            '12345678901',
            'contact@felipepavao.com',
            '21-98369-5365'          
        ]
        for content in contents:
            if self.subTest():
                self.assertIn(content, self.email.body)
