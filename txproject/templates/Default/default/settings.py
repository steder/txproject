"""Settings for Default

"""

from twisted.python import filepath

default_root = filepath.FilePath(__file__).parent().parent()
    
hostname = "localhost"
port = 7777

