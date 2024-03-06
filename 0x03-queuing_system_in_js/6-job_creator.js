import { createQueue } from "kue";

const queue = createQueue();

const job = queue
  .create("push_notification_code", {
    phoneNumber: "237831654",
    message: "hello world",
  })
  .on("enqueue", () => {
    console.log("Notification job created: " + job.id);
  });

job
  .on("complete", function () {
    console.log("Notification job completed");
  })
  .on("failed", function (errorMessage) {
    console.log("Notification job failed");
  });
job.save();
