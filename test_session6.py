import pytest
from session6 import *
import session6
import os # path
import string
import re
import inspect # to get files




#################### Tests about README.md ################
README_CONTENT_CHECK_FOR = [
    'check_func_doc_string',
]


def test_session6_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_session6_readme_500_words():
    readme = open("README.md", 'r')
    # get the words
    readme_words = readme.read().split()
    readme.close()
    assert len(
        readme_words) > 500, "Make your README.md file interesting! Add atleast 500 words"

def test_session6_readme_proper_description():
    # read the file
    file = open("README.md", "r", encoding="utf-8")
    content = file.read()
    file.close()
    # examine the contents
    READMELOOKSGOOD = True
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass

    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"


def test_session6_readme_file_for_more_than_10_hashes():
    file = open("README.md", "r", encoding="utf-8")
    content = file.read()
    file.close()
    assert content.count('#') > 10, "Your README file is not well formatted."


def test_session6_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
      significant indenting.'''
    # get the session6 python file
    lines = inspect.getsource(session6)

    #get the leading spaces for each line  using regular expr.
    spaces = re.findall('\n +.', lines)
    cnt = 0
    for space in spaces:
        cnt += 1
        print(f'space: {space}, line: {cnt}')
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(
            r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"


def test_session6_function_name_had_cap_letter():
    # get the function names
    func_names = inspect.getmembers(session6, inspect.isfunction)
    for name in func_names:
        assert len(re.findall(
            '([A-Z])', name[0])) == 0, "You have used Capital letter(s) in your function names"

################# Assignment Validation #################

######### check doc string ###################
def test_check_func_doc_string_no_args():
    with pytest.raises(TypeError, match= r".*required positional argument:.*"):
        session6.check_func_doc_string()

def test_check_func_doc_string_invalid_args():
    with pytest.raises(TypeError, match=r".* is not a function.*"):
        session6.check_func_doc_string("abc")

def temp_func():
    '''
    This is a temporary function.
    '''
    pass

def temp2_func():
    '''
    This is a temporary function to validation the closure which checks the length of the doc string.
    '''
    pass

def test_check_func_doc_string_check_closure_or_not():
    '''
    Check whether the function is closure or not.
    '''
    check_doc_string = session6.check_func_doc_string(temp_func)
    assert len(check_doc_string.__closure__) > 0, 'The implementation is NOT a closure.'

def test_check_func_doc_string_check_results():
    # get the closure function
    check_doc_string = session6.check_func_doc_string(temp_func)
    print(check_doc_string())

    # check the functionality by examing the return results.
    assert check_doc_string() == False, 'The expected return value is False.'
    
    assert session6.check_func_doc_string(temp2_func)() == True, 'The expected return value is True.'

#######################################################################
############# Fibonacci Number #########

def test_gen_fibonacci_num_closure_func_or_not():
    fib = session6.gen_fibonacci_num()
    assert len(fib.__closure__) > 0, 'The implementation is NOT a closure function!'

def test_gen_fibonacci_num_check_results():
    fib = session6.gen_fibonacci_num()
    assert (fib(), fib(), fib(), fib(), fib(), fib(), fib()) == (1, 1, 2, 3, 5, 8, 13), \
        'The Fibonacci numbers are NOT generated correctly.'
#######################################################################
############# Counter for add / mult / div #########

def test_add():
    assert session6.add(5, 8) == 13, 'The add function fails!'

def test_mult():
    assert session6.mult(8,9) == 72, 'The mult function fails!'

def test_div():
    with pytest.raises(ValueError, match=".* denominator can not be zero.*"):
        session6.div(8,0)
    assert session6.div(8, 4) == 2, 'The div function fails!'

def test_doc_string_for_counter_funcs():
    assert bool(session6.add.__doc__) == True, "No Doc string defined in function - add."
    assert bool(session6.mult.__doc__) == True, "No Doc string defined in function - mult."
    assert bool(session6.div.__doc__) == True, "No Doc string defined in function - div."
    assert bool(session6.counter.__doc__) == True, "No Doc string defined in function - counter."

def test_counter_for_closure():
    cnt_add = session6.counter(session6.add)
    assert bool(cnt_add.__closure__) == True, "Counter is not implemented as Closure function!"

def test_counter_for_validity():
    cnt_add = session6.counter(session6.add)
    cnt_mult = session6.counter(session6.mult)
    cnt_div  = session6.counter(session6.div)
    [cnt_add(3, 4) for _ in range(4)]
    [cnt_mult(3, 4) for _ in range(3)]
    [cnt_div(8, 2) for _ in range(2)]

    test_dict = { 'add': 4, 'mult': 3, 'div': 2}
    assert session6.counter_dict == test_dict, 'The counter is NOT working as expected!'


#######################################################################
############# counter with dictionary passed in #########

def test_counter_with_dict_invalid_func():
    test_dict = dict()
    with pytest.raises(TypeError, match=".* not a function.*"):
        session6.counter_with_dict("abc", test_dict)

def test_counter_with_dict_invalid_dict():
    temp_var = 10
    with pytest.raises(TypeError, match=".* not a dictionary.*"):
        session6.counter_with_dict(session6.add, temp_var)

def test_counter_with_dict_for_doc_string():
    temp_dict = dict()
    assert bool(session6.counter_with_dict.__doc__) == True, "No document string found."

def test_counter_with_dict_for_closure():
    temp_dict = dict()
    add_cnt = session6.counter_with_dict(session6.add, temp_dict)
    assert bool(add_cnt.__closure__) == True, "Counter is not implemented as closure!"


def test_counter_with_dict_for_validity():
    dict1 = dict()
    dict2 = dict()

    # get the closures
    add1 = session6.counter_with_dict(add, dict1)
    mult1 = session6.counter_with_dict(mult, dict1)
    div1 = session6.counter_with_dict(div, dict1)

    [add1(20, 40) for _ in range(5)]
    [mult1(9, 5) for _ in range(4)]
    [div1(9, 4) for _ in range(3)]

    temp_dict1 = { 'add': 5, 'mult': 4, 'div': 3}
    assert dict1 == temp_dict1, "Counter with dictionary is not working as expected!"

    # get the closures with different dictionary
    add2 = session6.counter_with_dict(add, dict2)
    mult2 = session6.counter_with_dict(mult, dict2)
    div2 = session6.counter_with_dict(div, dict2)

    [add2(30, 40) for _ in range(4)]
    [mult2(30, 40) for _ in range(3)]
    [div2(40, 30) for _ in range(2)]

    temp_dict2 = {'add': 4, 'mult': 3, 'div': 2}
    assert dict2 == temp_dict2, "Counter with dictionary is not working as expected!"
