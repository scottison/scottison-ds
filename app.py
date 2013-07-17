from flask import Flask, jsonify
from flask import render_template
from flask.ext import restful
import mimerender

mimerender = mimerender.FlaskMimeRender()

render_json = jsonify
render_html = lambda message: "<html>%s</html>" % message
render_xml = lambda message: "<text>%s</text>" % message
render_txt = lambda message: message

app = Flask(__name__)
app.debug = True



@app.route('/main')
@mimerender(
    default = 'html',
    html = render_html,
    json = render_json,
    xml = render_xml,
    txt = render_txt

)
def main(name='world'):
    return {'message': 'Hello, ' + name + '!'}

@app.route('/')
def hello_world():
    return render_template('layout.html', name='scott')

@app.route('/go')
def go():
    return render_template('gone.html', name='have gone')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404error.html')

if __name__ == '__main__':
    app.run()
