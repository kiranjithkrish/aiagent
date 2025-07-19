# tests.py

import unittest
import tempfile
import os
from functions.get_files_info import get_files_info, is_subdir
from functions.get_file_content import get_file_content
from config import MAX_CHARS

class TestGetFileInfo(unittest.TestCase):

    # def test_is_subdir_true_or_false(self):
    #     with tempfile.TemporaryDirectory() as parent:
    #         child = os.path.join(parent, 'child')
    #         os.mkdir(child)
    #         self.assertTrue(is_subdir(parent, child))
    #         self.assertFalse(is_subdir(child, parent))
            
    # def test_get_file_info_success(self):
    #     working_dir = os.path.abspath('./calculator')
    #     sub_dir = os.path.join(working_dir, '.')
    #     res = get_files_info(working_dir, sub_dir)
    #     print(res)
    #     self.assertIn('main.py', res)
    #     self.assertIn('tests.py', res)
    #     self.assertIn('pkg', res)
    
    # def test_get_file_info_success_2(self):
    #     working_dir = os.path.abspath('./calculator')
    #     sub_dir = os.path.join(working_dir, 'pkg')
    #     res = get_files_info(working_dir, sub_dir)
    #     print(res)
    #     self.assertIn('calculator.py', res)
    #     self.assertIn('render.py', res)
    #     self.assertIn('__pycache__', res)
    
    # def test_get_file_info_fail_message_on_failure(self):
    #     working_dir = './calculator'
    #     sub_dir = '../'
    #     res = get_files_info(working_dir, sub_dir)
    #     print(f'fail test is : {res}')
    #     self.assertIn('Error: Cannot list "../" as', res)
        
    # def test_get_file_info_fail_message_on_failure_2(self):
    #     working_dir = './calculator'
    #     sub_dir = '/bin'
    #     res = get_files_info(working_dir, sub_dir)
    #     print(f'fail test is : {res}')
    #     self.assertIn(f'Error: Cannot list "/bin" as', res)

    def test_get_file_content(self):
        working_dir = './calculator'
        filePath = os.path.join(working_dir, "lorem.txt")
        mainFilePath = os.path.join(working_dir, "main.py")
        calculatorFilePath = os.path.join(working_dir, "pkg/calculator.py")
        catFilePath = os.path.join(working_dir, "/bin/cat")
        doesNotExistPath = os.path.join(working_dir, "pkg/does_not_exist.py")
        res_str_one = get_file_content(working_dir, filePath)
        print(res_str_one)
        res_str_Two = get_file_content(working_dir, mainFilePath)
        print(res_str_Two)
        res_str_Three = get_file_content(working_dir, calculatorFilePath)
        print(res_str_Three)
        res_str_Four = get_file_content(working_dir, catFilePath)
        print(res_str_Four)
        res_str_Five = get_file_content(working_dir, doesNotExistPath)
        print(res_str_Five)
        self.assertIn("truncated at 10000 characters", res_str_one)
        self.assertTrue(len(res_str_Two) < MAX_CHARS)
        self.assertTrue(len(res_str_Three) < MAX_CHARS)
        self.assertIn("Error:", res_str_Four)
        self.assertIn("Error:", res_str_Five)

        



    
            


if __name__ == "__main__":
    unittest.main()