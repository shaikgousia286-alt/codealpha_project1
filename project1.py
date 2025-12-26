const express = require("express");
const mongoose = require("mongoose");
const cors = require("cors");
const http = require("http");
const socketio = require("socket.io");

const app = express();
const server = http.createServer(app);
const io = socketio(server, { cors: { origin: "*" } });

app.use(cors());
app.use(express.json());

mongoose.connect("mongodb://127.0.0.1:27017/project_manager");

io.on("connection", (socket) => {
  console.log("User connected");

  socket.on("newComment", (data) => {
    io.emit("commentUpdate", data);
  });

  socket.on("disconnect", () => {
    console.log("User disconnected");
  });
});

app.use("/api/auth", require("./routes/auth"));
app.use("/api/projects", require("./routes/project"));
app.use("/api/tasks", require("./routes/task"));

server.listen(5000, () => console.log("Server running on port 5000"));