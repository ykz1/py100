tweet = 'Woohoo! :-)'

if len(tweet) > 140:
    print('Tweet is too long!')

length_of_tweet = len(tweet + 5)        # We are trying to concatenate a str with an int, which is no bueno. To fix, we can convert 5 into '5' with str(5).