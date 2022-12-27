# Trivia
Trivia game using a Trivia DB API
To change the questions/amount of questions, goto: https://opentdb.com/api_config.php

THE SELECT TYPE FIELD MUST BE TRUE/FALSE, rest is to your liking. 

Once complete, click generate API URL:

How to read the API URL:

For Example: https://opentdb.com/api.php?amount=10&category=11&difficulty=medium&type=boolean

Everything before the '?' is the API URL that will replace the URL in the 'Get' method of the requests object in the UI.py file.
the items after such as 'amount = 10', 'category'=11, 'difficulty'=medium, 'type'=boolean must be put in dictionary form in the parameters variable in the UI.py file.
