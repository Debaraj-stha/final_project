from app import create_app, db, User



if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)