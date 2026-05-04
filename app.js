const dbPassword = process.env.DB_PASSWORD;

const config = require("./config.json");

console.log("DB Host:", config.dbHost);
console.log("DB User:", config.dbUser);

// NEVER print password in real apps (only for testing)
console.log("Password loaded from Secrets Manager");

// Example DB connection (pseudo)
console.log("Connecting to database...");