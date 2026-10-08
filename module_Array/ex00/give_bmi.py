def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """
        The funtion calcule the BMI

        :param height: a list of integers or floats representing the height of different people
        :param weight: a list of integers or floats representing the weight of different people
        :return: BMI calculation
    """
    bmi = [j / (i * i )for j, i in zip(weight, height)]
    return bmi
def apply_limit(bmi: list[int | float], limit: int)-> list[bool]:
    list_acept = [True if i >= limit else False for i in bmi]
    return list_acept

def main():
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))

if __name__ == "__main__":
    main()