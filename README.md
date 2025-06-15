# Financial Sentiment Classification — Financial PhraseBank

This repository contains our coursework for the NLP assignment on financial sentiment classification using the [Financial PhraseBank dataset](https://huggingface.co/datasets/takala/financial_phrasebank).

---

## 🧩 Part 0: Dataset Selection

We selected the **Financial PhraseBank** dataset ([Malo et al., 2014](https://huggingface.co/datasets/takala/financial_phrasebank)), which contains short English financial news sentences labeled as **negative (0)**, **neutral (1)**, or **positive (2)**. We used the **75% agreement** subset with **3,453 examples**, balancing label quality and dataset size.

---

## ⚙️ Part 1: Setting Up the Problem

- **a. Bibliography & SOA:**  
  Reviewed recent financial sentiment models like **FinBERT** and discussed business relevance in areas such as trading and risk management.

- **b. Dataset Description:**  
  Described class distribution, sentence length stats, and preprocessing steps (e.g., lemmatization, tokenization).

- **c. Random Classifier Benchmark:**  
  Simulated a random classifier achieving ~26.7% accuracy, serving as our baseline lower bound.

- **d. Rule-Based Baseline:**  
  Implemented a keyword-based classifier achieving **~60.6% accuracy**, performing best on neutral sentences but struggling with negative sentiment.

---

## 🧪 Part 2: Data Scientist Challenge

- Trained a BERT model on just **32 labeled samples**.  
- Augmented data without using LLMs.  
- Explored **zero-shot** and **LLM-generated** labels using ChatGPT.  
- Applied the most effective technique for performance gains.

---

## 📊 Part 3: State of the Art Comparison

- Trained models on incremental dataset sizes (1% to 100%).  
- Generated a learning curve.  
- Compared different training setups.  
- Analyzed the effectiveness of each approach against the full dataset benchmark.

---

## 🧱 Part 4: Model Distillation / Quantization

- Applied distillation and quantization to compress our best-performing model.  
- Compared performance and inference speed with the original.  
- Analyzed student model limitations and proposed future improvements.

---

## 📁 Repository Structure
```
├── data/ # Dataset files
├── figures/ # Plots & visualizations
├── packages/ # Custom Python modules
├── papers/ # PDFs and references
|── NLP_Final_Project # PDF for all the analysis
├── Notebook_Part01 # Baseline analysis
├── Notebook_Part02 # Data augmentation & LLMs
├── Notebook_Part03 # SOA comparison
├── Notebook_Part04 # Model compression
├── LICENSE
└── README.md
```

---

## 📜 License

Distributed under the MIT License.
