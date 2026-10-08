from typing import Any

def NULL_not_found(object: Any) -> int:
    my_values = {"": f"Empty: {object} {type(object)}",
                 False: f"Fake: {object} {type(object)}" if  type(object) is bool else f"Zero: {object} {type(object)}",
                 None: f"Nothing: {object} {type(object)}"}
    if (my_values.get(object) is None):
        if (type(object) is float):
            print(f"Cheese: {object} {type(object)}")
            return 0
        print("Type not found")
        return 1;
    print(my_values.get(object))
    return 0