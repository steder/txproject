import os
import unittest

from txproject import template

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "testingtemplates")

class TestTemplateRegistry(unittest.TestCase):
    def test_getEmptyTemplateRegistry(self):
        r = template.TemplateRegistry(template_dir=None)
        self.assertEquals(0, len(r.templates))

    def test_getSpecificTemplateRegistry(self):
        r = template.TemplateRegistry(template_dir=ROOT)
        self.assertEquals(1, len(r.templates))
        t = r.templates["test"]
        self.assertEquals("test", t.name)

    def test_getDefaultTemplateRegistry(self):
        r = template.TemplateRegistry()
        self.assertEquals(2, len(r.templates))
        

class TestTemplate(unittest.TestCase):
    def setUp(self):
        self.t = template.Template("test", {"directories":[],
                                            "files":[]})

    def test_name(self):
        self.assertEquals("test", self.t.name)

    def test_directories(self):
        self.assertEquals([], self.t.directories())

    def test_files(self):
        self.assertEquals([], self.t.files())

