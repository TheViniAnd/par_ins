import os.path
import json
import time

from uuid import uuid4
from flask import abort, make_response, request, Flask, jsonify
from celery import Celery
from redis import Redis
from rq.job import Job
from rq import Queue

from get_info_task import get_info



app = Flask(__name__)

@app.route('/api/search/', methods = ['GET'])
def search():
    """
    Запрос в функцию get_info для поиска инн
    """
    list_input = request.json

    for all_details_input in list_input:
        if all_details_input['account'] and all_details_input['email'] and all_details_input['token'] is not None:
            if all_details_input['token'] == '987654321':

                count = len(list_input)
                print(len(list_input))        #кол-во пользователей на поиск
                if count == 1:
                    redis_conn = Redis()     # Сам брокер
                    queue = Queue(connection = redis_conn)      #Подключение

                    job = queue.enqueue(get_info, all_details_input['account'],
                                        all_details_input['email'], job_timeout=-1)


                    while not job.result:
                        return jsonify({'response': {'output': all_details_input['email']}}), 201
                    print(job.result)
                else:
                    return jsonify({'error': 'Максимальное количество аккаунтов: 1!'})
            else:
                return jsonify({'error': 'Неверный токен авторизации'})
        else:
            return jsonify({'error': 'Ошибка переменной'})


@app.route('/api/result/', methods = ['GET'])
def get_result():

    input_task = request.json

    for all_details_input in input_task:
        if all_details_input['token'] and all_details_input['email'] is not None:
            if all_details_input['token'] == 987654321 or all_details_input['token'] == "987654321":

                email = os.path.join('result/' + all_details_input['email'] + '.json')

                with open(email, "rb") as write_file:
                    data = json.load(write_file)
                    #print(data)

                return jsonify(
                    {
                        'status': 'success',
                        'response': data
                    }
                ), 201
            else:
                return jsonify({'error': 'Неверный токен авторизации'})
        else:
            return jsonify({'error': 'Ошибка переменной'})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
if __name__ == '__main__':
    app.run()
