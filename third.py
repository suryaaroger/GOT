from flask import Flask

app = Flask(__name__)

@app.route('/')
def myfun():
    return 'hello surya'
 
if __name__ =='__main__':
    app.run()
    
    