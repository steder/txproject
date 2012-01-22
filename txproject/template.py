#-*- test-case-name: txproject.test_template -*-
"""
Reads a template into memory
"""

import os
try:
    import json
except ImportError:
    import simplejson as json



DEFAULT_TEMPLATE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")


class Template(object):
    def __init__(self, name, template_data):
        self.name = name
        self.template_data = template_data

    def directories(self):
        """Returns a list of directories to be
        created as part of this template

        """
        return self.template_data["directories"]

    def files(self):
        """Returns a list of files to be created
        as part of this template

        """
        return self.template_data["files"]


class TemplateRegistry(object):
    """Contains lookup table of all available
    templates.  Can be asked to provide
    an entire template configuration and data

    """
    def __init__(self, template_dir=DEFAULT_TEMPLATE_DIR):
        self.template_dir = template_dir
        self.templates = {}
        if self.template_dir is not None:
            tocFile = open(os.path.join(self.template_dir, "index.json"), "r")
            toc = json.load(
                tocFile
            )
            for templateName in toc:
                self.templates[templateName] = Template(templateName, toc[templateName])
