from flask import abort, make_response
from ..db import db

def create_model(cls, model_data): 
    class_attributes = cls.attr_list()
        
    for attribute in class_attributes:
        try:
            attribute = model_data[attribute]
        except KeyError as error:
            response = {"details": f"Invalid request: missing {error.args[0]}"}
            abort(make_response(response, 400))
            
    new_model = cls.from_dict(model_data)
    db.session.add(new_model)
    db.session.commit()

    return new_model.to_dict()

def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except ValueError:
        abort(make_response({"details": f"{cls.__name__} with id {model_id} is invalid"}, 400))

    query = db.select(cls).where(cls.id == model_id)
    model = db.session.scalar(query)
    
    if not model:
        abort(make_response({"details": f"{cls.__name__} with id {model_id} does not exist"}, 404))
    
    return model