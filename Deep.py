# #Remove Preexisting Files
# ! rm -rf NBA-Machine-Learning-Sports-Betting
# ! rm -rf *

# #Bootstrap Files
# ! git clone https://github.com/kyleskom/NBA-Machine-Learning-Sports-Betting.git
# ! mv -v ./NBA-Machine-Learning-Sports-Betting/* .
# ! pip3 install -r requirements.txt

# #Clear Bootstrap Logs
import openai
from textblob import TextBlob
import tweepy
from IPython.display import clear_output
clear_output()

print("Successful Bootstrap!!!")


# Authenticate with Twitter API
consumer_key = 'eq9QvcZRupgT1iBdqEbnu9Wea'
consumer_secret = 'cvbu9YAI5TcGXkuVk6mNB54cNjlAo3Pbr3NcXGb109XFI2PcHX'
access_token = '2479063608-4cx5s5H6wIRXZJBcM19MbGSBBLPUCuY8K54UYNv'
access_token_secret = 'vpGBGHEzBrxNp1JKIeWSE9c1n5WMACamAeDVTcNFj8j8k'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Search for tweets about the Warriors
warriors_tweets = tweepy.Cursor(
    api.search, q='#Golden State Warriors').items(100)


# Perform sentiment analysis on tweets
positive_tweets = 0
negative_tweets = 0
neutral_tweets = 0

for tweet in warriors_tweets:
    analysis = TextBlob(tweet.text)
    if analysis.sentiment.polarity > 0:
        positive_tweets += 1
    elif analysis.sentiment.polarity < 0:
        negative_tweets += 1
    else:
        neutral_tweets += 1

# Print results
print("Positive tweets: ", positive_tweets)
print("Negative tweets: ", negative_tweets)
print("Neutral tweets: ", neutral_tweets)

# Add GPT Explanation


# Import the OpenAI library

# Set the API key
openai.api_key = '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'

# Define the text to summarize
text = "------------------fanduel odds data------------------Toronto Raptors (106) @ Milwaukee Bucks (-124)Brooklyn Nets (-178) @ San Antonio Spurs (150)Portland Trail Blazers (194) @ Denver Nuggets (-235)Philadelphia 76ers (108) @ LA Clippers (-126)---------------XGBoost Model Predictions---------------Milwaukee Bucks (76.7%) vs Toronto Raptors: UNDER 222 (55.1%)San Antonio Spurs vs Brooklyn Nets (79.7%): UNDER 229.5 (56.8%)Denver Nuggets (77.7%) vs Portland Trail Blazers: UNDER 237 (79.1%)LA Clippers vs Philadelphia 76ers (58.7%): UNDER 223 (58.1%)--------------------Expected Value---------------------Milwaukee Bucks EV: 38.61Toronto Raptors EV: -52.07San Antonio Spurs EV: -49.2Brooklyn Nets EV: 24.45Denver Nuggets EV: 10.76Portland Trail Blazers EV: -34.44LA Clippers EV: -25.9Philadelphia 76ers EV: 22.07"

# Use the OpenAI API to summarize the text
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=(f"summarize this text: {text}"),
    max_tokens=100
)

# Print the summary
print(response["choices"][0]["text"])
