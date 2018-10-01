from flask import Flask, jsonify, request
app = Flask(__name__)

books = [
    {'id': 0,
     'chapter': '1',
     'name': 'Harry Potter and Philosopher stone'},
     {'id': 1,
     'chapter': '2',
     'name': 'Harry Potter and Chamber of secret'},
     {'id': 2,
     'chapter': '3',
     'name': 'Harry Potter and Prisoner of Azkaban'},
    {'id': 3,
     'chapter': '4',
     'name': 'Harry Potter and Goblet of fire'},
    {'id': 4,
     'chapter': '5',
     'name': 'Harry Potter and Orden of Phoenix'},
    {'id': 5,
     'chapter': '6',
     'name': 'Harry Potter and Halfblood Prince'},
    {'id': 6,
     'chapter': '7',
     'name': 'Harry Potter and Deathly hallows'}
]
@app.route('/', methods = ['GET'])
def test():
    return jsonify({'message': 'Yaaaas!'})
@app.route('/bks',methods = ['GET'])
def returnAll(): 
    return jsonify({'books': books})

@app.route('/bks/<int:id>',methods = ['GET'])
def returnOne(id):
    bks = [book for book in books if book['id'] == id]
    return jsonify({'book':bks[0]})

@app.route('/bks/<string:word>',methods = ['GET'])
def returnOnes(word):
    bks = [book for book in books if word in book['name']]
    output=[]
    output.append(bks)
    return jsonify({'book':output})

@app.route('/bks/<int:id>', methods =['PUT'])
def editOne(id):
    bks = [book for book in books if book['id']  == id]
    bks[0]['name'] = request.json['name']
    return jsonify({'book': bks[0]})

@app.route('/bks', methods = ['POST'])
def addOne():
    book = {'id':request.json['id'],'chapter': request.json['chapter'],'name': request.json['name']}
    books.append(book)
    return jsonify({'books':books})

@app.route('/bk/<int:id>', methods = ['DELETE'])
def removeOne(id):
    bk = [book for book in books if book['id'] == id]
    books.remove(bk[0])
    return jsonify({'books':books})
if __name__ == '__main__':
    app.run(debug=True,port=8000)