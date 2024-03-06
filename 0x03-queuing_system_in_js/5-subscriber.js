import { createClient } from "redis";

const client = createClient()
  .on("error", (err) => {
    console.error("Redis client not connected to the server: " + err);
  })
  .on("connect", () => {
    console.log("Redis client connected to the server");
  });
client.subscribe("holberton school channel");
client.on("message", (channel, msg) => {
  console.log(msg);
  if (msg === "KILL_SERVER") {
    client.unsubscribe("holberton school channel");
    client.quit();
  }
});
