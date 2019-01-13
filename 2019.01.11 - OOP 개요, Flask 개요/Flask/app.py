from flask import Flask, render_template

app = Flask(__name__)   # 고정 부분

@app.route('/')   # 홈 주소
def index():
    return '안녕하세요'

@app.route('/html')
def html():
    return render_template('chicken.html')

# chicken.html 페이지를 띄우기

@app.route('/html_name/<string:name>')
def html_name(name):
    return render_template('chicken.html', your_name=name)


@app.route('/dictionary/<string:word>')
def dictionary(word):
    word_dict = {"apple": "사과", "banana": "바나나"}
    return render_template('dictionary.html', word=word, word_dict = word_dict)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)

