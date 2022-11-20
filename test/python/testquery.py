"""
Query module tests
"""

import unittest

from contextlib import redirect_stdout

from paperai.query import Query

# pylint: disable=C0411
from utils import Utils


class TestQuery(unittest.TestCase):
    """
    Query tests
    """

    def testRun(self):
        """
        Test query execution
        """

        # Execute query
        with open(
            Utils.PATH + "/query.txt", "w", newline="\n", encoding="utf-8"
        ) as query:
            with redirect_stdout(query):
                Query.run("risk factors studied", 10, Utils.PATH)

        self.assertEqual(
            Utils.hashfile(Utils.PATH + "/query.txt"),
            "0413b97092f4ea58f7b15750582c4ad2",
        )
