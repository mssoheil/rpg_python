""" Adventure X """

# from player_class import Player
from utils.validations import is_gender_valid, is_race_valid
from utils.playerCreationInputs import get_gender_from_user, get_race_from_user
from utils.mappings import genderFromAbbr, raceFromAbbr

print("Welcome to the Adventure X.")
print("In this game you can choose your character and find the lost treasure.")

print("Choose your character:")

name = input("Write your name: ")

gender = get_gender_from_user()

while is_gender_valid(gender) is False:
    print("Gender is wrong")
    gender = get_gender_from_user()


race = get_race_from_user()

while is_race_valid(race) is False:
    print("Race is wrong")
    race = get_race_from_user()

print("name: {0}, gender: {1}, race: {2}"
      .format(name, genderFromAbbr[gender], raceFromAbbr[race]))
