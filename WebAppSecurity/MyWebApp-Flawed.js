const express = require("express");
const path = require("path");
const app = express();
const port = 3000;
const multer = require('multer');
const crypto = require('crypto');
const fs = require('fs');

// Serve static HTML content
app.get("/", (req, res) => {
    res.send("<h1>Welcome to My Web Application</h1>\r\n<p><img src='/image?filename=kuva2.jpg' /></p>");
});

// Endpoint to serve images
app.get("/image", (req, res) => {
    let filename = req.query.filename;

    let clean_filename = filename.replace(/[^a-zäöå\.]/gi, "")

    const option = {
        root: path.join(__dirname)
    }

    let filepath = path.join(__dirname, clean_filename);
    console.log(`Serving image at path "${filepath}".`);

    // Send the requested file
    res.sendFile(clean_filename, option, (err) => {
        if (err) {
            res.status(404).send("Image not found");
        }
    });
});

app.listen(port, () => {
    console.log(`Server is running at http://localhost:${port}`);
});

