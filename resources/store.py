from flask_restful import Resource, reqparse
from models.store import StoreModel

class Store(Resource):

    ##parser = reqparse.RequestParser()
    ##parser.add_argument("name", type=str, required=True, help="this field can not be empty")

    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json(), 200
        return {'message': "store not found"}, 404
    
    def post(self, name):
        ##data = Store.parser.parse_args()
        if StoreModel.find_by_name(name):
            return {'message': f"store with name {name} already exists"}, 400
        
        store = StoreModel(name)

        try:
            store.save_to_db()
        except:
            return {'message': "An error occured!"}, 500
        
        return store.json(), 201
    
    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
        return {"message": "deleted from database"}

class StoreList(Resource):
    def get(name):
        return {'stores': [store.json() for store in StoreModel.query.all()]}