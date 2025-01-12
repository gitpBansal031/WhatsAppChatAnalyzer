import streamlit as st
import preprocessor
import count_stats
import helper
import word_cloud
import filtering
import matplotlib.pyplot as plt
st.sidebar.title('Whastsapp Chat Analyser')
uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data=uploaded_file.getvalue()
    data=bytes_data.decode('utf-8')
    df=preprocessor.preprocess(data)
    st.dataframe(df)

    # making side buttons
    user_list=df['user'].unique().tolist()
    user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0,'All')
    selected_user=st.sidebar.selectbox('Select User',user_list)
    if st.sidebar.button("Show Analysis"):

        # count_stats 
        msg_count,words_count,media_count,links_count=count_stats.fetch_stats(selected_user,df)
        col1,col2,col3,col4=st.columns(4)
        with col1:
            st.header("Total messages")
            st.title(msg_count)
        with col2:
            st.header("Total words")
            st.title(words_count)
        with col3:
            st.header("Total media")
            st.title(media_count)
        with col4:
            st.header("Total links")
            st.title(links_count)

        # most_busy_users
        if(selected_user=="All"):
            st.title("Most busy users")
            x=helper.most_busy_users(df)
            new_df=helper.chat_contributions(df)
            fig,ax=plt.subplots()
            col1,col2=st.columns(2)
            with col1:
                ax.bar(x.index,x.values,color='red')
                plt.xticks(rotation='vertical')
                st.pyplot(fig)
            with col2:
                st.dataframe(new_df)

        # filtered df
        filter_df=filtering.filter(df)
        st.dataframe(filter_df)

        # word_cloud
        st.title("Word Cloud")
        df_wc=word_cloud.create_word_cloud(selected_user,filter_df)
        fig,ax=plt.subplots()
        ax.imshow(df_wc)
        st.pyplot(fig)

        # most common words
        most_common_words_df=helper.most_common_words(selected_user,filter_df)
        fig,ax=plt.subplots()
        ax.barh(most_common_words_df[0],most_common_words_df[1])
        plt.xticks(rotation='vertical')
        st.title("Most common words")
        st.pyplot(fig)

