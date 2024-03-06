import { createClient } from "redis";

async function conn() {
  const client = createClient({
    url: "redis://root@localhost:6379",
  });

  client.on("connect", () => {
    console.log("Redis client connected to the server");
  });

  client.on("error", (err) => {
    console.error("Redis client not connected to the server: ", err);
  });

  return client;
}

conn();
