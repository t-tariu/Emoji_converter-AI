from flask import Flask, render_template, request
from utils.emoji_converter import convert_to_emoji

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    emoji_result = None 
    if request.method == 'POST':
        user_text = request.form.get('user_input')
        emoji_result = convert_to_emoji(user_text)
    return render_template('index.html', result=emoji_result)

if __name__ == "__main__":
    app.run(debug=True)
