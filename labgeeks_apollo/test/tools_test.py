""" Tests the existence and functionality of all Tools forms"""

from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import *
from forms_builder.forms.models import *

class ToolsTestCase(TestCase):

    def setUp(self):
        """
        Prepares DB for testing tools
        """
        self._site = Site.objects.get_current()
        self.closing = Form.objects.create(title="Closing Procedures", slug='closing-procedures', id=1, status=STATUS_PUBLISHED)
        self.closing.sites.add(self._site)
        self.closing.save()
        self.printer = Form.objects.create(title="Printer Issues", slug='printer-issue', id=2, status=STATUS_PUBLISHED)
        self.printer.sites.add(self._site)
        self.printer.save()
        self.login = Form.objects.create(title="Login Issues", slug='login-issue', id=3, status=STATUS_PUBLISHED)
        self.login.sites.add(self._site)
        self.login.save()
        self.dude = User.objects.create_user('Dude', 'dude@dude.com', 'dude')
        self.dude.save()

    def testToolsExist(self):
        """
        Tests that each tool exists and is available to a logged in user at the correct URLs
        """
        c = Client()
        c.login(username="Dude", password='dude')
        response = c.get('/tools/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Closing Procedures")
        response2 = c.get('/tools/2/')
        self.assertEqual(response2.status_code, 200)
        self.assertContains(response2, "Printer Issues")
        response3 = c.get('/tools/3/')
        self.assertEqual(response3.status_code, 200)
        self.assertContains(response3, "Login Issues")
        response4 = c.get('/tools/')
        self.assertEqual(response4.status_code, 200)
        self.assertContains(response4, "Closing Procedures")
        self.assertContains(response4, "Printer Issues")
        self.assertContains(response4, "Login Issues")
        c.logout()
