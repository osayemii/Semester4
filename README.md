# Semester4

**Bio:** Semester 4 programming coursework covering Python fundamentals, data processing, visualization, Flask web apps, Tkinter GUIs, machine learning, deep learning, and NLP.

**Description:** Coursework repository organized by subject area: `DL`, `ML`, `NLP`, and `missKene_python`.

## Folder guide

| Folder | What it contains |
| --- | --- |
| `DL/` | Deep learning scripts and experiments: CNNs, RNNs, autoencoders, backpropagation, batch normalization, AlexNet/VGG/LeNet examples, and RL-style ANN work. |
| `DL/assignment/` | Deep learning assignment files, including an MTN US churn model and classwork helper code. |
| `ML/` | Machine learning exercises: EDA, regression, classification, clustering, dimensionality reduction, inference tests, notebooks, and datasets. |
| `ML/__pycache__/` | Python bytecode cache for ML scripts. Safe to ignore or delete. |
| `NLP/` | NLP experiments: sentiment analysis, aspect extraction, POS tagging, entity linking, feature extraction, and text classifiers. |
| `NLP/__pycache__/` | Python bytecode cache for NLP scripts. Safe to ignore or delete. |
| `NLP/test/` | Small NLP test scripts for rule-based sentiment and VADER lexicon checks. |
| `missKene_python/` | Main Python coursework folder: fundamentals, assignments, packages, data processing, visualization, Flask apps, Tkinter GUIs, and web scraping. |
| `missKene_python/.vscode/` | VS Code workspace settings for the coursework folder. |
| `missKene_python/__pycache__/` | Python bytecode cache for root-level coursework scripts. Safe to ignore or delete. |
| `missKene_python/assignment/` | General Python assignments: regex, data visualization, student scores, and practice files. |
| `missKene_python/assignment/real_estate/` | Container for the real-estate app assignment versions. |
| `missKene_python/assignment/real_estate/estate_flask/` | Flask version of the real-estate app with app/db modules. |
| `missKene_python/assignment/real_estate/estate_flask/__pycache__/` | Python bytecode cache for the Flask real-estate app. Safe to ignore or delete. |
| `missKene_python/assignment/real_estate/estate_flask/static/` | Static asset container for the Flask real-estate app. |
| `missKene_python/assignment/real_estate/estate_flask/static/css/` | Stylesheet for the Flask real-estate app. |
| `missKene_python/assignment/real_estate/estate_flask/templates/` | HTML templates for the Flask real-estate app. |
| `missKene_python/assignment/real_estate/estate_tkinter/` | Tkinter desktop version of the real-estate app: login, CRUD, enquiries, images, and summary UI. |
| `missKene_python/assignment/real_estate/estate_tkinter/__pycache__/` | Python bytecode cache for the Tkinter real-estate app. Safe to ignore or delete. |
| `missKene_python/assignment/tempPackage/` | Sample Python package for temperature conversion. |
| `missKene_python/assignment/tempPackage/__pycache__/` | Python bytecode cache for `tempPackage`. Safe to ignore or delete. |
| `missKene_python/data_processing/` | Pandas/data preprocessing exercises and datasets: cleaning, encoding, scaling, feature engineering, and train/test splits. |
| `missKene_python/data_processing/clw/` | Classwork pandas/data-processing scripts. |
| `missKene_python/data_visualization/` | Matplotlib/pyplot chart examples: bar charts, histograms, scatter plots, and product rating plots. |
| `missKene_python/flask/` | Container for Flask web app examples. |
| `missKene_python/flask/book_app/` | Simple Flask book catalogue app. |
| `missKene_python/flask/book_app/template/` | HTML templates for the book catalogue app. |
| `missKene_python/flask/flask_app/` | Flask routing/template examples. |
| `missKene_python/flask/flask_app/template/` | HTML templates for `flask_app`. |
| `missKene_python/flask/real_estate/` | Flask real-estate web app iterations. |
| `missKene_python/flask/real_estate/__pycache__/` | Python bytecode cache for Flask real-estate scripts. Safe to ignore or delete. |
| `missKene_python/flask/real_estate/template/` | HTML templates for the Flask real-estate app. |
| `missKene_python/flask/sales_inventory/` | Flask sales/inventory app with static assets and templates. |
| `missKene_python/flask/sales_inventory/static/` | Static asset container for the sales/inventory app. |
| `missKene_python/flask/sales_inventory/static/css/` | Stylesheet for the sales/inventory app. |
| `missKene_python/flask/sales_inventory/static/images/` | Images for the sales/inventory app, including the logo. |
| `missKene_python/flask/sales_inventory/template/` | HTML templates for the sales/inventory app. |
| `missKene_python/gui_tkinter/` | Tkinter GUI exercises: frames, checkboxes, student info/design forms. |
| `missKene_python/gui_tkinter/sales_record/` | Tkinter sales record app with database/table setup and a transactions CSV. |
| `missKene_python/mathPackage/` | Sample Python package for basic math operations. |
| `missKene_python/mathPackage/__pycache__/` | Python bytecode cache for `mathPackage`. Safe to ignore or delete. |
| `missKene_python/mrOba_python/` | Introductory Python exercises: variables, data types, functions, conditionals, and assignments. |
| `missKene_python/turtle/` | Turtle graphics example, including a rainbow color demo. |
| `missKene_python/web_scrappy/` | Web scraping experiments using BeautifulSoup and Scrapy-style scripts, including a Jumia scrape. |

## Repository tree

```text
Semester4/
├── DL/
│   └── assignment/
├── ML/
│   └── __pycache__/
├── NLP/
│   ├── __pycache__/
│   └── test/
└── missKene_python/
    ├── .vscode/
    ├── __pycache__/
    ├── assignment/
    │   ├── real_estate/
    │   │   ├── estate_flask/
    │   │   │   ├── __pycache__/
    │   │   │   ├── static/
    │   │   │   │   └── css/
    │   │   │   └── templates/
    │   │   └── estate_tkinter/
    │   │       └── __pycache__/
    │   └── tempPackage/
    │       └── __pycache__/
    ├── data_processing/
    │   └── clw/
    ├── data_visualization/
    ├── flask/
    │   ├── book_app/
    │   │   └── template/
    │   ├── flask_app/
    │   │   └── template/
    │   ├── real_estate/
    │   │   ├── __pycache__/
    │   │   └── template/
    │   └── sales_inventory/
    │       ├── static/
    │       │   ├── css/
    │       │   └── images/
    │       └── template/
    ├── gui_tkinter/
    │   └── sales_record/
    ├── mathPackage/
    │   └── __pycache__/
    ├── mrOba_python/
    ├── turtle/
    └── web_scrappy/
```

## Running the code

There is no single entry point; run individual scripts from their folders. Common dependencies across the repo include:

```bash
pip install pandas numpy matplotlib scikit-learn flask jupyter
pip install beautifulsoup4 scrapy spacy nltk vaderSentiment
```

Tkinter is usually included with Python on desktop installs. Some notebooks may also need `tensorflow`, `torch`, or `keras` depending on the script.

`__pycache__/` folders are generated Python bytecode caches and do not need to be committed.
