# Maplecroft Twitter

Maplecroft Twitter is a simple Flask application that displays the last 10 tweets of a Twitter account with an interactive map displaying the location of all the countries hashtags (e.g #China) that also exist in the csv `countries_coordinates.csv`.


## Usage

Clone this repo
```
git clone
```

Install the requirements
```
pip install -r requirements.txt
```

Specify the twitter account
* open `config.py` and in the class `ProductionConfig` update the `ACCOUNT_NAME` value with the Twitter account username you wish to use.

Start the application
```
python app.py
```

Open your browser and go to `http://localhost:5000/`.
