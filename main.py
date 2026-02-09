from app import app

@app.route('/')
def homepage():
    return "Esse é meu site"

if __name__ == '__main__':
    app.run(debug=True)