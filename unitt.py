import unittest

import time


class Parent(object):
    def __init__(self):
        self.parent_var=None
        self.file="tmp.file"

    def read_file_right(self,path):
        cur_time=time.time()

    def read_file_except(self,path):
        with open(self._already_installed_file,"wb") as output:
            cur_time=time.time()
            output.write(cur_time)

    def can_not_import(self):
        sys.exit(3)

class Test(unittest.TestCase):
    #@unittest.expectedFailure
    def test_read_file_except(self):
        p=Parent()
        p.read_file_except()
        self.assert_(True)

    def test_read_file_right(self):
        p=Parent()
        p.read_file_right("tsets")
        self.assert_(True)

    def test_exception_is_valid(self):
        try:
            p=Parent()
            p.can_not_import()
            self.assert_(False)
        except:
            self.assert_(True)

    @unittest.expectedFailure
    def test_expected_failure(self):
        raise Exception("test exception")

    def test_unexpected_failure(self):
        raise Exception("test unexpected exception")


if __name__ == "__main__":
    unittest.main()
