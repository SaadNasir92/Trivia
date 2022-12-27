import requests as rq

parameters = {
    'amount': 10,
    'type': 'boolean'

}

request = rq.get(url='https://opentdb.com/api.php', params=parameters)
data = request.json()

question_data = data['results']
