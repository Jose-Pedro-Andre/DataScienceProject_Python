import numpy as np

def slice_me(family: list, start: int, end: int) -> list:
    my_array2D = np.array(family)
    # print(my_array2D)
    print(f"My shape is: {my_array2D.shape}")
    object_slice = slice(start, end)
    print(f"My new shape {my_array2D[object_slice].shape}")
    return (my_array2D[object_slice].tolist())