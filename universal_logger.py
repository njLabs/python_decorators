
def log_decorator(func):
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
