from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from pkg_resources import resource_exists
import json

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite.db'
db = SQLAlchemy(app)

resource_fields = {
    'id': fields.Integer,
    'company': fields.String,
    'question': fields.String,
}


class QuestionModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(100), nullable=False)
    question = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return f"Question(id = {id}, comapany = {company}, question = {question})"


question_put_args = reqparse.RequestParser()
question_put_args.add_argument("company", type=str, help="Name of company is required", required=True)
question_put_args.add_argument("question", type=str, help="question is required", required=True)


@marshal_with(resource_fields)
def convertToJSON(qmObj):
    return qmObj


class Questions(Resource):
    @marshal_with(resource_fields)
    def get(self, question_id):
        result = QuestionModel.query.filter_by(id=question_id).first()
        if (not result):
            abort(404, message="Could not find question with that id...")
        return result

    @marshal_with(resource_fields)
    def put(self, question_id):
        args = question_put_args.parse_args()
        question = QuestionModel(id=question_id, company=args['company'],
                                 question=args['question'])
        db.session.add(question)
        db.session.commit()
        return question, 201


class CompanySpecificQuestions(Resource):
    @marshal_with(resource_fields)
    def get(self, companyName):
        result = QuestionModel.query.filter_by(company=companyName).all()
        if (not result):
            abort(404, message="Could not find question with that company...")
        asList = []
        for _ in result:
            asList.append(convertToJSON(_))
        return (asList)


api.add_resource(Questions, "/question/<int:question_id>")
api.add_resource(CompanySpecificQuestions, "/question/<string:companyName>")

if __name__ == "__main__":
    app.run(debug=True)


