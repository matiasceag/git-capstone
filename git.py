import json

def main(filename):
  tweets = []
  for line in open(filename, 'r'):
    tweets.append(json.loads(line))

def top_tweets():
  pass

def top_users():
  pass

def top_days():
  pass

def top_hashtags():
  pass

main('data.json')