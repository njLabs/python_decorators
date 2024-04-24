import time
import cProfile
import pstats
import io


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


def profile(fnc):
    """
    Profiles any function in following class just by adding @profile above function
    """
    def inner(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        retval = fnc(*args, **kwargs)
        pr.disable()
        s = io.StringIO()
        sortby = 'cumulative'  # Ordered
        ps = pstats.Stats(pr, stream=s).strip_dirs().sort_stats(sortby)
        n = 10  # reduced the list to be monitored
        ps.print_stats(n)
        # ps.dump_stats("profile.prof")
        print(s.getvalue())
        return retval

    return inner
