const express = require('express');
const fs = require('fs');
const { execSync } = require('child_process');

const app = express();

// Endpoint to execute shell command
app.get('/execute', (req, res) => {
    const command = req.query.command;
    try {
        let output = '';

        // Handle different commands to display different files
        if (command === 'docker-alpine-hello') {
            output = '<!DOCTYPE html>' +
                '<html lang="en">' +
                '<head>' +
                '<meta charset="UTF-8">' +
                '<meta name="viewport" content="width=device-width, initial-scale=1.0">' +
                '<title>Dockerfile Contents</title>' +
                '<style>' +
                'body {' +
                '    background-color: #00FF00; /* Neon green background color */' +
                '}' +
                'pre {' +
                '    color: purple; /* Purple text color */' +
                '}' +
                '</style>' +
                '</head>' +
                '<body>' +
                '<h1>Contents of Dockerfile in docker-alpine-hello:</h1>' +
                '<pre>' +
                'FROM alpine:latest\n' +
                'CMD ["echo", "Hello, World!"]' +
                '</pre>' +
                '</body>' +
                '</html>';
        }
        // Add more conditions for other files if needed

        // Send the output as response
        res.send(output);
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

