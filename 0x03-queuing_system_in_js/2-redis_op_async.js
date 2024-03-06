import { createClient, print } from "redis";
import { promisify } from "util";
let client;

async function getClient() {
  if (!client) {
    client = createClient({
      url: "redis://root@localhost:6379",
    });

    client.on("connect", () => {
      console.log("Redis client connected to the server");
    });

    client.on("error", (err) => {
      console.error("Redis client not connected to the server: ", err);
    });

    client.getAsync = promisify(client.get).bind(client);
    client.setAsync = promisify(client.set).bind(client);
  }
  return client;
}

async function setNewSchool(schoolName, value) {
  const connection = await getClient();
  await connection.setAsync(schoolName, value   );
}

async function displaySchoolValue(schoolName) {
  const connection = await getClient();
  const value = await connection.getAsync(schoolName);
  console.log(value);
}
displaySchoolValue("Holberton");
setNewSchool("HolbertonSanFrancisco", "100");
displaySchoolValue("HolbertonSanFrancisco");
