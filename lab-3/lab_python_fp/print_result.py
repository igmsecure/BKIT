def print_result(function):
    def decorated_func(*args):
        print(function.__name__)
        res = function(*args)
        if type(res) == list:
            for i in res:
                print(i)
        elif type(res) == dict:
            for i in res.keys():
                print(i, ' = ', res[i])
        else:
            print(res)
        return res
    return decorated_func