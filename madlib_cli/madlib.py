# import re

def read_template(read_file):
    with open(read_file) as file:
      return file.read().strip()
 
def parse_template(strip_template):
    stripped_string = ""
    stripped_parts = []
    current_string = ""
    captured_part = False
    for char in strip_template:
      if char == "{":
        stripped_parts += char
        captured_part = True
        current_string = ""
      elif char == "}":
        stripped_parts += char
        captured_part = False
        stripped_parts.append(current_string)
      elif captured_part:
        current_string += char
      else:
        stripped_string += char
    return stripped_string, tuple(stripped_parts)

# def parse_template_regex(str):
#   parts = tuple(re.findall(r"\{(.*?)\}", str))
#   str = re.sub(r"\{(.*?)\}", "{}", str)
#   return (str, parts)

def merge(stripped, parts):
  return stripped.format(*parts)

def user_input(parts):
    response_list = []
    for part in parts:
      response = input(f"Enter a {part} ")
      response_list.append(response)
    return response_list

def save(merged, path):
    with open(path, "w") as file:
      file.write(merged)


def main(path):
    template = read_template(path)
    stripped, parts = parse_template(template)
    response_list = user_input(parts)
    merged = merge(stripped, response_list)
    print(merged)
    output = path.replace(".txt", ".completed.txt")
    save(merged, output)
# adjective = input("Enter an Adjective: ")
# next_adjective = input("Enter another Adjective: ")
# noun = input("Enter a Noun: ") 
# selected_words = ()

# madlib_story = open('assets/dark_and_stormy_night_template.txt')
# print(parse_template(madlib_story))


if __name__ == "__main__":
  path = "assets/dark_and_stormy_night_template.txt"
  # welcome = 'assets/welcome.txt'
  main(path)
  # input(read_template(welcome))

# while user_selection != "exit":
