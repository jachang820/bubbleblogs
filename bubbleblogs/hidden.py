def read_dot_env():
  variables = {}
  with open(".env", 'r') as file:
    key, value = extract_key_value_pair(file)
    variables[key] = value
  return variables

def extract_key_value_pair(file):
  line = file.readline()
  key, value = split_key_value_pair(line)
  value = string_to_int_or_float(value)
  return key, value

def split_key_value_pair(line):
  return line.split('=') # key, value

def string_to_int_or_float(str):
  if str.isdecimal():
    str = float(str) if str.find('.') > 0 else int(str)
  return str

dot_env = read_dot_env()