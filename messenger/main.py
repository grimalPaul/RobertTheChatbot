import messenger

if __name__ == '__main__':
    #messenger.app.config['DEBUG'] = True
    messenger.app.run(host="0.0.0.0", port=5005)