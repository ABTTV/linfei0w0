require("dotenv/config.js");
const {Client, IntentsBitField} = require("discord.js");

const client = new Client({
    intents: [
    IntentsBitField.Falgs.Guilds,
    IntentsBitField.Falgs.GuildsMessages,
    IntentsBitField.Falgs.MessageContent,
    ]
})

client.on("ready", () => {
    console.log("The bot is online");
})

client.login(process.env.TOKEN);
