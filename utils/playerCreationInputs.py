def get_gender_from_user():
    # get the inputted gender from the user

    print("""Genders:
1) F(Female)
2) M(Male)
3) R(Random)""")
    gender = input("Choose your gender: ")
    return gender


def get_race_from_user():
    # get the inputted gender from the user

    print("""Races:
1) H(Human)
  stats: health (+5%), attack (+5%), defense (+5%)
2) O(Orc)
  stats: health (+5%), backpack (+10%), defense (-10%)
3) E(Elf)
  stats: health (-5%), attack (+15%), defense (-5%)
4) R(Random)
""")
    race = input("Choose your race: ")
    return race
