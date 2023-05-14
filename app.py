from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file:
        size = len(file.read())
        size_kb = size / 1000.0
        print(f'The size of the picture is {size_kb:.2f} kilobytes.')
        response = make_response(f'The size of the picture is {size_kb:.2f} kilobytes.')
        response.headers['Access-Control-Allow-Origin'] = '*'

        return response 
    else:
        return 'No file uploaded', 400

if __name__ == '__main__':
    app.run(debug=True)
