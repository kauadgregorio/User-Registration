from app import app

@app.route('/')
def homepage():
    return "Serpa cagão!"

if __name__ == '__main__':
    app.run(debug=True)