import slack

def sendSlackMessage(token, channel, message):
    client = slack.WebClient(token=token)
    client.chat_postMessage(channel=channel, text=message)

if __name__ == '__main__':
    token = 'xoxb-1645416874523-1374846945645-4gsdgferghefGDFhgaewGawe'
    channel = "#my-channel"
    message = "Test slack from python!"
    sendSlackMessage(token, channel, message)