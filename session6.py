'''
About closures
'''
def check_func_doc_string(fn : 'function') -> 'closure\'s inner function':
    '''
    This function checks the input function's doc string length is
    atleast 50 characters long.

    Input:
        fn: function

    Returns:
        function - inner function which checks doc string.
    '''
    min_doc_str_size = 50 

    if not callable(fn):
        raise TypeError(f'The input {fn} is not a function.')

    def check_doc_string() -> bool:
        '''
        This inner function checks the input functions doc string length.
        Returns
            True - if it is/more than min_doc_str_size.
            False - otherwise
        '''
        if len(fn.__doc__) >= min_doc_str_size:
            print(f'check_doc_string: doc str len - {len(fn.__doc__)}')
            print(f'{fn.__doc__}')
            return True
        else:
            return False

    return check_doc_string

def gen_fibonacci_num() -> 'closure function':
    '''
    This is a closure function, which generates the fibonacci numbers.

    Input: 
        None

    Returns:
        closure function - on invocation generates next fibonacci number.
    '''
    fib_num = 1
    prev_fib_num = 0
    is_first = True

    def next_fibonacci_num() -> int:
        '''
        generate the next fibonacci number.
        '''
        nonlocal fib_num, prev_fib_num, is_first
        if is_first:
            # reset the flag
            is_first = False
            return fib_num
        else:
            # generate the next fib num
            temp = fib_num
            fib_num = fib_num + prev_fib_num
            prev_fib_num = temp
            return fib_num

    return next_fibonacci_num

## counter for add / mult / div functions
def add(x, y):
    '''
    Function which adds two numbers.
    '''
    return x + y

def mult(x, y):
    '''
    Function which multiplies two numbers.
    '''
    return x * y

def div(x, y):
    '''
    Function which divides two numbers.
    '''
    if y == 0:
        raise ValueError('The denominator can not be zero!')
    else:
        return x/y

counter_dict = dict()

def counter(fn : 'function'):
    '''
    This is a closure function to track how many times a function is called.

    Input: 
        fn : function which needs to tracked

    Returns:
        inner closure function.
    '''
    cnt = 0

    def inner(*args, **kwargs):
        nonlocal cnt
        cnt += 1
        counter_dict[fn.__name__] = cnt
        return fn(*args, **kwargs)

    return inner

#### counter with dictionary passed in #######

def counter_with_dict(fn : 'function', cnt_dict: 'dict'):
    '''
    This is a counter wrapper which can take the dictionary.
    This updates the passed in dictionary with the number of times 
    the input function being called.

    Inputs:
        fn : function to be tracked
        cnt_dict: dictionary to store count

    Returns:
        inner closure function
    '''
    if type(cnt_dict) is not dict:
        raise TypeError(f'The input {cnt_dict} is not a dictionary type.')

    if callable(fn) == False:
        raise TypeError(f'The input {fn} is not a function!')

    cnt = 0
    def inner(*args, **kwargs):
        nonlocal cnt

        cnt += 1
        cnt_dict[fn.__name__] = cnt
        return fn(*args, **kwargs)

    return inner
