from collections import Counter
import pandas as pd
import emoji
import warnings

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
                if(word[0]!="@"):
                    words.append(word)
    most_common_words_df=pd.DataFrame(Counter(words).most_common(20))
    return most_common_words_df 

# gives most common emojis in the chat
warnings.filterwarnings("ignore", message="Glyph.*missing from font")
def most_common_emojis(selected_user,df):
    if(selected_user!="All"):
        df=df[df['user']==selected_user]
    emojis=[]
    for msg in df['message']:
        emojis.extend([c for c in msg if c in emoji.EMOJI_DATA])
    most_common_emojis_df=pd.DataFrame(Counter(emojis).most_common(len(Counter(emojis)))).rename(columns={0:'emoji',1:'count'})
    return most_common_emojis_df

# month wise analysis
def monthly_timeline(selected_user,df):
    if(selected_user!="All"):
        df=df[df['user']==selected_user]
    timeline=df.groupby(['year','month_num','month'])['message'].count().reset_index()
    time=[]
    for i in range(timeline.shape[0]):
        time.append(timeline['month'][i]+"-"+str(timeline['year'][i]))
    timeline['time']=time
    return timeline

# daily analysis
def daily_timeline(selected_user,df):
    if(selected_user!="All"):
        df=df[df['user']==selected_user]
    timeline=df.groupby(['only_date'])['message'].count().reset_index()
    return timeline

# week activity map
def week_activity_map(selected_user,df):
    if(selected_user!="All"):
        df=df[df['user']==selected_user]
    return df['day_name'].value_counts()

# monthly activity map
def month_activity_map(selected_user,df):
    if(selected_user!="All"):
        df=df[df['user']==selected_user]
    return df['month'].value_counts()