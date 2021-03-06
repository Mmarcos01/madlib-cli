def read_template(read_file):
    with open(read_file) as file:
      return file.read().strip()

def parse_template(template):
    stripped_string = ""
    parts = []
    current_string = ""
    captured_part = False
    for char in template:
        if char == "{":
            stripped_string += char
            captured_part = True
            current_string = ""
        elif char == "}":
            stripped_string += char
            captured_part = False
            parts.append(current_string)
        elif captured_part:
            current_string += char
        else:
            stripped_string += char
    return stripped_string, tuple(parts)

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

def welcome():
  welcome = 'assets/welcome.txt'
  input(read_template(welcome))

def main(path):
    welcome()
    template = read_template(path)
    stripped, parts = parse_template(template)
    response_list = user_input(parts)
    merged = merge(stripped, response_list)
    print(merged)
    output = path.replace(".txt", ".completed.txt")
    save(merged, output)

if __name__ == "__main__":
  path = "assets/story_template.txt"
  main(path)

# while user_selection != "exit":
