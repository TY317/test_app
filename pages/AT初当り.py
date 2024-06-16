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
with st.form(key='bonus_data_input'):

    # 3列のカラムを作成
    col1, col2, col3 = st.columns(3)

    #当選ゲーム数の入力
    with col1:
        # st.subheader("ゲーム数")
        game_num = st.number_input(label="ゲーム数", step=1)

    #推測モードの入力
    with col2:
        # st.subheader("推測モード")
        mode = st.multiselect("推測モード",
                            ["天国","通常","地獄","?"])

    #当選契機の入力
    with col3:
        # st.subheader("当選契機")
        koyaku = st.multiselect("当選契機",
                                ["中チェ","強スイカ","チャンス目","弱スイカ","角チェ","確定役","謎"])
        
    #登録ボタン
    submit_btn = st.form_submit_button("登録")