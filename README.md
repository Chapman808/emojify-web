# emojify-web

This is a little web app I wrote for my friend group's discord server. It interfaces with the Discord API to upload custom server emojis based on the user avatars of members of the sever.
There is also a functionality to create a doodle on the web app and upload it as an emoji 


At one point, this app was running on an EC2 instance in AWS.

CREDIT: The JS for the doodle is based on code from a tutorial.


## Future improvments

- This app uses some hardcoded data for discord roles, etc. To make this a fully generalized bot, it should use configuration files for this.
- Cloud integration: AWS CDK or Cloudformation IAC for DB and web application.
