from collections import Counter
import pandas as pd
import filtering

# gives most busy users in the chat
def most_busy_users(df):
    x=df['user'].value_counts().head()
    return x

# gives percentage of contribution of each user in the chat
def chat_contributions(df):
    df=round((df['user'].value_counts()/df.shape[0])*100,2).reset_index().rename(columns={'index':'name','user':'percentage'})
    return df

# gives most common words in the chat
def most_common_words(selected_user,df):
    if(selected_user!="All"):
        df=df[df['user']==selected_user]
   
    # reading the stop words file 
    f=open("stop_words.txt","r")
    stop_words=f.read()

    # getting most common words
    words=[]
    for msg in df['message']:
        for word in msg.lower().split():
            if word not in stop_words:
                words.append(word)
    most_common_words_df=pd.DataFrame(Counter(words).most_common(10))
    return most_common_words_df 