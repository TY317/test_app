import streamlit as st

##### ページの内容 #####
# ATの当選ゲーム数と契機をメモ
# 当選回数と当選ゲーム数の合算から当選確率を算出

##############################
##### 当選ゲーム数と契機のメモ
##############################
#見出し
st.header("初当りのデータメモ")

##### 初当りのデータを入力し、登録するフォーム
# 3列のカラムを作成
col1, col2, col3 = st.columns(3)

#当選ゲーム数の入力
with col1:
    # st.subheader("ゲーム数")
    game_num = st.number_input(label="ゲーム数")

#推測モードの入力
with col2:
    st.subheader("推測モード")

#当選契機の入力
with col3:
    st.subheader("当選契機")