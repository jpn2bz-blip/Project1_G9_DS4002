# Lyric Matching Model
Group 9: Mackenzie Craig, Jackson Haiz, Austin Chun

Course: DS 4002 Section 001
## Contents of Repository
This repository contains all the necessary files to reproduce the analysis for our Lyric Matching Model project. It includes the source code for data collection and modeling, the datasets used, and the outputs generated from our analysis.

# Software and Platform
Software: Python 3.8+

Main Packages:

lyricsgenius

spotipy

pandas

scikit-learn

numpy

matplotlib / seaborn

Platform: The code is platform-agnostic and should run on Windows, macOS, or Linux.

# Documentation
```
├── README.md
├── LICENSE.md
├── DATA/
│   ├── Man's_Best_Friend_lyrics.csv
│   ├── Readme Plots.pdf
│   ├── back_to_black_lyrics.csv
│   ├── readme.md
│   └── reputation_lyrics.csv
├── SCRIPTS/
│   ├── EDA_SCRIPT.ipynb
│   ├── Lyric_Collector (1).py
│   └── MI3_Analysis.ipynb
└── OUTPUT/
├── total_word_counts.png
└── frequent_words_amy.png
```


# Reproducibility
1. Clone the repository:
```
git clone <repository-url>
```
2. Install dependencies:
Navigate to the project directory and install the required packages.
```
pip install lyricsgenius spotipy pandas scikit-learn numpy matplotlib seaborn
```
3. Run the scripts:
Execute the scripts in the SCRIPTS folder in numerical order. The first script collects the data (if not already present), and the second script performs the analysis and generates the model and plots.

4. View the output:
All generated plots and model results will be saved in the OUTPUT folder.


