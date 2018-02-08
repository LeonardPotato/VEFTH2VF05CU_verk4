from bottle import route, run, template, static_file, error
import json

""""
f = open('bekkur.json', 'r')

bekkur = json.load(f)

f.close()
"""
with open('bekkur.json', 'r', encoding='utf-8')as f:
    bekkur = json.load(f)

print(bekkur['nemendur'][0]['kt'])

@route('/')
def index():
    return template('index', bekkur = bekkur)

@route('/nemandi/<kt>')
def nemandi(kt):
    return template('nemandi', kt=kt, bekkur=bekkur)

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./myfiles')

@error(404)
def error404(error):
    return '<h1>[404] Siðan er ekki til.</h1>'

@error(500)
def error500(error):
    return '<h1>[500] Villa á miðlara</h1>'

run()