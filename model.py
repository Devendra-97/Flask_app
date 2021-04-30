import json
from flask_restx import Api,Resource,fields
from flask_restx import reqparse
import logging
from backend import *
from EndpointsRequest import *

app=Flask(__name__)
api=Api(app)
my_topic=api.model('Topic',{'topic':fields.String})

my_answer=api.model('Answers',{'answer':fields.String(),'qid':fields.String()})

my_question=api.model('Question',{'question':fields.String(),'topic':fields.String('')})
logging.basicConfig(level=logging.INFO)
ns1 = api.namespace('api/v1', description='test')

@ns1.route('/questions')
class Question(Resource):
    @api.expect(my_question)
    def post(self):
        status=add_new_question()
        print(status)
        if status:
            ns1.logger.info("Question has successfully posted")
            response = {'result':"Question has successfully added"}
        else:
            ns1.logger.info("Question was not  posted")
            response = {'result':"Question has not  added"}

        return response,200

@ns1.route('/answers/')
class Answers(Resource):
    @api.expect(my_answer)
    def post(self):
        status=add_new_answer()
        print(status)
        if status == True :
            ns1.logger.info("Answer has successfully added")
            response = {'result':"Answer has successfully added"}
        else:
            ns1.logger.info("Answer was not  added")
            response = {'result':"Answer has not  added"}

        return response,200


@ns1.route("/all")
class searchall(Resource):
    def get(self):
        ns1.logger.info("You Have received all entries of DB")
        return get_all()

@ns1.route("/search/<_id>")
class Search(Resource):
    def get(self,_id):
        ns1.logger.info("You are searching by id ")
        return search_by_id(_id)


@ns1.route('/topic/')
class Topic(Resource):
    @api.expect(my_topic)
    def post(self):
        ns1.logger.info("You are searching by Topic")
        return search_by_topic()    
  

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)
