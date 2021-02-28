# 1000 dots

## Description

### Implementation description

- Created a dashboard app with **Dash** (Plotly) and with routing by url supporting
- Application communicate with fake mock data generator as possible API data providing services are not support 
  to share history of the prices for BTC for their free paid subscribers.
- Taken data is a set of the BTC prices and its timestamps. In use for building the statistical chart.
- Chart view is configurable with next parameters: interval => [15m, 1h, 1d] . 

## How to launch

There are two ways how to launch application

### For Production (with Docker-Compose)

If you have a docker installed on your machine, it's much easier to launch the application `$( docker-compose up )`,

now application accessed on [http://localhost]

To stop the application run the command `$( docker-compose down )`

### For Development (with many hand steps)

Note: please have Python3+ installed on your machine. 

#### Configure environment

Note: To keep work environment (workstation) clean, please use local env `python -m venv env` and please use in command below the python instance from local environment (Windows)`env\Script\python.exe` or (Linux) `env\bin\python3`

Create local env `$( python3 -m venv env )`

Install dependencies `$( ./env/bin/pip3 intall -r requirements.txt )`

Note: for freezing deps use `$( ./env/bin/pip3 freeze > requirements.txt )`

#### Launch app

`$( ./env/bin/python main.py )`

To stop the app needs to terminate process or close console `Ctrl + C`.
