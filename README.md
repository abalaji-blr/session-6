# S6 - Closures in Python

### About Nonlocal scope

In the case of **nested functions**, the **inner function** has access to the scope which is **neither local** nor **global**, that is it has access to **outer function's scope variables**, they are called as **non local scope** (with respect to inner function).

### About Closures

Closure is a phenomenon with nested functions, where the inner function uses or references the enclosing scope's variables, also known as **nonlocal scope variable**. Then, the **outer function exposes the inner function to the external world by returning it**.

Closures also **provides a way of data hiding and avoids global scope**.

Closures are alternate to **small classes** - that is, classes with just one or two methods / data.

### Requirement for Closure

	* Being a nested function
	* Use nonlocal scope also known as **free variable**.
	* Return inner function

### Overview of Assignment

The assignment is about implementing the following functions as a closure.

* **check_func_doc_string**

  ```
  check_func_doc_string(fn: 'function') -> "closure's inner function"
      This function checks the input function's doc string length is
      atleast 50 characters long.
      
      Input:
          fn: function
      
      Returns:
          function - inner function which checks doc string.
  ```

  ```
  Usage:
  def temp_func():
      '''
      This is a temporary function.
      '''
      pass
      
  # get the closure
  check_doc_string = check_func_doc_string(temp_func)
  
  # invoke closure
  print(check_doc_string())
  ```

  

* **gen_fibonacci_num**

  ```
  gen_fibonacci_num() -> 'closure function'
      This is a closure function, which generates the fibonacci numbers.
      
      Input: 
          None
      
      Returns:
          closure function - on invocation generates next fibonacci number.
  ```

  

* **counter** - to track how many times the function being called using global dictionary.

  ```
  add(x, y)
      Function which adds two numbers.
  ```

  ```
  mult(x, y)
      Function which multiplies two numbers.
  ```

  ```
  div(x, y)
      Function which divides two numbers.
  ```

  ```
  counter(fn: 'function')
      This is a closure function to track how many times a function is called.
      
      Input: 
          fn : function which needs to tracked
      
      Returns:
          inner closure function.
  
  ```

  

* **counter_with_dict**

  ```
  counter_with_dict(fn: 'function', cnt_dict: 'dict')
      This is a counter wrapper which can take the dictionary.
      This updates the passed in dictionary with the number of times 
      the input function being called.
      
      Inputs:
          fn : function to be tracked
          cnt_dict: dictionary to store count
      
      Returns:
          inner closure function
  ```



### Overview of Tests

The following tests checks for the following:

	* invalid arguments - TypeError, ValueError
	* Existence of doc string for a function
	* whether the **implementation is a closure or not**.
	* **functionality with valid arguments**.

## Test Results

```
collected 23 items                                                                                    

test_session6.py::test_session6_readme_exists PASSED                                            [  4%]
test_session6.py::test_session6_readme_500_words PASSED                                         [  8%]
test_session6.py::test_session6_readme_proper_description PASSED                                [ 13%]
test_session6.py::test_session6_readme_file_for_more_than_10_hashes PASSED                      [ 17%]
test_session6.py::test_session6_indentations PASSED                                             [ 21%]
test_session6.py::test_session6_function_name_had_cap_letter PASSED                             [ 26%]
test_session6.py::test_check_func_doc_string_no_args PASSED                                     [ 30%]
test_session6.py::test_check_func_doc_string_invalid_args PASSED                                [ 34%]
test_session6.py::test_check_func_doc_string_check_closure_or_not PASSED                        [ 39%]
test_session6.py::test_check_func_doc_string_check_results PASSED                               [ 43%]
test_session6.py::test_gen_fibonacci_num_closure_func_or_not PASSED                             [ 47%]
test_session6.py::test_gen_fibonacci_num_check_results PASSED                                   [ 52%]
test_session6.py::test_add PASSED                                                               [ 56%]
test_session6.py::test_mult PASSED                                                              [ 60%]
test_session6.py::test_div PASSED                                                               [ 65%]
test_session6.py::test_doc_string_for_counter_funcs PASSED                                      [ 69%]
test_session6.py::test_counter_for_closure PASSED                                               [ 73%]
test_session6.py::test_counter_for_validity PASSED                                              [ 78%]
test_session6.py::test_counter_with_dict_invalid_func PASSED                                    [ 82%]
test_session6.py::test_counter_with_dict_invalid_dict PASSED                                    [ 86%]
test_session6.py::test_counter_with_dict_for_doc_string PASSED                                  [ 91%]
test_session6.py::test_counter_with_dict_for_closure PASSED                                     [ 95%]
test_session6.py::test_counter_with_dict_for_validity PASSED                                    [100%]

====================================== 23 passed in 0.05 seconds ======================================
```

