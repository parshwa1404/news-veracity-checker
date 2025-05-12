import streamlit as st
from transformers import pipeline
from wordcloud import WordCloud
import matplotlib.pyplot as plt

st.set_page_config(page_title="📰 News Veracity Checker", layout="wide")

@st.cache_resource
def load_models():
    veracity_model = pipeline('text-classification', model='jy46604790/Fake-News-Bert-Detect')
    summarizer = pipeline('summarization', model='facebook/bart-large-cnn')
    return veracity_model, summarizer, explainer

veracity_model, summarizer, explainer = load_models()


def get_summary(text):
    summary = summarizer(text, max_length=120, min_length=30, do_sample=False)
    return summary[0]['summary_text']

def plot_wordcloud(text):
    wc = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    st.pyplot(plt)

def get_veracity(text):
    res = veracity_model(text[:512])[0] 
    label = res['label']
    score = round(res['score'], 3)

    if label == "LABEL_0":
        return "False", score 
    else:
        return "True", score

#Streamlit
st.title("📰 News Veracity Checker")
st.sidebar.info("Paste a news headline or article to get a veracity check, summary, and AI-generated explanation.")

input_text = st.text_area("Paste news headline or article:", height=200)

if st.button("🚀 Analyze"):
    with st.spinner("Analyzing the content..."):
        label, score = get_veracity(input_text)
        if label == "True":
            st.markdown(f"""<h4>✅ <span style='color:green;'>Veracity: True</span> ({score*100:.2f}% confidence)</h4>""",unsafe_allow_html=True)
        else:
            st.markdown(f"""<h4>❌ <span style='color:red;'>Veracity: False</span> ({score*100:.2f}% confidence)</h4>""",unsafe_allow_html=True)

        #summary
        summary = get_summary(input_text)
        st.markdown("### 📃 **Summary:**")
        st.info(summary)

        plot_wordcloud(input_text)
