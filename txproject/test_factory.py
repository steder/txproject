import os
import shutil
import unittest

from txproject import factory


ROOT = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "testdirs"
)


class MockTemplate(object):
    def __init__(self, directories=[], files=[]):
        self._directories = directories
        self._files = files

    def directories(self):
        return self._directories

    def files(self):
        return self._files


class TestNewProjectFactory(unittest.TestCase):
    def setUp(self):
        self.f = factory.NewProject("testproject", "default", root=ROOT)
        self.f.getTemplate = self.mockGetTemplate

    def mockGetTemplate(self):
        m = MockTemplate(directories=["bin",
                                      "<project>",
                                      "test",
                                      "twisted/plugins"],
                         files=[{"<project>/web.py":""},
                                {"test/test_web.py":""},
                                {"twisted/plugins/<project>_plugin.py":""}]
                         )
        return m

    def test_projectName(self):
        self.assertEquals("Testproject", self.f.projectName())

    def test_directories(self):
        dirs = self.f.directories()
        self.assertEquals(["bin", "testproject", "test", "twisted/plugins"],
                          dirs,
                          "expect this list of dirs with substitutions")

    def test_files(self):
        files = self.f.files()
        self.assertEquals(["testproject/web.py",
                           "test/test_web.py",
                           "twisted/plugins/testproject_plugin.py"],
                           files,
                          "expect this list of files with substitutions")


class TestCreatingDirectories(unittest.TestCase):
    def setUp(self):
        self.tearDown()
        os.makedirs(ROOT)
        f = factory.NewProject("testproject", "default", root=ROOT)
        f.getTemplate = self.mockGetTemplate
        f.makeDirectories()

    def mockGetTemplate(self):
        m = MockTemplate(directories=["bin",
                                      "<project>",
                                      "test",
                                      "twisted/plugins"],
                         files=[])
        return m

    def tearDown(self):
        if os.path.exists(ROOT):
            shutil.rmtree(ROOT)

    def test_bin(self):
        self.assertTrue(os.path.exists(
                os.path.join(ROOT, "Testproject", "bin")
            ),
            "project should contain a bin directory"        
        )

    def test_project(self):
        self.assertTrue(os.path.exists(
                os.path.join(ROOT, "Testproject", "testproject")
            ),
            "project should contain project subdirectory"
        )

    def test_testDir(self):
        self.assertTrue(os.path.exists(
                        os.path.join(ROOT, "Testproject", "test")
                        ),
                        "project should contain test directory"
                        )

    def test_plugins(self):
        self.assertTrue(os.path.exists(
            os.path.join(ROOT, "Testproject", "twisted", "plugins")
            ),
                        "project should contain twisted/plugins directory"
                        )
        

class TestCreatingDirectoriesAndFiles(unittest.TestCase):
    def setUp(self):
        self.tearDown()
        os.makedirs(ROOT)
        newfile1 = open(os.path.join(ROOT, "testfile1.py"), "w")
        newfile1.write("# __init__.py default Default 1\n")
        newfile1.close()
        newfile2 = open(os.path.join(ROOT, "testfile2.py"), "w")
        newfile2.write("# __init__.py 2\n")
        newfile2.close()
        f = factory.NewProject("testproject", "default", root=ROOT, templateRoot=ROOT)
        f.getTemplate = self.mockGetTemplate
        f.makeDirectories()
        f.makeFiles()

    def mockGetTemplate(self):
        m = MockTemplate(directories=["bin",
                                      "<project>",
                                      "test",
                                      "twisted/plugins"],
                         files=[{"<project>/web.py":"testfile1.py"},
                                {"test/test_web.py":"testfile2.py"},
                                {"twisted/plugins/<project>_plugin.py":"testfile1.py"}]
                         )
        return m

    def tearDown(self):
        if os.path.exists(ROOT):
            shutil.rmtree(ROOT)

    def test_tests(self):
        self.assertTrue(
            os.path.exists(
                os.path.join(ROOT, "Testproject", "test", "test_web.py")
            ),
            "There should be a test_web.py file"
        )

    def test_web(self):
        self.assertTrue(
            os.path.exists(
                os.path.join(ROOT, "Testproject",
                             "testproject", "web.py")
            ),
            "There should be a web.py file"
        )

    def test_plugin(self):
        self.assertTrue(
            os.path.exists(
                os.path.join(ROOT, "Testproject",
                             "twisted", "plugins",
                             "testproject_plugin.py")
            ),
            "There should be a web.py file"
        )

    def test_tests_contents(self):
        f = open(os.path.join(ROOT, "Testproject", "test", "test_web.py"),"r")
        contents = f.read()
        self.assertEquals("# __init__.py 2\n", contents)

    def test_web_contents_substitution(self):
        f = open(os.path.join(ROOT, "Testproject",
                     "testproject", "web.py"), "r")
        contents = f.read()
        self.assertEquals("# __init__.py testproject Testproject 1\n", contents)
