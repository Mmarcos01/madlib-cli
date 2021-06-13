import re

def read_template(read_file):
    with open(read_file) as file:
      return file.read().strip()

def parse_template(str):
  parts = tuple(re.findall(r"\{(.*?)\}", str))
  str = re.sub(r"\{(.*?)\}", "{}", str)
  return (str, parts)

def merge(story, words):
  words = ['dark', 'stormy', 'night']

  story = f"""It was a {words[0]} and {words[1]} {words[2]}."""
  return(story.strip("{}"))

# adjective = input("Enter an Adjective: ")
# next_adjective = input("Enter another Adjective: ")
# noun = input("Enter a Noun: ") 

# print('Welcome......')



# Make Me A Video Game!

# I the {Adjective} and {Adjective} {A First Name} have {Past Tense Verb}{A First Name}'s {Adjective} sister and plan to steal her {Adjective} {Plural Noun}!

# What are a {Large Animal} and backpacking {Small Animal} to do? Before you can help {A Girl's Name}, you'll have to collect the {Adjective} {Plural Noun} and {Adjective} {Plural Noun} that open up the {Number 1-50} worlds connected to A {First Name's} Lair. There are {Number} {Plural Noun} and {Number} {Plural Noun} in the game, along with hundreds of other goodies for you to find.

if __name__ == "__main__":
  path = 'assets/dark_and_stromy_night_template.txt'
  print(read_template(path))
