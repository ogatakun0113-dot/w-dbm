import streamlit as st
import math

# --- ページ設定 ---
st.set_page_config(page_title="W→dBm変換アプリ", layout="centered")

# --- 見た目の設定（CSS） ---
st.markdown("""
    <style>
    /* クレジット表示用のCSS */
    .credit {
        text-align: right;
        font-size: 14px;
        color: #666;
        margin-bottom: -20px;
    }
    /* 入力欄のラベルを大きく、太く、緑色にする */
    .stNumberInput label {
        font-size: 32px !important;
        color: #22c55e !important;
        font-weight: 800 !important;
        line-height: 1.5;
    }
    /* 入力枠そのものを大きく、枠線を緑色にする */
    div[data-baseweb="input"] {
        height: 60px !important;
        font-size: 28px !important;
        border: 3px solid #22c55e !important;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# 右上にクレジットを表示
st.markdown('<p class="credit">開発/制作：緒方</p>', unsafe_allow_html=True)

st.title('📡 W → dBm 変換アプリ')
st.markdown("---")

# 入力欄（ワットを入力）
w_in = st.number_input("ワット (W) を入力してください", value=1.0, format="%.4f")

# 計算ロジック (50Ω系)
mw_val = w_in * 1000
if mw_val > 0:
    dbm_val = 10 * math.log10(mw_val)
else:
    dbm_val = -float('inf')

v_val = math.sqrt(w_in * 50)
dbuv_val = 20 * math.log10(v_val * 10**6)

# 表示
st.subheader("変換結果 (50Ω)")
c1, c2 = st.columns(2)
with c1:
    st.metric("電力 (dBm)", f"{dbm_val:.2f}")
    st.metric("電圧 (V)", f"{v_val:,.4f}")
with c2:
    st.metric("電力 (mW)", f"{mw_val:,.2f}")
    st.metric("dBμV (50Ω)", f"{dbuv_val:.2f}")
