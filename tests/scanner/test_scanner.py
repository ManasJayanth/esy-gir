import unittest
import optparse
import os

from giscanner.scannermain import get_source_root_dirs


class TestScanner(unittest.TestCase):

    def test_get_source_root_dirs_options(self):
        options = optparse.Values({"sources_top_dirs": ["foo"]})
        paths = get_source_root_dirs(options, ["nope"])
        self.assertEqual(len(paths), 1)
        self.assertTrue(os.path.isabs(paths[0]))
        self.assertEqual(paths[0], os.path.join(os.getcwd(), "foo"))

    def test_get_source_root_dirs_guess(self):
        options = optparse.Values({"sources_top_dirs": []})
        cwd = os.getcwd()
        paths = get_source_root_dirs(
            options, [os.path.join(cwd, "foo"), os.path.join(cwd, "bar")])
        self.assertEqual(len(paths), 1)
        self.assertEqual(paths[0], cwd)

        paths = get_source_root_dirs(options, [])
        self.assertEqual(paths, [])


if __name__ == '__main__':
    unittest.main()
