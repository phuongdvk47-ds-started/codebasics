# codebasics
practice tutorials of codebasic channel on youtube


## preparation
* Install conda
* Create envornment for tensorflow 
```bash
conda create --name py39tf2gpu python=3.9 -y

```
* Install Visual Studio Code and Plugins (WSL, Python, Python Environment Manager, Docker, Dev Containers...)


### NLP Tutorial

reference: 
* Spacy Tutorials https://www.tutorialspoint.com/spacy/spacy_models_and_languages.htm
* Spacy Source https://github.com/explosion/spacy-models
* Build your first NLP application https://www.firstlanguage.in/

active python env
```bash
conda env list
# example, env name "py39tf2gpu"
conda activate py39tf2gpu
pip install nltk spacy
python -m spacy download en
## You can now load the package via spacy.load('en_core_web_sm')

##
#python -m spacy download en_core_web_lg
pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.0.0/en_core_web_sm-3.0.0-py3-none-any.whl
# You can now load the package via spacy.load('en_core_web_lg')
#python -m spacy download en_core_web_md
# You can now load the package via spacy.load('en_core_web_md')

pip install pyvi https://gitlab.com/trungtv/vi_spacy/-/raw/master/vi_core_news_lg/dist/vi_core_news_lg-0.0.1.tar.gz

```

