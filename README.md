# 🚀 Python Socket FTP Server & Client

A beginner-friendly FTP-style project that uses **Python's socket programming** to send and receive files over TCP between clients and a server on `localhost`.

---

## 📂 Features

- 🔌 Supports multiple clients for file upload  
- 💾 Saves each file dynamically as `output0.txt`, `output1.txt`, etc.  
- 🧠 Simple, modular, and well-commented code  
- ❗ Handles basic errors (e.g., missing file)  
- 🧪 Great for learning about TCP, sockets, and file handling  

---

## 🛠️ Technologies Used

- Python 3.x 🐍  
- TCP/IP Socket Programming

---

## 📁 Project Structure

```
ftp-socket-python/
├── server.py         # Server to receive files from multiple clients
├── client.py         # Client to send a selected file to the server
└── README.md         # Project documentation (this file)
```

---

## ⚙️ Getting Started

### 🐍 Prerequisites

Make sure Python 3 is installed:

```bash
python --version
```

---

### 🚀 Running the Project

#### 🖥️ Step 1: Start the Server

In your terminal:

```bash
python server.py
```

> 🧑‍💻 Enter how many clients you expect to connect.

---

#### 💻 Step 2: Start the Client(s)

In another terminal (can run multiple times in parallel):

```bash
python client.py
```

> 📤 Enter the **filename** of the file you want to send (should be in the same directory).

---

## 📸 Screenshots

<details>
  <summary>✅ Server Output</summary>

  ![Server Output](https://via.placeholder.com/600x300.png?text=Server+Receiving+Files)
</details>

<details>
  <summary>📤 Client Sending File</summary>

  ![Client Output](https://via.placeholder.com/600x300.png?text=Client+Sending+Files)
</details>

---

## 🧠 How It Works

- The **server** listens for multiple client connections.
- Each **client** connects, opens a text file, reads its content, and sends it in chunks.
- The server receives the file and writes it to a new `.txt` file using a unique name.
- When all clients are done, the server saves and closes the connections.

---

## 🚧 Future Improvements

- 🔄 Add file integrity checks (checksum)  
- 📦 Add file metadata transfer (filename, size, timestamp)  
- 🌐 Allow remote IP configuration  
- 🧵 Use multithreading for concurrent client handling  
- 🖥️ Build a GUI using Tkinter or PyQt  

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repo, improve the logic, and submit a pull request.  
If you liked the project, consider giving it a ⭐!

---




