
#### :warning: Merge pull requests into the development branch :warning:

### Setup

1. [Intsall node.js](https://nodejs.org/en/download/), if you havent already
2. Install discord.js
```bash
npm install discord.js
```
3. Create .env.development in /secrets/ and add the following fields, the API token and client_id are found in the [discord developer portal](https://discord.com/developers/applications) and the guild_ID can be found by right clicking the server name in discord and clicking on copy id
```js
DISCORD_API_TOKEN="Your_token" 
DISCORD_GUILD_ID="Guild_id"
DISCORD_CLIENT_ID="Client_id"
```

### Make Bot Here

https://discord.com/developers/applications


### Link to invite to server

https://discord.com/api/oauth2/authorize?client_id=<applicationid>&permissions=8192&scope=bot%20applications.commands


### Environment Variables

Create a /secrets/.env.development and a /secrets/.env.production with the following structure


### Running the bot

To run the program with  `npm start production` for production and `npm start dev` for development
