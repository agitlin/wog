from flask import Flask, render_template_string
from score import get_score
app = Flask(__name__)

@app.route('/')
def serve_template_string ():
    template ='''
    <html>
    <head>
        <title>Scores Game</title>
    </head>
    <body>
        <h1>The score is:</h1>
        <div id="score">{{SCORE}}</div>
    </body>
</html>
    '''
    value=get_score()
    if int(value)>0:
        return render_template_string(template,SCORE=value)
    else:
        # can't happen
        return render_template_string('<html></html>')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8777)