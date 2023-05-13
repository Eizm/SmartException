import re

class SmartException:
    """
    Currently supports (if error appears in the file where the context manager is)  TODO: include support for errors in imported modules
        KeyError for dict and pandas DataFrame
        IndexError
        AttributeError
    
    """

    def __init__(self):
        pass
    
    def __enter__(self):
        pass
    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            l = self.get_line(traceback.tb_lineno)
            if exc_type == KeyError:
                failkey = str(exc_value).strip()
                variable = re.findall(r"([a-zA-Z0-9]+)\[", l)[0]
                print()
                print("Error trying to index the following variable")
                print(eval(variable))
                print("Which has the following keys")
                print(eval(variable).keys())
            if exc_type == IndexError:
                variables = re.findall(r"([a-zA-Z0-9]+)\[", l)
                const_indexes = re.findall(r"\[(\d)\]", l)
                var_indexes = re.findall(r"\[([a-zA-Z0-9]+)\]", l)
                print()
                print("Error trying to index the following variable(s)")
                for var in variables:
                    print(eval(var))
                print("with the following constant index(es)")
                for idx in const_indexes:
                    print(eval(idx))
                print("and the following variable index(es)")
                for idx in var_indexes:
                    print(eval(idx))
            if exc_type == AttributeError:
                objects = re.findall(r"([a-zA-Z0-9]+)\.", l)
                print()
                print("Error trying to dot-index the following object(s)")
                for obj in objects:
                    print(obj)
                print("Which is/are of type")
                for obj in objects:
                    print(type(obj))
                print("which has/have the following attributes")
                for obj in objects:
                    print(obj.__dir__())
                    

    def get_line(self, ln):
        with open(__file__) as fid:
            for _ in range(ln-1):
                next(fid)
            return next(fid)


# examples below:
if __name__ == '__main__':
    
    with SmartException():
        data = {
            't': [1, 2, 3],
            'r': [5, 7, 9],
        }
        # the following works
        print(data['t'])
        # the following fails with KeyError
        print(data['k'])
        
        shortlist = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
        a = 2
        b = [1, 6]
        # the following index works
        print(shortlist[1])
        # the following fails with IndexError
        print(shortlist[a][b[1]])
        
        k = 3
        # the following fails with AttributeError
        k.append(2)
