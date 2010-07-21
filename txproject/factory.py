#-*- test-case-name: txproject.test_factory -*-
"""
defines project factory

The project factory is responsible for loading a project template and
creating a project directory with the specified template and project name.

"""

import os

from txproject import template


class NewProject(object):
    def __init__(self, projectName, templateName, root=".", templateRoot=template.DEFAULT_TEMPLATE_DIR):
        self.name = projectName.lower()
        self.templateName = templateName
        self._template = None
        self.root = root
        self.templateRoot = templateRoot
        
    def getTemplate(self):
        """Loads template *self.templateName*

        """
        if self._template is None:
            r = template.TemplateRegistry()
            self._template = r.templates[self.templateName]
        return self._template

    def projectName(self):
        return self.name.capitalize()

    def directories(self):
        dirs = []
        for dir in self.getTemplate().directories():
            d = dir.replace("<project>", self.name)
            dirs.append(d)
        return dirs

    def files(self):
        files = []
        for f in self.getTemplate().files():
            for path, realPath in f.iteritems():
                nf = path.replace("<project>", self.name)
                files.append(nf)
        return files

    def makeDirectories(self):
        for d in self.directories():
            path = os.path.join(self.root,
                             self.projectName(),
                             d)
            os.makedirs(path)
            
    def makeFiles(self):
        for templateFile in self.getTemplate().files():
            for f, realPath in templateFile.iteritems():
                f = f.replace("<project>", self.name)
                realPath = realPath.replace("<project>", self.name)
                path = os.path.join(self.root,
                                    self.projectName(),
                                    f)
                contents = open(os.path.join(self.templateRoot, realPath), "r").read()
                contents = contents.replace(self.templateName.capitalize(), self.projectName())
                contents = contents.replace(self.templateName, self.name)
                o = open(path, "w")
                o.write(contents)
                o.close()
            
