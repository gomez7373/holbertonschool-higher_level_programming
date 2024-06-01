const express = require('express');
const fs = require('fs');
const path = require('path');

const app = express();

// Endpoint to execute shell command
app.get('/execute', (req, res) => {
    const command = req.query.command;
    try {
        let output = '';

        // Handle different commands to display different files
        if (command === 'github_actions') {
            const filePath = path.join(__dirname, 'github_actions', 'docker-image.yml');
            output = 'Contents of docker-image.yml in github_actions:\n\n';
            output += fs.readFileSync(filePath, 'utf-8');
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

