from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
import pymongo

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta


@app.route('/')
def home():
    return render_template('index.html')

# 글 생성
@app.route('/create', methods=['POST'])
def createCard():
    postTitle = request.form['title_give']
    postDescription = request.form['description_give']

    post = {'title': postTitle, 'description': postDescription}

    db.posts.insert_one(post)

    return jsonify({'result': 'success'})


# 글 수정
@app.route('/update', methods=['POST'])
def updateCard():
    beforeTitle = request.form['beforeTitle_give']
    postTitle = request.form['title_give']
    postDescription = request.form['description_give']

    # post = {'title': beforeTitle}, {'$set': {'title': postTitle, 'description': postDescription}}

    db.posts.update_one({'title': beforeTitle}, {'$set': {'title': postTitle, 'description': postDescription}})

    return jsonify({'result': 'success'})

#
# 글 삭제
@app.route('/delete', methods=['POST'])
def deleteCard():
    postTitle = request.form['title_give']

    post = {'title': postTitle}

    db.posts.delete_one(post)

    return jsonify({'result': 'success'})


# 글 읽기
@app.route('/api/memo', methods=['GET'])
def read():
    result = list(db.posts.find({}, {'_id':False}))

    # print(result)

    return jsonify({'result': 'success', 'posts': result})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
