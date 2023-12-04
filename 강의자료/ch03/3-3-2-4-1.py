import streamlit as st
import pandas as pd

# 예제 데이터 생성
data = {
    '이름': ['홍길동', '김철수', '이영희', '박영수'],
    '나이': [30, 25, 28, 32],
    '성별': ['남성', '남성', '여성', '남성']
}

# 데이터 프레임 생성
df = pd.DataFrame(data)

# 데이터 프레임 출력
st.write(df)
st.dataframe(df, height=200)
st.table(df)
st.markdown(df.to_markdown())

st.code('''
st.write(df)
st.dataframe(df, height=200)
st.table(df)
st.markdown(df.to_markdown())
''')
