# Web Service

## Requirements

Install dependencies:

    for req in $(cat requirements.txt); do pip install $req; done

Set up caffe path:

    PYTHONPATH="/userpath/caffe/python":PYTHONPATH
    export $PYTHONPATH

## Run

    % python app.py

    Options:
      -h, --help            show this help message and exit
      -d, --debug           enable debug mode
      -p PORT, --port=PORT  which port to serve content on
