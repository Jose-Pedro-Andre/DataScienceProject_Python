from typing import Any

def all_thing_is_obj(object: Any) -> int:
    type_object = type(object);
    Objects_sentences = {'list': f"List: {type_object}",
                         'tuple': f"Tuple: {type_object}",
                         "dict": f"Dict: {type_object}",
                         "set": f"Set: {type_object}",
                         "str": f"{object} is in the kitchen: {type_object}"}
    result = Objects_sentences.get(type_object.__name__);
    if (result == None):
        print("Type not found")
    else:
        print(result);
    return 42
    