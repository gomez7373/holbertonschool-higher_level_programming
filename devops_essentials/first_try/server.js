const express = require('express');
const fs = require('fs');
const { execSync } = require('child_process');

const app = express();

// Serve the index.html file as the default route
app.get('/', (req, res) => {
    // Read the index.html file and send it as response
    fs.readFile('./index.html', 'utf-8', (err, data) => {
        if (err) {
            res.status(500).send(err.message);
        } else {
            res.send(data);
        }
    });
});

// Serve the styles.css file
app.get('/styles.css', (req, res) => {
    // Read the styles.css file and send it as response
    fs.readFile('./styles.css', 'utf-8', (err, data) => {
        if (err) {
            res.status(500).send(err.message);
        } else {
            // Set the content type to CSS
            res.setHeader('Content-Type', 'text/css');
            res.send(data);
        }
    });
});

// Endpoint to execute shell command
app.get('/execute', (req, res) => {
    const command = req.query.command;
    try {
        let output = '';

        // Handle different commands to display different files
        if (command === 'docker-alpine-hello') {
            output = 'Contents of Dockerfile in docker-alpine-hello:\n\n';
            output += fs.readFileSync('./docker-alpine-hello/Dockerfile', 'utf-8');
        } else if (command === 'docker-alpine-extended') {
            output = 'Contents of Dockerfile in docker-alpine-extended:\n\n';
            output += fs.readFileSync('./docker-alpine-extended/Dockerfile', 'utf-8');
            output += '\n\nContents of config.txt:\n\n';
            output += fs.readFileSync('./docker-alpine-extended/config.txt', 'utf-8');
        } else if (command === 'github_actions') {
            output = 'Contents of docker-image.yml in github_actions:\n\n';
            output += fs.readFileSync('./github_actions/.github/workflows/docker-image.yml', 'utf-8');
        }
        // Add more conditions for other files if needed

        // Send the output as response with HTML markup
        res.send(`<pre>${output}</pre>`);
    } catch (error) {
        // Handle error
        res.status(500).send(error.message);
    }
});

// Start the server
const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});

