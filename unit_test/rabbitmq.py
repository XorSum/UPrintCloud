from util import rabbitmq

if __name__ == '__main__':
    username = 'master'
    passwd = 'admin'
    uri = 'debian-docker'
    queue = 'job'
    while True:
        content = input()
        rabbitmq.push(uri, username, passwd, content, queue)
        print("send '%s' to queue: %s" % (content, queue))
