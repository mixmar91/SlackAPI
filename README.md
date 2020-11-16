# SlackAPI

Before run the above code, you should follow the next steps:

   ### 1. Installing slackclient
The name of the package we'll use is called slackclient, and it can be installed using pip. To install locally you can run:

pip install slackclient


   ### 2. Generate a Slack API token
To generate a Slack API token, you'll need to run do the following:

* Create a new Slack App

To start, you'll need to create a Slack App. Follow the link, and click Create New App. The process is fairly self-explanatory.

* Add permissions

In the menu on the left, find OAuth and Permissions. Click it, and scroll down to the Scopes section. Click Add an OAuth Scope. Search for the chat:write scope, and add it. At this point, you'll need to re-install the app in your workspace for the permissions to take effect.

* Copy the token URL

On the same page you'll find your access token under the label Bot User OAuth Access Token. Copy this token, and save it for later.
  
  
  ### 3. Add the bot to a channel
In the Slack application, choose a channel that you want the bot to interact with. Click the Conversation Settings icon (the cog), and then click Add an app.

Search for your app name, then click Add.
