while True:
    def time():
        from datetime import datetime
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(time())