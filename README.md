## 📊 Datasets

This project uses multiple datasets to train, evaluate, and analyze the model. Below is a detailed description of each dataset and its purpose within the project.

### 1. **Old English Corpora**
- **Name:** Old English Corpora (Kielipankki / ORACC 2017-09)  
- **Source:** [[Link to the website](https://www.kielipankki.fi/download/ORACC/2017-09/vrt/)]  
- **Description:**  
  Contains:
  - Corpus of Ancient Mesopotamian Scholarship (CAMS)
  - Digital Corpus of Cuneiform Lexical Texts (DCCLT)
  - Royal Inscriptions of Babylonia Online (RIBO)
  - Royal Inscriptions of the Neo-Assyrian Period (RINAP)
  - State Archives of Assyria Online (SAAO)
- **Format:** VRT  
- **Size:** 23 MB 

### 2. **Modern English Corpus**
- **Name:** BBC News Dataset (Kaggle)
- **Source:** [[Link to the website](https://www.kaggle.com/datasets/gpreda/bbc-news)]
- **Description:**  
  Self updating dataset. It collects RSS Feeds from BBC News using a Kernel: https://www.kaggle.com/gpreda/bbc-news-rss-feeds.
  The Kernel is run with a fixed frequency and the dataset is updated using the output of the Notebook.
  BBC News RSS Feeds. The data contains the following columns:
  - title
  - pubDate
  - guid
  - link
  - description
- **Format:** CSV 
- **Size:** 14 MB

## 💻 Installation and Setup

Follow these steps in your terminal or command prompt:

1.  **Clone the Repository**
    Get a local copy of the project files using Git. 

    ```bash
    git clone https://github.com/Sahe00/NLPTM_finalproject.git
    cd NLPTM_finalproject
    ```

2.  **Create and Activate a Virtual Environment (Recommended)**
    Use a virtual environment to manage dependencies and avoid conflicts.

    ```bash
    python -m venv venv
    # On Windows (Command Prompt):
    .\venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    Install all required libraries listed in `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```


## 🏃 Running the Project

The core analysis is performed within the primary Jupyter Notebook.

### Option A: Running via Terminal/Browser (Standard)

1.  **Launch Jupyter Lab/Notebook**
    Start the local server from the project root directory:

    ```bash
    jupyter lab
    # OR
    jupyter notebook
    ```

2.  **Execute the Code**
    A web browser will open. Navigate to and click on **`project.ipynb`**. Run the cells sequentially to reproduce the results.

### Option B: Running via Visual Studio Code (IDE)

1.  **Open the Project in VS Code**
    Open the `NLPTM_finalproject` folder in VS Code.

2.  **Select the Python Kernel**
    * Open **`project.ipynb`**.
    * In the top right corner of the notebook interface, select the Python kernel associated with your newly created **`venv`** environment.
    * *Note: Ensure you have the **Python** and **Jupyter** extensions installed in VS Code.*

3.  **Execute the Code**
    Run the cells one by one or select "Run All" within the notebook interface to perform the analysis.

---