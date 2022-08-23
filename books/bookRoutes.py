from DBconnection import connection

from flask import Flask
from flask import jsonify, request

# connection to DB
collections = connection()


def book_routes(endpoints):
    @endpoints.route('/add-book', methods=['POST'])
    def add_books():
        resp = {}
        try:
            req_body = request.json
            collections.insert_one(req_body)

            print("Book Data Stored Successfully in the Database.")

            status = {
                "statusCode": "200",
                "statusMessage": "Book Data Stored Successfully in the Database."
            }
        except Exception as e:
            print(e)
            status = {
                "statusCode": "400",
                "statusMessage": str(e)
            }
        resp["status"] = status
        return resp

    @endpoints.route('/read-books', methods=['GET'])
    def read_books():
        resp = {}
        try:
            books = collections.find({})
            print(books)
            books = list(books)
            status = {
                "statusCode": "200",
                "statusMessage": "Book Data Retrieved Successfully from the Database."
            }
            output = [{'Name': book['Name'], 'Author': book['Author']}
                      for book in books]
            resp['data'] = output
        except Exception as e:
            print(e)
            status = {
                "statusCode": "400",
                "statusMessage": str(e)
            }
        resp["status"] = status
        return resp

    @endpoints.route('/update-books', methods=['PUT'])
    def update_books():
        resp = {}
        try:
            req_body = request.json
            collections.update_one({"Author": req_body['Author']}, {
                                   "$set": req_body['updated_book_body']})
            print("Book Data Updated Successfully in the Database.")
            status = {
                "statusCode": "200",
                "statusMessage": "Book Data Updated Successfully in the Database."
            }
        except Exception as e:
            print(e)
            status = {
                "statusCode": "400",
                "statusMessage": str(e)
            }
        resp["status"] = status
        return resp

    @endpoints.route('/delete', methods=['DELETE'])
    def delete():
        resp = {}
        try:
            delete_author = request.args.get('delete_author')
            collections.delete_one({"Author": delete_author})
            status = {
                "statusCode": "200",
                "statusMessage": "User Data Deleted Successfully in the Database."
            }
        except Exception as e:
            print(e)
            status = {
                "statusCode": "400",
                "statusMessage": str(e)
            }
        resp["status"] = status
        return resp
    return endpoints
