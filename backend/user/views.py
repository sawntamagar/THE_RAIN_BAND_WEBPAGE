from flask import Blueprint, jsonify, request
from user.models import User, Role
from constant import HTTP_400_BAD_REQUEST 
from user import db
from flask_login import current_user




views = Blueprint('views', __name__)


@views.route('/user', methods = ['GET'])
def getpets():
     all_user = []
     users = User.query.all()
     for user in users:
          results = {
                    "id":user.id,
                    "username":user.username,
                    "email":user.email,
                     }
          all_user.append(results)

     return jsonify(
            {
                "success": True,
                "users": all_user,
                
            }
        )


@views.route("/update/<int:id>", methods = ["PUT"])
def update_pet(id):
    user = User.query.get(id)
    username = request.json['username']
    email = request.json['email']

    if user is None:
        abort(404)
    else:
        user.username = username
        user.email = email
        db.session.add(user)
        db.session.commit()
        return jsonify({"success": True, "response": "User Details updated"})
     
    
@views.route('/delete/<int:id>', methods = ['DELETE'])
def delete(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return {'message': "Data deleted"} 



# @views.route('/role/<int:id>', methods = ['GET', 'POST'])
# def role(id):
#     if request.method == 'POST':
#         users = User.query.all()
#         user_id = Role(name=request.json['name'])
#         # name = request.json['name']
     
#         db.session.add(m)
#         db.session.commit()
#         return jsonify({"success": "role has been created"})
#     else:
#         return jsonify({"error: not accessible"})
    
    
@views.route("/role", methods=["POST"])
def create_category():

    name = request.json['name']

    if 'name' in request.json:
        name = request.json['name']
    else:
        name = ""

    new_role = Role(name)

    db.session.add(new_role)
    db.session.commit()

    result = (new_role) 

    data = {
        'message': 'New Category Created!',
        'status': 201,
        'data': result
    }
    return make_response(jsonify(data))



# endpoint to GET all categories
@views.route("/role", methods=["GET"])
def get_categories():

    all_roles = Role.query.all()
    result = (all_roles)

    data = {
        'message': 'roles!',
        'status': 200,
        'data': result
    }
    return make_response(jsonify(data))



# endpoint to GET category detail by id
@views.route("/role/<int:id>", methods=["GET"])
def get_category(id):

    role = Role.query.get(id)

    if(role):
        result = (role)
        data = {
            'message': 'role Info!',
            'status': 200,
            'data': result
        }
    else:
        data = {
            'message': 'Invalid Category ID!',
            'status': 200
        }
    return make_response(jsonify(data))



# endpoint to UPDATE category
# @views.route("/role/<int:id>", methods=["PATCH"])
# def update_category(id):

#     role = Role.query.get(id)

#     if(role):
#         if 'name' in request.json:
#             role.name = request.json['name']
#         if 'short_desc' in request.json:
#             category.short_desc = request.json['short_desc']

#         db.session.commit()
#         result = category_schema.dump(category)
        
#         data = {
#             'message': 'Category Info Edited!',
#             'status': 200,
#             'data': result
#         }

#     else:
#         data = {
#             'message': 'Invalid Category ID!',
#             'status': 200
#         }
#     return make_response(jsonify(data))



# # endpoint to DELETE category
# @views.route("/category/<int:id>", methods=["DELETE"])
# def delete_category(id):

#     category = Category.query.get(id)

#     if(category):
#         db.session.delete(category)
#         db.session.commit()

#         data = {
#             'message': 'Category Deleted!',
#             'status': 200
#         }
#     else:
#         data = {
#             'message': 'Invalid Category ID!',
#             'status': 200
#         }
#     return make_response(jsonify(data))
