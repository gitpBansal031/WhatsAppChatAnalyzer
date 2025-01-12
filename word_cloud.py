from wordcloud import WordCloud
def create_word_cloud(selected_user,df):
    if(selected_user!="All"):
        df=df[df['user']==selected_user]
    wc=WordCloud(width=500,height=500,background_color='white',min_font_size=10)
    df_wc=wc.generate(df['message'].str.cat(sep=' '))
    return df_wc