from flask import Flask
from flask_restful import Resource, Api
# create a flask object
app = Flask(__name__)
api = Api(app)

# creating a class for Books that will hold
# the accessors
class Books(Resource):
    def get(self):
        return {
            'books': ['1984', 'The Hobbit', 'Sapiens', 'The Alchemist']
        }

# adds the resources at the root route
api.add_resource(Books, '/')

# if this file is being executed then run the service
if __name__ == '__main__':
    # run the service
    app.run(host='0.0.0.0', port=80, debug=True)
