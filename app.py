from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

import streamlit as st

st.title("チャットボットアプリ")

st.write("##### モード1: ビジネスボット")
st.write("ビジネスに関するアドバイスを受けることができます")
st.write("##### モード2: 健康ボット")
st.write("健康に関するアドバイスを受けられます")

selected_item = st.radio(
    "モードを選択してください。",
    ["ビジネスボット", "健康ボット"]
)

input_message = st.text_input(label="テキストを入力してください")


if st.button("実行") and input_message:

    if selected_item == "ビジネスボット":
        system_prompt = "あなたはビジネスに詳しいアドバイザーです。論理的かつ実用的なアドバイスを日本語で提供してください。"
    else:
        system_prompt = "あなたは健康に詳しいアドバイザーです。親しみやすく丁寧な口調で健康に関する助言を日本語で提供してください。"

    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=input_message),
    ]

    result = llm(messages)

    st.markdown(f"### 回答：\n{result.content}")
