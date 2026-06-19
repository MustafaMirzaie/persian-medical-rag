# 🩺 Advanced Medical RAG System — Type 2 Diabetes Q&A

A complete **end‑to‑end Retrieval‑Augmented Generation (RAG)** system for answering Persian questions about Type 2 Diabetes, implemented in a top‑to‑bottom executable Jupyter Notebook.

The system reads Persian medical documents from three types of sources, chunks and vectorizes them, retrieves the most relevant passages using a combination of semantic and keyword search, improves results through reranking and diversification, and finally generates a source‑grounded answer using a language model.

---

## ✨ Features

### Core System (10 Phases)
- **Data ingestion** from three source types: PDF, web pages (HTML), and text (FAQ)
- **Chunking** using both Recursive and Semantic methods, with quantitative comparison
- **Vectorization** using a local multilingual model and storage in the Chroma vector database
- **Hybrid retrieval** combining Dense search and BM25 using RRF
- **Metadata filtering** to restrict results by source type
- **Reranking** using a local Cross‑Encoder model
- **Result diversification** with the MMR algorithm
- **Answer generation** with citations and refusal for out‑of‑scope questions
- **Evaluation** using Recall@k, MRR, and faithfulness/relevance metrics (LLM‑as‑Judge)
- **Graphical user interface** built with Gradio

### Advanced Capabilities (Bonus)
- **Conversation memory + query rewriting**: handling follow‑up and ambiguous questions
- **HyDE**: improving retrieval by generating a hypothetical answer
- **Multimodal support**: text‑to‑image search using CLIP
- **Right‑to‑left interface** with Vazir font and display of a related image

---

## 📁 Project Structure

```
rag-medical/
├── notebook.ipynb          # Main notebook (run top to bottom)
├── download_models.py      # Script for downloading local models
├── requirements.txt        # Dependencies
├── .env                    # API key and configuration (create manually)
├── .gitignore
├── README.md
├── data/
│   ├── raw/                # Raw documents: PDF, HTML, TXT
│   └── processed/
├── indexes/                # Chroma database and BM25 file
├── cache/                  # Cached LLM responses (JSON)
├── models/                 # Local models (embedding, reranker, CLIP)
└── assets/
    ├── fonts/              # Vazir font
    └── images/             # Images for the multimodal phase
```

---

## 🧠 Local Models (Free, CPU‑Friendly)

| Role | Model | Vector Dimension |
|---|---|---|
| Embedding | `intfloat/multilingual-e5-small` | 384 |
| Reranker | `cross-encoder/mmarco-mMiniLMv2-L12-H384-v1` | — |
| Multimodal | `sentence-transformers/clip-ViT-B-32` | 512 |

Embedding, reranking, and CLIP run **entirely locally and free of cost**. Only **answer generation** and **LLM‑as‑Judge evaluation** use an API.

---

## ⚙️ Installation & Setup

### 1. Create a Virtual Environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### 2. Download Local Models

```powershell
python download_models.py
```

If downloads are slow or restricted, you can use a mirror (configurable in the script):

```python
os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"
```

Downloads are **resumable**; simply run the script again if interrupted.

### 3. Configure the API Key

Create a `.env` file in the project root:

```dotenv
GAPGPT_API_KEY=your_key
GAPGPT_BASE_URL=https://api.gapgpt.app/v1
GAPGPT_MODEL=model_name
```

### 4. Prepare Data

Place raw documents in `data/raw/` and images in `assets/images/`.

---

## ▶️ Running the System

Open `notebook.ipynb` in VS Code, select the `Python (rag-medical)` kernel, and use **Run All** from the menu. At the end, the Gradio interface will automatically open in your browser.

---

## 🔄 System Workflow

```
Raw Document → Chunking → Vectorization → [Chroma + BM25]
                                            ↓
Query → Rewriting → Hybrid Search (RRF) → Filter → Rerank → MMR
                                            ↓
                          Source‑grounded Answer ← Selected Context
                                            ↓
                           Response + Sources + Related Image
```

---

## 📊 Evaluation

| Category | Metric | Description |
|---|---|---|
| Retrieval | Recall@k, MRR | No API cost |
| Generation | Faithfulness, Relevance | Using LLM‑as‑Judge, cached |

To control costs, evaluation runs on **3 questions by default**.  
For the full **15‑question evaluation**, set:

```
RUN_FULL_EVAL = True
```

---

## 💰 Cost Discipline

- Embeddings, reranking, and CLIP are **local and free**.
- LLM responses and judge outputs are **cached in JSON**, so re‑runs incur no additional cost.
- Output tokens are capped (`max_tokens ≤ 700`) with a low temperature for stability.

---

## 🛠️ Tech Stack

Python · Jupyter · sentence-transformers · Chroma · rank_bm25 · OpenAI SDK (GapGPT‑compatible) · Gradio · CLIP

---

## 📝 Medical Disclaimer

This system is **for educational purposes only**, and its responses **do not replace professional medical advice from a qualified physician**.
