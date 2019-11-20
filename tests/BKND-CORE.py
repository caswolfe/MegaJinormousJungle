import json
import unittest
import logging
import sys

sys.path.append("../src/")

class MyTestCase(unittest.TestCase):


    @staticmethod
    def test_syntax():
        from PySyntaxHandler import Syntax
        syn = Syntax()
        assert syn
        assert len(syn.COLORS) >= len(syn.keyword_list)
        assert syn.assign_colors()
        assert len(syn.get_keywords()) > 0
        assert len(syn.get_color_dict()) > 0
    



if __name__ == '__main__':

    unittest.main()