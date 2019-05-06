# Robo-Advisor

Allows users to use the AlphaVantage API to select stocks and receive recommendations on whether or not they should purchase them. 

## Prerequisites

-Python 3.7.

-pip

## Installation 

First, clone or download this repository locally. Then install the packages in the requirements.txt file via the following line in the command line:

```
pip install -r requirements.txt
```

## Usage

1. Procure an API key from https://www.alphavantage.co/


2. create a .env file and add your API key to it as follows:
```
ALPHAVANTAGE_API_KEY= "Your Key"
```

3. Run the program:

```
python app/robo_advisor.py
```

4. Follow the on-screen instructions.

## Tests

In order to perform a test, enter the following line into the command line:

```sh
pytest
```


