# Real Estate ChatBot

### A simple chat bot in Sinhale for real estate domain built using [RASA](https://rasa.com/docs/).

## Required libraries & packages

- Python
- Anaconda
- Rasa
- Tensorflow
- ujson

## Instructions for run the project

1. Install Anaconda and create a virtual environment
2. Install RASA and necessary python libraries using Anaconda.
3. Clone the repository.
4. Go to root folder.
5. In a seperate terminal execute `rasa run actions` to run actions.
6. Run `python -m http.server` to start http server.
7. Run `rasa run` to start chat bot in terminal or run `rasa run --enable-api --cors="*"` to chat on web browser [http://localhost:8000/](http://localhost:8000/).

## Queries

- Get District information from user
- Get land type information from user (Residential or Business)
- Get required perch price from user.
- Search and Provide project Details.
- Provide Agent details who assigned to the selected project

## Useful Commands

- `conda install -c [channel_name] [package_name]` - install a package using anaconda
- `rasa init` - initiate new RASA project
- `rasa train` - train new model
- `rasa shell` - load most recently trained model
- `rasa run` - start chat bot with the trained model
- `rasa run actions` - run actions
- `rasa run --enable-api --cors="*"` - run server with allow API and all CORS
- `python -m http.server` - start a basic http server
