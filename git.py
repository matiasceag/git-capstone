import json

def main(filename):
  tweets = []
  for line in open(filename, 'r'):
    tweets.append(json.loads(line))
  # result = top_tweets(tweets)
  # result = top_users(tweets)
  # result = top_days(tweets)
  result = top_hashtags(tweets)
  print(result)

def top_tweets(tweets):
  mergeSortTweet(tweets, 0, len(tweets)-1)
  return tweets[len(tweets)-10:len(tweets)]

def top_users(tweets):
  mergeSortUser(tweets, 0, len(tweets)-1)
  return tweets[len(tweets)-10:len(tweets)]

def top_days(tweets):
  days = {}
  days_array = []
  for tweet in tweets:
    if tweet["date"] in days:
      days_array[days[tweet["date"]]]["count"] += 1
    else:
      days_array.append({"date": tweet["date"], "count": 1})
      pos = len(days_array) - 1
      days[tweet["date"]] = pos
  mergeSortDay(days_array, 0, len(days_array)-1)
  return days_array[len(days_array)-10:len(days_array)]

def top_hashtags(tweets):
  hashtags = {}
  hashtags_array = []
  for tweet in tweets:
    hashtags_list = extract_hashtags(tweet["content"])
    for hashtag in hashtags_list:
      if hashtag in hashtags:
        hashtags_array[hashtags[hashtag]]["count"] += 1
      else:
        hashtags_array.append({"hashtag": hashtag, "count": 1})
        pos = len(hashtags_array) - 1
        hashtags[hashtag] = pos
  mergeSortHashtags(hashtags_array, 0, len(hashtags_array)-1)
  return hashtags_array[len(hashtags_array)-10:len(hashtags_array)]

# REF: https://www.geeksforgeeks.org/python-program-for-merge-sort/#:~:text=Merge%20Sort%20is%20a%20Divide,assumes%20that%20arr%5Bl..
def mergeTweet(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
 
    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)
 
    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]
 
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
 
    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray
 
    while i < n1 and j < n2:
        if L[i]["retweetCount"] <= R[j]["retweetCount"]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
 
    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
 
    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
 
# l is for left index and r is right index of the
# sub-array of arr to be sorted

def mergeUser(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
 
    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)
 
    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]
 
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
 
    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray
 
    while i < n1 and j < n2:
        if L[i]["user"]["mediaCount"] <= R[j]["user"]["mediaCount"] :
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
 
    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
 
    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
 
# l is for left index and r is right index of the
# sub-array of arr to be sorted

def mergeDay(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
 
    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)
 
    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]
 
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
 
    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray
 
    while i < n1 and j < n2:
        if L[i]["count"] <= R[j]["count"]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
 
    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
 
    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
 
# l is for left index and r is right index of the
# sub-array of arr to be sorted

def mergeHashtags(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
 
    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)
 
    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]
 
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
 
    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray
 
    while i < n1 and j < n2:
        if L[i]["count"] <= R[j]["count"]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
 
    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
 
    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
 
# l is for left index and r is right index of the
# sub-array of arr to be sorted
 
def mergeSortTweet(arr, l, r):
    if l < r:
 
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l+(r-l)//2
 
        # Sort first and second halves
        mergeSortTweet(arr, l, m)
        mergeSortTweet(arr, m+1, r)
        mergeTweet(arr, l, m, r)

def mergeSortUser(arr, l, r):
    if l < r:
 
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l+(r-l)//2
 
        # Sort first and second halves
        mergeSortUser(arr, l, m)
        mergeSortUser(arr, m+1, r)
        mergeUser(arr, l, m, r)

def mergeSortDay(arr, l, r):
    if l < r:
 
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l+(r-l)//2
 
        # Sort first and second halves
        mergeSortDay(arr, l, m)
        mergeSortDay(arr, m+1, r)
        mergeDay(arr, l, m, r)

def mergeSortHashtags(arr, l, r):
    if l < r:
 
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l+(r-l)//2
 
        # Sort first and second halves
        mergeSortHashtags(arr, l, m)
        mergeSortHashtags(arr, m+1, r)
        mergeHashtags(arr, l, m, r)

# REF: https://www.geeksforgeeks.org/python-extract-hashtags-from-text/#:~:text=Split%20the%20text%20into%20words,Print%20the%20list%20of%20hashtags.
def extract_hashtags(text):
     
    # initializing hashtag_list variable
    hashtag_list = []
     
    # splitting the text into words
    for word in text.split():
         
        # checking the first character of every word
        if word[0] == '#':
             
            # adding the word to the hashtag_list
            hashtag_list.append(word[1:])
     
    return hashtag_list

main('data.json')