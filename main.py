import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title("Streamlit 超入門")

st.write("プログレスバーの表示")
"Start!!"

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f"Iteration {i+1}")
    bar.progress(i + 1)
    # time.sleep(0.1)

"Done!!!!!"

st.write("DataFrame")

# df = pd.DataFrame({
#     "1列目": [1, 2, 3, 4],
#     "2列目": [10, 20, 30, 40]
# })

# writeだと設定が変更出来ない
# st.write(df)
# dataframeだと設定が変更出来る
# st.dataframe(df.style.highlight_max(axis=0), width=500, height=500)
# tableだと静的な表を作れる
# st.table(df.style.highlight_max(axis=0))


# マークダウン記法
# """
# # 章
# ## 節
# ### 項

# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```

# """


# 乱数を生成して折れ線グラフを作る
# df = pd.DataFrame(
#     np.random.rand(20, 3),
#     columns=["a", "b", "c"]
# )
# st.line_chart(df)
# st.area_chart(df)
# st.bar_chart(df)


# 座標情報をマッピングする
# df = pd.DataFrame(
#     np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#     columns=["lat", "lon"]
# )
# st.map(df)


# 画像を表示する
# st.write("Display Image")




# インタラクティブなコンテンツ
st.write("Interactive Widgets")

left_column, right_column = st.beta_columns(2)
button = left_column.button("右カラムに文字を表示")
if button:
    right_column.write("ここは右カラム")

expander1 = st.beta_expander("問い合わせ1")
expander1.write("問い合わせ1の回答")
expander2 = st.beta_expander("問い合わせ2")
expander2.write("問い合わせ2の回答")
expander3 = st.beta_expander("問い合わせ3")
expander3.write("問い合わせ3の回答")

if st.checkbox("Show Image"):
    img = Image.open("S__69967876.jpg")
    st.image(img, caption="filter", use_column_width=True)

option = st.selectbox(
    "あなたが好きな数字を教えてください。",
    list(range(1, 11))
)
"あなたの好きな数字は", option, "です。"

text = st.sidebar.text_input("あなたの趣味を教えてください。")
"あなたの趣味：", text

condition = st.sidebar.slider("あなたの今の調子は？", 0, 100, 50)
"コンディション：", condition
