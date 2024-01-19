import time


def time_it(func):
    """
    timing decorator
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time-start_time} seconds")
        return result
    return wrapper


def log_decorator(func):
    """
    log input and outpt of a definition
    """

    def wrapper(*args, **kwargs):
        function_name = func.__name__
        args_info = args
        kwargs_info = kwargs
        returned = func(*args, **kwargs)
        # Log the function call information
        logging.info(f"Calling function '{function_name}' with args: {args_info} and kwargs: {kwargs_info}")
        logging.info(f"Calling function '{function_name}' and return {returned}")

        return func(*args, **kwargs)

    return wrapper
