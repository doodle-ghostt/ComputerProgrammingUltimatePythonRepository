import unittest
import yaml
import inspect
import main
import os

def test_function_definition(test_case, module, function_name, expected_num_args):
    # check the function is defined
    function_defined = hasattr(module, function_name)
    test_case.assertTrue(function_defined, f"{function_name} is not defined in {module.__name__}")

    # check the function takes correct # arguments
    function = getattr(module, function_name)
    signature = inspect.signature(function)
    num_arguments = len(signature.parameters)

    test_case.assertEqual(num_arguments, expected_num_args, f"{function_name} should take {expected_num_args} argument(s)")

def execute_test(test_case, module, function_name, data):
    test_function_definition(test_case, module, function_name, len(data[function_name][0]["input"]))
    func = getattr(module, function_name)
    for row in data[function_name]:
      with test_case.subTest(arguments=row["input"]):
          arguments = row["input"]
          expected_result = row["output"]
          result = func(*arguments)
          test_case.assertEqual(result, expected_result, f"{function_name}({', '.join(map(str, arguments))}) was expected to return:\n{expected_result}\nInstead, it returned:\n{result}\n")

class TestFunctions(unittest.TestCase):
    longMessage = False

    @classmethod
    def setUpClass(cls):
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        with open(os.path.join(__location__, "testing_data.yaml"), "r") as file:
            cls.data = yaml.safe_load(file)

    def test_is_alliteration(self):
        execute_test(self, main, "is_alliteration", self.data)

    def test_count_vowels(self):
        execute_test(self, main, "count_vowels", self.data)

    def test_count_numbers(self):
        execute_test(self, main, "count_numbers", self.data)

    def test_count_target_letters(self):
        execute_test(self, main, "count_target_letters", self.data)

    def test_in_alphabetical_order(self):
        execute_test(self, main, "in_alphabetical_order", self.data)

<<<<<<< HEAD
    def test_alternate_case(self):
=======
    def test_alterate_case(self):
>>>>>>> 518ec80c134dadfea8b8245dee4298db0f7b5626
        execute_test(self, main, "alternate_case", self.data)

    def test_remove_vowels(self):
        execute_test(self, main, "remove_vowels", self.data)
    
    def test_to_camel_case(self):
        execute_test(self, main, "to_camel_case", self.data)

    def test_to_snake_case(self):
        execute_test(self, main, "to_snake_case", self.data)
    
    def test_without_duplicates(self):
        execute_test(self, main, "without_duplicates", self.data)
    
    def test_filter_valid_act_scores(self):
        execute_test(self, main, "filter_valid_act_scores", self.data)

    
if __name__ == '__main__':
    unittest.main(verbosity=2, exit=False, catchbreak=False)
