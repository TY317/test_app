import streamlit as st
import pandas as pd

st.title("スマスロ北斗の拳")

##### 新規作成ボタンを押すとデータをすべてリセットする

#フォームの作成
with st.form(key='new_play'):

    #新規作成ボタンの設定
    start_btn = st.form_submit_button("新規作成")

    #ボタンが押されたらcsvファイルをリセットし保存
    if start_btn:

        ##### AT初当り用
        #AT初当り用のデータフレームを保存するcsvファイル
        AT_get_df = pd.DataFrame(columns=["ゲーム数", "推測モード", "当選契機"])
        # AT_get_df = pd.DataFrame(columns=["a", "b", "c"])
        AT_get_df.to_csv("./pages/AT_get_df.csv", index=False)

        ##### 通常時中段ベル用
        #通常時中段ベルの回数を保存するcsvファイル
        nomal_center_bell_df = pd.DataFrame(data=[0],columns=["中段ベル回数"])
        # nomal_center_bell_df = pd.DataFrame(columns=["中段ベル回数"])
        nomal_center_bell_df.to_csv("./pages/nomal_center_bell_df.csv", index=False)

        ##### AT中の中段ベル用
        #AT中の中段ベルの回数を保存するcsvファイル
        at_center_bell_df = pd.DataFrame(data=[0], columns=["中段ベル回数"])
        # at_center_bell_df = pd.DataFrame(columns=["中段ベル回数"])
        at_center_bell_df.to_csv("./pages/at_center_bell_df.csv", index=False)
        
st.caption("ver1.0.0")
st.caption("   ・新規作成")