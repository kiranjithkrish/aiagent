# tests.py

import unittest
import os
from functions.get_files_info import get_files_info, is_subdir
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from config import MAX_CHARS
from functions.run_python import run_python_file

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
        #print(res_str_one)
        res_str_Two = get_file_content(working_dir, mainFilePath)
        #print(res_str_Two)
        res_str_Three = get_file_content(working_dir, calculatorFilePath)
        #print(res_str_Three)
        res_str_Four = get_file_content(working_dir, catFilePath)
        #print(res_str_Four)
        res_str_Five = get_file_content(working_dir, doesNotExistPath)
        #print(res_str_Five)
        # self.assertIn("truncated at 10000 characters", res_str_one)
        # self.assertTrue(len(res_str_Two) < MAX_CHARS)
        # self.assertTrue(len(res_str_Three) < MAX_CHARS)
        # self.assertIn("Error:", res_str_Four)
        # self.assertIn("Error:", res_str_Five)
        # return_str_one = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
        # print(return_str_one)
        # retrun_str_two = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
        # print(retrun_str_two)
        # return_str_three = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
        # print(return_str_three)
        output_one = run_python_file("calculator", "main.py")
        print(output_one)
        
        output_two = run_python_file("calculator", "main.py", ["3 + 5"])
        print(output_two)
        
        output_three = run_python_file("calculator", "tests.py")
        print(output_three)
        
        output_four = run_python_file("calculator", "../main.py")
        print(output_four)
        
        output_five = run_python_file("calculator", "nonexistent.py")
        print(output_five)

        



    
            


if __name__ == "__main__":
    unittest.main()