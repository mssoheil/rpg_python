def is_gender_valid(gender):
    # check whether the given gender is valid

    genders = ("M", "Male", "F", "Female", "R", "Random")

    return gender in genders


def is_race_valid(race):
    # check whether the given race is valid

    races = ("H", "Human", "E", "Elf", "O", "Orc", "Random", "R")
    return race in races
