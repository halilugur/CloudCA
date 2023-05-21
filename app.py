from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

quotes = [
    {
        'id': 1,
        'author': 'Oscar Wilde',
        'quote': "Be yourself; everyone else is already taken."
    },
    {
        'id': 2,
        'author': 'Albert Einstein',
        'quote': "Two things are infinite: the universe and human stupidity; and I'm not sure about the universe."
    },
    {
        'id': 3,
        'author': 'Mahatma Gandhi',
        'quote': "Be the change that you wish to see in the world."
    }
]


@app.route('/quotes', methods=['GET'])
def get_quotes():
    return jsonify(quotes)


@app.route('/quotes/<int:index>', methods=['GET'])
def get_quote(index):
    if 0 <= index < len(quotes):
        return jsonify(quotes[index])
    else:
        return jsonify({'error': 'Quote not found'})


@app.route('/quotes', methods=['POST'])
def create_quote():
    quote = request.get_json()
    quote['id'] = len(quotes) + 1
    quotes.append(quote)
    return jsonify({'message': 'Quote created successfully'})


@app.route('/quotes/<int:index>', methods=['PUT'])
def update_quote(index):
    if 0 <= index < len(quotes):
        quote = request.get_json()
        quote['id'] = quotes[index]['id']
        quotes[index] = quote
        return jsonify({'message': 'Quote updated successfully'})
    else:
        return jsonify({'error': 'Quote not found'})


@app.route('/quotes/<int:index>', methods=['DELETE'])
def delete_quote(index):
    if 0 <= index < len(quotes):
        deleted_quote = quotes.pop(index)
        return jsonify({'message': 'Quote deleted successfully', 'quote': deleted_quote})
    else:
        return jsonify({'error': 'Quote not found'})


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
