## Setup

The adopted programming language is Python, and one dependency library (pandas) is used. Assume that Python and pip are already installed on the machine, the following command can be used to install the dependency library (pandas):

`sudo pip install pandas`

## File structure

**9gag_1.py** is the solution to the 1st challenge, while **9gag_2.py** is the solution to the 2nd challenge.

## Procedures

- Step 1: Download the raw data from https://storage.googleapis.com/data_interview/reddit_posts_2016_09_week1/reddit_posts_2016_09_week_1.csv.gz.
- Step 2: Uncompress it, and copy it to the repository folder so that the Python scripts are able to read it.
- Step 3: `python 9gag_1.py` will generate a file named `9gag_1.csv`, which is the final result for the 1st challenge.
- Step 4: `python 9gag_2.py` will generate a file named `9gag_2.csv`, which is the final result for the 2nd challenge.