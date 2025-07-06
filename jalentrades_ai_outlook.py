import streamlit as st

st.set_page_config(page_title="JalenTrades AI Outlook", layout="centered")

st.title("📊 JalenTrades AI Market Outlook")
st.markdown("Type in a stock or index ticker to get an instant AI-powered outlook.")

# Ticker input
ticker = st.text_input("Enter Ticker Symbol (e.g. AAPL, SPY, ES)")

# Simulated AI response logic
if ticker:
    ticker = ticker.upper()
    st.markdown(f"### 🔍 Outlook for {ticker}")

    st.markdown("#### 📈 Weekly Outlook")
    st.write(f"- Trend: {ticker} showing consolidation near recent highs")
    st.write("- Support: 204.30 | Resistance: 217.40")
    st.write("- Bias: Short-term bullish continuation")

    st.markdown("#### 📆 Monthly Outlook")
    st.write("- Macro: Market sentiment aligned with tech sector strength")
    st.write("- Strategy: Buy dips into support, cautious of high CPI next week")

    st.markdown("#### 🗓️ Yearly Outlook")
    st.write("- Long-term trend remains intact")
    st.write("- Watch for Q4 earnings breakout or macro shock risks")

    st.success("This is a sample AI-driven forecast. Premium subscribers get real-time data and trade setups.")
else:
    st.info("Enter a ticker above to generate a forecast.")