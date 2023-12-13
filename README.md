# CTQ
Create test questions with AI

## Installation
First, install **Python** with the next command.
```bash
pip install Flask
pip install openai
```
### API Key
Your OpenAI API key needs to be in the server.py file:

```
client = OpenAI(api_key='OPENAI_API_KEY')
```
or You can also add the API key in an environment variable.

```
Name = OPENAI_API_KEY
Variable = api_key
```

#### Running the Application
Execute the following command to get the app up and running:

```
server.py
```

This kickstarts the Flask application. You can then access the web interface by heading to http://localhost:8000 on your web browser.

Usage
To use this feature, enter information in the fields provided and press Create Question to create a test question below.
