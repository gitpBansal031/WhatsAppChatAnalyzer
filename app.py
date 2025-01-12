import streamlit as st
import preprocessor
import helper
st.sidebar.title('Whastsapp Chat Analyser')
uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data=uploaded_file.getvalue()
    data=bytes_data.decode('utf-8')
    df=preprocessor.preprocess(data)
    st.dataframe(df)

    #fetch unique users
    user_list=df['user'].unique().tolist()
    user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0,'All')
    selected_user=st.sidebar.selectbox('Select User',user_list)
    if st.sidebar.button("Show Analysis"):
        msg_count,words_count=helper.fetch_stats(selected_user,df)
        col1,col2,col3,col4=st.columns(4)
        with col1:
            st.header("Total messages")
            st.title(msg_count)
        with col2:
            st.header("Total words")
            st.title(words_count)