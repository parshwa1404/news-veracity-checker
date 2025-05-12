[![Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://news-veracity-checker-parshwa-nandu.streamlit.app/)

🔗 **Live Demo**: [Click here to try the app](https://news-veracity-checker-parshwa-nandu.streamlit.app/)

> Classify news as true or false using AI, generate summaries and factual explanations.

---

# 📰 News Veracity Checker

With the explosive growth of social media, the spread of **fake news** has become a global crisis. According to the MIT Media Lab, **false information spreads six times faster** than true news on platforms like Twitter. Studies also show that nearly **64% of adults have been exposed to fake news online**, often without even realizing it.

That’s why I built this project: an **News Veracity Checker Using AI**. This tool classifies whether a news article or headline is **true or false** and provides a **fact-based explanation using an open-source language model**.

---

## 💡 Features

- ✅ **Veracity Score** – Classifies news as true or false using a BERT-based fake news detector
- 📃 **Article Summarizer** – Provides a concise summary of the content using Facebook’s BART model
- 🤖 **AI Explanation** – Uses Falcon-1B, an open-source lightweight language model, to generate fact-based rationales and corrected versions of misleading news
- ☁️ **Word Cloud Visualization** – Visual insight into the most frequent keywords
- 🧠 **All models are run locally using Hugging Face Transformers**

---

## 🛠️ Tech Stack

- **Streamlit** – For interactive front-end interface
- **Hugging Face Transformers** – For veracity detection, summarization, and explanation generation
- **PyTorch**
- **Matplotlib & WordCloud** – For visualization
- **Models Used:**
  - `jy46604790/Fake-News-Bert-Detect` – for veracity classification
  - `facebook/bart-large-cnn` – for summarizing long news texts
  - `google/gemma-2b-it` – for AI-generated factual explanation
