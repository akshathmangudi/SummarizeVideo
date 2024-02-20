# SummarizeVideo
To run the notebooks inside the 'trials' folder, run the code inside google colab. 

SummarizeVideo is an application that allows you to summarize the content in a YouTube video. The application allows you
to pass in a YouTube link when is then converted into its textual context. Then, the context is passed to a abstractive s
summarization model which allows you to generate condensed summaries with respect to the video.

## Table of Contents
* <a href="https://github.com/akshathmangudi/SummarizeVideo#overview">Overview</a>
* <a href="https://github.com/akshathmangudi/SummarizeVideo#requirements">Requirements</a>
  * <a href="https://github.com/akshathmangudi/SummarizeVideo#conda-environment">Conda Environment</a>
  * <a href="https://github.com/akshathmangudi/SummarizeVideo#installing-dependencies">Installing dependencies</a>
* <a href="https://github.com/akshathmangudi/SummarizeVideo#licensing">Licensing</a>
* <a href="https://github.com/akshathmangudi/SummarizeVideo#help">Help</a>

## Overview

The LLMBot is a Python application that uses a language model and natural language processing in which the use can 
query multiple PDFs and can ask the bot on questions related to the PDF queried. The language model used for this
application is the OpenAI model and Hugging Face models are used for embeddings. This application generates
accurate answers to your queries. 

## Requirements
### Conda Environment
Though one can use virtualvenv for virtual environments, it is standard to resort to conda environments. 

Clone the repository and change into it: 
```shell
$ git clone https://github.com/akshathmangudi/SummarizeVideo.git
$ cd SummarizeVideo/
```

For Python 3.6+ users: 
```shell
$ python -m venv /path/to/virtualenv
```

Create a conda environment:
```bash
$ conda -V
$ conda update conda
$ conda create -n <envname> python=3.10 anaconda
$ conda activate <envname>
```
### NOTE: Running PyTorch requires Python version to be less than 3.12, use version 3.10 instead.

For deactivation: 
```bash
$ conda deactivate
```

### Installing dependencies
To install the dependencies required for the streamlit application to run, run the follow command
```shell
$ pip install -r requirements.txt
```

## Licensing
This repository is licensed under the MIT License. See the LICENSE file for details.

## Help
If there are any queries, please write to: 
1. akshath: akshathmangudi@gmail.com (or)
2. ivan: mail.ivanchristo@gmail.com
