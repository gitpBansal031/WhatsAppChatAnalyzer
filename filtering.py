# removing the system messages
def filter(df):
    df=df[df['message']!="group notification"]
    df=df[df['message']!="<Media omitted>\n"]
    df=df[df['message']!="Waiting for this message\n"]
    df=df[df['message']!="This message was deleted\n"]
    df=df[df['message']!="You deleted this message\n"]
    df=df[df['message']!="null\n"]
    return df
