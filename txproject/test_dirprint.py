import os
import shutil
import unittest

from printer import printDirectory

ROOT = os.path.dirname(os.path.abspath(__file__))

def writeTestFileToPath(path):
    testFileContents = "I am a test file."
    f = open(path, "w")
    f.write(testFileContents)
    f.close()


class TestEmptyDirectory(unittest.TestCase):
    def setUp(self):
        os.makedirs(os.path.join(ROOT,"testdir"))

    def tearDown(self):
        shutil.rmtree(os.path.join(ROOT,"testdir"))

    def test_dirprint(self):
        s = printDirectory(os.path.join(ROOT,"testdir"))
        expected = """testdir/"""
        print "expected:"
        print expected
        print "got:"
        print s
        self.assertEquals(expected, s)


class TestOneFileDirectory(unittest.TestCase):
    def setUp(self):
        os.makedirs(os.path.join(ROOT,"testdir"))
        testFiles = ["testdir/test1.txt",
                     ]
        for filePath in testFiles:
            writeTestFileToPath(os.path.join(ROOT, filePath))

    def tearDown(self):
        shutil.rmtree(os.path.join(ROOT,"testdir"))

    def test_dirprint(self):
        s = printDirectory(os.path.join(ROOT,"testdir"))
        expected = """testdir/
`-- test1.txt"""
        print "expected:"
        print expected
        print "got:"
        print s
        self.assertEquals(expected, s)


class TestTwoFileDirectory(unittest.TestCase):
    def setUp(self):
        os.makedirs(os.path.join(ROOT,"testdir"))
        testFiles = ["testdir/test1.txt",
                     "testdir/test2.txt",
                     ]
        for filePath in testFiles:
            writeTestFileToPath(os.path.join(ROOT, filePath))

    def tearDown(self):
        shutil.rmtree(os.path.join(ROOT,"testdir"))

    def test_dirprint(self):
        s = printDirectory(os.path.join(ROOT,"testdir"))
        expected = """testdir/
|-- test1.txt
`-- test2.txt"""
        print "expected:"
        print expected
        print "got:"
        print s
        self.assertEquals(expected, s)


class TestNestedDirectories(unittest.TestCase):
    def setUp(self):
        os.makedirs(os.path.join(ROOT,"testdir","subdir"))
        testFiles = ["testdir/subdir/test1.txt",
                     "testdir/subdir/test2.txt",
                     ]
        for filePath in testFiles:
            writeTestFileToPath(os.path.join(ROOT, filePath))

    def tearDown(self):
        shutil.rmtree(os.path.join(ROOT,"testdir"))

    def test_dirprint(self):
        s = printDirectory(os.path.join(ROOT,"testdir"))
        expected = """testdir/
`-- subdir/
    |-- test1.txt
    `-- test2.txt"""
        print "expected:"
        print expected
        print "got:"
        print s
        self.assertEquals(expected, s)


class TestNestedDirectoriesWithMultipleTopLevelFiles(unittest.TestCase):
    def setUp(self):
        os.makedirs(os.path.join(ROOT,"testdir","subdir"))
        testFiles = ["testdir/test1.txt",
                     "testdir/test2.txt",
                     "testdir/subdir/test3.txt",
                     "testdir/subdir/test4.txt",
                     ]
        for filePath in testFiles:
            writeTestFileToPath(os.path.join(ROOT, filePath))

    def tearDown(self):
        shutil.rmtree(os.path.join(ROOT,"testdir"))

    def test_dirprint(self):
        s = printDirectory(os.path.join(ROOT,"testdir"))
        expected = """testdir/
|-- subdir/
|   |-- test3.txt
|   `-- test4.txt
|-- test1.txt
`-- test2.txt"""
        print "expected:"
        print expected
        print "got:"
        print s
        self.assertEquals(expected, s)


class TestMultipleNestedDirectoriesMultipleFiles(unittest.TestCase):
    def setUp(self):
        os.makedirs(os.path.join(ROOT,"testdir","subdir1"))
        os.makedirs(os.path.join(ROOT,"testdir","subdir2"))
        testFiles = ["testdir/test1.txt",
                     "testdir/test2.txt",
                     "testdir/subdir1/test3.txt",
                     "testdir/subdir1/test4.txt",
                     "testdir/subdir2/test5.txt",
                     "testdir/subdir2/test6.txt",
                     ]
        for filePath in testFiles:
            writeTestFileToPath(os.path.join(ROOT, filePath))

    def tearDown(self):
        shutil.rmtree(os.path.join(ROOT,"testdir"))

    def test_dirprint(self):
        s = printDirectory(os.path.join(ROOT,"testdir"))
        expected = """testdir/
|-- subdir1/
|   |-- test3.txt
|   `-- test4.txt
|-- subdir2/
|   |-- test5.txt
|   `-- test6.txt
|-- test1.txt
`-- test2.txt"""
        print s
        self.assertEquals(expected, s)


class TestTwistedSinglePlugin(unittest.TestCase):
    def setUp(self):
        os.makedirs(os.path.join(ROOT,"testdir","test","web"))
        os.makedirs(os.path.join(ROOT,"testdir","twisted","plugins"))
        testFiles = ["testdir/test1.txt",
                     "testdir/test2.txt",
                     "testdir/test/__init__.py",
                     "testdir/test/web/__init__.py",
                     "testdir/test/web/root.py",
                     "testdir/twisted/plugins/testplugin.py",
                     ]
        for filePath in testFiles:
            writeTestFileToPath(os.path.join(ROOT, filePath))

    def tearDown(self):
        shutil.rmtree(os.path.join(ROOT,"testdir"))

    def test_dirprint(self):
        s = printDirectory(os.path.join(ROOT,"testdir"))
        expected = """testdir/
|-- test/
|   |-- __init__.py
|   `-- web/
|       |-- __init__.py
|       `-- root.py
|-- test1.txt
|-- test2.txt
`-- twisted/
    `-- plugins/
        `-- testplugin.py"""
        print "expected", expected
        self.assertEquals(expected, s)
