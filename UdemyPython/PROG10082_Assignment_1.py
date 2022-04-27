# 1.
Running_METS = 10
Basketball_METS = 8
Sleeping_METS = 1


def lbs_to_kgs(weight):
    return weight*0.454


def calc_calories(weight):
    calories_burnt = ((1.05 * Running_METS * (lbs_to_kgs(weight)))*0.5) + ((1.05 * Basketball_METS * (lbs_to_kgs(weight)))*(2/3)) + ((1.05 * Sleeping_METS * (lbs_to_kgs(weight)))*6.5)
    return calories_burnt

# 2.


def calc_finish_days(seconds):
    seconds = (seconds / (60 * 60 * 24))
    return seconds


if __name__ == "__main__":
    print(calc_calories(125))
    print(calc_calories(170))
    print(calc_calories(210))
    print(calc_finish_days(1234567))
