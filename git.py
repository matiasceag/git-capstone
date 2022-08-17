import json

def main(filename):
  print(filename)
  f = open(filename, 'r')
  data = json.load(f)

  pass

def top_tweets():
  pass

def top_users():
  pass

def top_days():
  pass

def top_hashtags():
  pass

main("data.json")