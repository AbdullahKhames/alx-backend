import { createClient, print } from "redis";

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
async function setNewSchool(schoolName, value) {
  const connection = await conn();
  connection.set(schoolName, value, print);
}
async function displaySchoolValue(schoolName) {
  const connection = await conn();
  connection.get(schoolName, (err, reply) => {
    if (err) {
      console.error(err);
    } else {
      console.log(reply);
    }
  });
}
displaySchoolValue("Holberton");
setNewSchool("HolbertonSanFrancisco", "100");
displaySchoolValue("HolbertonSanFrancisco");
