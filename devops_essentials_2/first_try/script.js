<script>
// Function to fetch outputs from server
function fetchOutputs() {
    // Array of commands to execute
    const commands = [
        "cd ~/holberton_projects/holbertonschool-higher_level_programming/devops_essentials/docker-alpine-hello && if [ -f Dockerfile ]; then echo 'Dockerfile exists in docker-alpine-hello directory' && cat Dockerfile; else echo 'Dockerfile does not exist in docker-alpine-hello directory'; fi",
        "cd ~/holberton_projects/holbertonschool_higher_level_programming/devops_essentials/docker-alpine-extended && if [ -f Dockerfile ]; then echo 'Dockerfile exists in docker-alpine-extended directory' && cat Dockerfile; else echo 'Dockerfile does not exist in docker-alpine-extended directory'; fi && if [ -f config.txt ]; then echo 'config.txt exists in docker-alpine-extended directory' && cat config.txt; else echo 'config.txt does not exist in docker-alpine-extended directory'; fi",
        "cd ~/holberton_projects/holbertonschool_higher_level_programming/devops_essentials/github_actions/.github/workflows && if [ -f docker-image.yml ]; then echo 'docker-image.yml exists in .github/workflows directory' && cat docker-image.yml; else echo 'docker-image.yml does not exist in .github/workflows directory'; fi",
        "cd ~/holberton_projects/holbertonschool_higher_level_programming/devops_essentials/docker-volumes && if [ -f Dockerfile ]; then echo 'Dockerfile exists in docker-volumes directory' && cat Dockerfile; else echo 'Dockerfile does not exist in docker-volumes directory'; fi",
        "cd ~/holberton_projects/holbertonschool_higher_level_programming/devops_essentials/docker-compose && if [ -f docker-compose.yml ]; then echo 'docker-compose.yml exists in docker-compose directory' && cat docker-compose.yml; else echo 'docker-compose.yml does not exist in docker-compose directory'; fi"
    ];

    // Container to hold outputs
    const outputContainer = document.getElementById("output-container");

    // Fetch outputs for each command
    commands.forEach(command => {
        // Create a paragraph element to display output
        const outputElement = document.createElement("p");
        // Execute command and update output
        outputElement.textContent = executeCommand(command);
        // Append output to container
        outputContainer.appendChild(outputElement);
    });
}

// Function to execute terminal command and return output
function executeCommand(command) {
    // Use synchronous XMLHttpRequest to execute shell command
    const xhr = new XMLHttpRequest();
    xhr.open("GET", "/execute?command=" + encodeURIComponent(command), false);
    xhr.send(null);
    // Return response text
    return xhr.responseText;
}

// Call fetchOutputs function when page loads
window.onload = fetchOutputs;
</script>

