#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django_eulasees
------------

Tests for `django_eulasees` api module.
"""

import os
import shutil
import unittest
import datetime
from unittest.mock import Mock, MagicMock

from rest_framework.test import APIRequestFactory

from django_eulasees import models
from django_eulasees import api


class TestDjango_eulasees(unittest.TestCase):

    def setUp(self):
        """ Create some data """
        eula = models.RawEula()
        eula.text = "we own you"
        eula.site = "weownu.com"
        eula.url = ""
        eula.date = datetime.date.today()
        eula.save()

        eula = models.RawEula()
        eula.text = "we love you"
        eula.site = "welvoveu.bm"
        eula.url = ""
        eula.date = datetime.date.today()
        eula.save()

        # Snippets
        snippet = models.EulaSnippet()
        snippet.title + "Feel the love"
        snippet.text = "We really do love you"
        snippet.start = 0
        snippet.end = 0
        snippet.eula = eula
        snippet.save()

        # Tag
        tag = models.Tag()
        tag.name = "One Love"
        tag.description = "This site loves its users"
        tag.save()

        snippettag = models.SnippetTag()
        snippettag.tag = tag
        snippettag.snippet = snippet
        snippettag.save()

    def test_eulasfortag(self):

        factory = APIRequestFactory()
        tag = models.Tag.objects.all()[0]
        request = factory.post('/eulasfortag/', {'pk': tag.pk}, format='json')


    def tearDown(self):
        pass
