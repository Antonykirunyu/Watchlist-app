from app import app

if __name__ == '__main__':
    app.run()
    
    app.run(debug = True)

    # Creating app instance
app = create_app('development')

manager = Manager(app)
manager.add_command('server',Server)