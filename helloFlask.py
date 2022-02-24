from bottle import run,get
animals=[{'name':'aaaa','type':'bbbbb'},{'name':'cccc','type':'dddd'},
         {'name':'eeee','type':'ffff'}]
@get('Test.py')
def getall():
    return {'animals':animals}
run(reloader=True,debug=True)