import slack

def send_slack_notification(message, channel):
    client = slack.WebClient(token="YOUR_SLACK_API_TOKEN")  
    response = client.chat_postMessage(channel=channel, text=message)
    if response['ok']:
        print("Notification sent successfully.")
    else:
        print("Failed to send notification.")

if __name__ == "__main__":
    message = "This is a test notification."
    channel = "#your-channel-name"  
    send_slack_notification(message, channel)

