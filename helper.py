def total_messages(df):
    return df.shape[0]

def total_words(df):
    words=[]
    for message in df['message']:
        words.extend(message.split())
    return len(words)

def fetch_stats(selected_user,df):
    if(selected_user!="All"):
        df=df[df['user']==selected_user]
    msg_count=total_messages(df)
    words_count=total_words(df)
    return msg_count,words_count