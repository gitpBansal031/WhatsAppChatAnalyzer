def most_busy_users(df):
    x=df['user'].value_counts().head()
    return x
def chat_contributions(df):
    df=round((df['user'].value_counts()/df.shape[0])*100,2).reset_index().rename(columns={'index':'name','user':'percentage'})
    return df
