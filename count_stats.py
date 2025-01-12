from urlextract import URLExtract
def total_messages(df):
    return df.shape[0]

def total_words(df):
    words=[]
    for message in df['message']:
        words.extend(message.split())
    return len(words)

def total_media(df):
    new_df=df[df['message']=="<Media omitted>\n"]
    return new_df.shape[0]

def total_links(df):
    links=[]
    extactor=URLExtract()
    for msg in df['message']:
        links.extend(extactor.find_urls(msg))
    return len(links)
    
def fetch_stats(selected_user,df):
    if(selected_user!="All"):
        df=df[df['user']==selected_user]
    msg_count=total_messages(df)
    words_count=total_words(df)
    media_count=total_media(df)
    links_count=total_links(df)
    return msg_count,words_count,media_count,links_count