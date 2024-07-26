
Curriculum
[C#23] Foundations v2 - Part 2
Average: 98.96%
You have a captain's log due before 2024-07-28 (in 2 days)! Log it now!
Project badge
JavaScript DOM manipulation
 Novice
 By: Javier Valenzani
 Weight: 1
 Migrated to checker v2: 
 Manual QA review must be done (request it when you are done with the project)
JavaScript DOM Manipulation
Resources
Read or watch:
What is JavaScript?
Introduction to the DOM
Document Interface
Element Class
Locating DOM elements using selectors
CSS Selectors
CSS Diner Play with Selectors
Client-side Web APIs
Introduction to web APIs
Manipulating documents
Fetching data from the server
What went wrong? Troubleshooting JavaScript
Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
How to select HTML elements in JavaScript
What are differences between ID, class and tag name selectors
How to modify an HTML element style
How to get and update an HTML element content
How to modify the DOM
How to make a request with XmlHTTPRequest
How to make a request with Fetch API
How to listen/bind to DOM events
How to listen/bind to user events
Requirements
General
Allowed editors: All of them.
All your files will be interpreted on Chrome browser (version 57.0 or later)
All your files should end with a new line
A mandatory README.md file with meaningful information about the content, should be placed at the root folder of the project.
Your code should be semistandard compliant
You are not allowed to use var
HTML should not reload for each action: DOM manipulation, update values, fetch data…
Tasks
0. Color Me
mandatory
Write a JavaScript script that updates the text color of the header element to red (#FF0000):

You must use document.querySelector to select the HTML tag
Please test with this HTML file in your browser:

javiercito@ubuntu:~/javascript-dom_manipulation$ cat 0-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <footer>
      Holberton School - 2022
    </footer>
    <script type="text/javascript" src="0-script.js"></script>
  </body>
</html>
javiercito@ubuntu:~/javascript-dom_manipulation$ 
Repo:

GitHub repository: holbertonschool-higher_level_programming
Directory: javascript-dom_manipulation
File: 0-script.js
0/1 pt
1. Click and turn red
mandatory
Write a JavaScript script that updates the text color of the header element to red (#FF0000) when the user clicks on the tag with id red_header:

Please test with this HTML file in your browser:

javiercito@ubuntu:~/javascript-dom_manipulation$ cat 1-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <div id="red_header">Red header</div>
    <footer>
      Holberton School - 2022
    </footer>
    <script type="text/javascript" src="1-script.js"></script>
  </body>
</html>
javiercito@ubuntu:~/javascript-dom_manipulation$ 
Repo:

GitHub repository: holbertonschool-higher_level_programming
Directory: javascript-dom_manipulation
File: 1-script.js
0/5 pts
2. Add `.red` class
mandatory
Write a JavaScript script that adds the class red to the header element when the user clicks on the tag with id red_header

Please test with this HTML file in your browser:

javiercito@ubuntu:~/javascript-dom_manipulation$ cat 2-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <style>
      .red {
        color: #FF0000;
      }
    </style>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <div id="red_header">Red header</div>
    <footer>
      Holberton School - 2022
    </footer>
    <script type="text/javascript" src="2-script.js"></script>
  </body>
</html>
javiercito@ubuntu:~/javascript-dom_manipulation$
Repo:

GitHub repository: holbertonschool-higher_level_programming
Directory: javascript-dom_manipulation
File: 2-script.js
0/5 pts
3. Toggle classes
mandatory
Write a JavaScript script that toggles the class of the header element when the user clicks on the tag id toggle_header:

The header element must always have one class: red or green, never both in the same time and never empty. If the current class is red, when the user click on id toggle_header element, the class must be updated to green ; and the reverse.

Please test with this HTML file in your browser:

javiercito@ubuntu:~/javascript-dom_manipulation$ cat 3-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <style>
      .red {
        color: #FF0000;
      }
      .green {
        color: #00FF00;
      }
    </style>
  </head>
  <body>
    <header class="green"> 
      First HTML page
    </header>
    <div id="toggle_header">Toggle header</div>
    <footer>
      Holberton School - 2022
    </footer>
    <script type="text/javascript" src="3-script.js"></script>
  </body>
</html>
javiercito@ubuntu:~/javascript-dom_manipulation$ 
Repo:

GitHub repository: holbertonschool-higher_level_programming
Directory: javascript-dom_manipulation
File: 3-script.js
0/5 pts
4. List of elements
mandatory
Write a JavaScript script that adds a li element to a list when the user clicks on the element with id add_item:

The new element must be: <li>Item</li> The new element must be added to the ul element with class my_list

Please test with this HTML file in your browser:

javiercito@ubuntu:~/javascript-dom_manipulation$ cat 4-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <br />
    <div id="add_item">Add item</div>
    <br />
    <ul class="my_list">
      <li>Item</li>
    </ul>
    <footer>
      Holberton School - 2022
    </footer>
    <script type="text/javascript" src="4-script.js"></script>
  </body>
</html>
javiercito@ubuntu:~/javascript-dom_manipulation$ 
Repo:

GitHub repository: holbertonschool-higher_level_programming
Directory: javascript-dom_manipulation
File: 4-script.js
0/5 pts
5. Change the text
mandatory
Write a JavaScript script that updates the text of the header element to New Header!!! when the user clicks on the element with id update_header

Please test with this HTML file in your browser:

javiercito@ubuntu:~/javascript-dom_manipulation$ cat 5-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <br />
    <div id="update_header">Update the header</div>
    <br />
    <footer>
      Holberton School - 2022
    </footer>
    <script type="text/javascript" src="5-script.js"></script>
  </body>
</html>
javiercito@ubuntu:~/javascript-dom_manipulation$ 
Repo:

GitHub repository: holbertonschool-higher_level_programming
Directory: javascript-dom_manipulation
File: 5-script.js
0/5 pts
6. Star wars character
mandatory
Write a JavaScript script that fetches the character name from this URL: https://swapi-api.hbtn.io/api/people/5/?format=json

The name must be displayed in the HTML tag with id character.
You must use the Fetch API.
You probably should read something about usign Promises later.
Please test with this HTML file in your browser:

javiercito@ubuntu:~/javascript-dom_manipulation$ cat 6-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header> 
      Star Wars character
    </header>
    <br />
    <div id="character"></div>
    <br />
    <footer>
      Holberton School - 2022
    </footer>
    <script type="text/javascript" src="6-script.js"></script>
  </body>
</html>
javiercito@ubuntu:~/javascript-dom_manipulation$ 
Repo:

GitHub repository: holbertonschool-higher_level_programming
Directory: javascript-dom_manipulation
File: 6-script.js
0/5 pts
7. Star Wars movies
mandatory
Write a JavaScript script that fetches and lists the title for all movies by using this URL: https://swapi-api.hbtn.io/api/films/?format=json

All movie titles must be list in the HTML ul element with id list_movies
You must use the Fetch API.
Please test with this HTML file in your browser:

javiercito@ubuntu:~/javascript-dom_manipulation$ cat 7-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header> 
      Star Wars movies
    </header>
    <br />
    <ul id="list_movies">
    </ul>
    <br />
    <footer>
      Holberton School - 2022
    </footer>
    <script type="text/javascript" src="7-script.js"></script>
  </body>
</html>
javiercito@ubuntu:~/javascript-dom_manipulation$ 
Repo:

GitHub repository: holbertonschool-higher_level_programming
Directory: javascript-dom_manipulation
File: 7-script.js
0/5 pts
8. Say Hello!
mandatory
Write a JavaScript script that fetches from https://hellosalut.stefanbohacek.dev/?lang=fr and displays the value of hello from that fetch in the HTML element with id hello.

The translation of “hello” must be displayed in the HTML element with id hello
Your script must work when it is imported from the <head> tag
Please test with this HTML file in your browser:

javiercito@ubuntu:~/javascript-dom_manipulation$ cat 8-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script type="text/javascript" src="8-script.js"></script>
  </head>
  <body>
    <header> 
      Say Hello!
    </header>
    <br />
    <div id="hello"></div>
    <br />
    <footer>
      Holberton School - 2022
    </footer>
  </body>
</html>
javiercito@ubuntu:~/javascript-dom_manipulation$ 
Repo:

GitHub repository: holbertonschool-higher_level_programming
Directory: javascript-dom_manipulation
File: 8-script.js
0/5 pts
9. List, add, remove
#advanced
Write a JavaScript script that adds, removes and clears li elements from a list when the user clicks:

The new element must be: <li>Item</li>
The new element must be added to the element with id my_list
When the user clicks on the element with id add_item: a new element is added to the list
When the user clicks on the element with id remove_item: the last element is removed from the list
When the user clicks on the element with id clear_list: all elements of the list are removed You script must work when it imported from the head tag Please test with this HTML file in your browser:
javiercito@ubuntu:~/javascript-dom_manipulation$ cat 100-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script type="text/javascript" src="100-script.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <br />
    <div id="add_item">Add item</div>
    <div id="remove_item">Remove item</div>
    <div id="clear_list">Clear list</div>
    <br />
    <ul class="my_list">
      <li>Item</li>
    </ul>
    <footer>
      Holberton School - 2022
    </footer>
  </body>
</html>
javiercito@ubuntu:~/javascript-dom_manipulation$ 
Repo:

GitHub repository: holbertonschool-higher_level_programming
Directory: javascript-dom_manipulation
File: 100-script.js
0/10 pts
10. Say hello to everybody!
#advanced
Write a JavaScript script that fetches and prints how to say “Hello” depending on the language

You should use this API service: https://hellosalut.stefanbohacek.dev/
The language code will be the value selected in the combo box with id language_code (es, fr, en etc.)
The translation must be fetched when the user clicks on element with id btn_translate
The translation of “Hello” must be displayed in the HTML tag with id hello
You script must work when imported from the <head> tag
Please test with this HTML file in your browser:

javiercito@ubuntu:~/javascript-dom_manipulation$ cat 101-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script type="text/javascript" src="101-script.js"></script>
  </head>
  <body>
    <header> 
      Say Hello
    </header>
    <br />
    <label for="language_code">Language code:</label>
    <select name="language" id="language_code">
        <option value="">--Please choose an option--</option>
        <option value="en">English</option>
        <option value="es">Spanish</option>
        <option value="fr">French</option>
    </select>
    <input id="btn_translate" type="button" value="Translate"/>
    <br />
    <div id="hello"></div>
    <br />
    <footer>
      Holberton School - 2022
    </footer>
  </body>
</html>
javiercito@ubuntu:~/javascript-dom_manipulation$ 
Repo:

GitHub repository: holbertonschool-higher_level_programming
Directory: javascript-dom_manipulation
File: 101-script.js
0/10 pts
Score
Project badge
Now that you are ready to be reviewed, share your link to your peers. You can find some here.

	
Don't forget to review one of them.

Next project: HBnB Evolution: Part 3 (Client)


