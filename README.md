# CAPSTONE - QUIZMAKER
## CS50W Final Project

**Quizmaker is a web app allowing users to build their own quizzes, take public quizzes themselves and compare the scores.**


### Description
-----------

The app is a final part of [HarvardX CS50W: Web Programming with Python and JavaScript](https://cs50.harvard.edu/web/2020/). It was built using plain JavaScript on the front-end and Django on the back-end, saving all necessary data in a SQLite database. It also makes use of Bootstrap's CSS on the frontend. Apart from the login and register page, it is written as a single page application.


### Task and requirements
-----------

*In this project, you are asked to build a web application of your own. The nature of the application is up to you, subject to a few requirements:*

* *Your web application must be sufficiently distinct from the other projects in this course and more complex than those.*
* *Your web application must utilize Django (including at least one model) on the back-end and JavaScript on the front-end.*
* *Your web application must be mobile-responsive.*

*Beyond these requirements, the design, look, and feel of the website are up to you!*

**The following description was written according to further CW50w README.md requirements.**


### Deployment
-----------

* Download the code and go to project directory.
* Install Python 3.x.
* Run `pip install -r requirements.txt` to install dependencies. 
* Generate your Django secret key and hide it in you .env file. There is an .env.example file in this repo as an example.
* In the project directory run `python manage.py makemigrations quizmaker` to make migrations.
* Run `python manage.py migrate` to apply migrations to your database.
* Run `python manage.py runserver`, open it in your browser of choice and register an account.


### Files
-----------

* `capstone` project directory
    * `urls.py` - path reference to the app URLs
    * default django project files, such as: `settings.py`, `wsgi.py`, `asgi.py` etc.
* `quizmaker` - app directory
    * `static` - directory containing the JavaScript and CSS files inside the app directory within
        * `quizmaker.js` - JavaScript file containing all frontend dynamic functionality, including displaying different views, quiz and question forms, gathering and sending information, displaying quiz questions while taking it etc.
        * `style.css` - additional CSS to the Bootstrap library, e.g. classes for right and wrong answers as well as for quiz main colors
    * `templates` - directory containing the HTML templates inside the app directory within
        * `layout.html` - HTML template for all other HTML files, containing navigation bar and links to CSS and JS files
        * `register.html` - register form
        * `login.html` - login form
        * `index.html` - main HTML page containing mostly empty sections for different views and the forms for adding quizzes and questions
    * `admin.py` - registration of app models for the default django admin page
    * `apps.py` - app configuration codeAfterward, users can add questions selecting one from three types: type answer, multiple choice and true or false. Then the question form with corresponding fields is displayed. Users can also edit and remove quizzes as well as edit and remove questions. When users click on a quiz card *edit* button, they are taken to the quiz dashboard, where all these features are available.

    * `models.py` - user, quiz, question and score models definition
    * `test.py` - place for app testsAfterward, users can add questions selecting one from three types: type answer, multiple choice and true or false. TAfterward, users can add questions selecting one from three types: type answer, multiple choice and true or false. Then the question form with corresponding fields is displayed. Users can also edit and remove quizzes as well as edit and remove questions. When users click on a quiz card *edit* button, they are taken to the quiz dashboard, where all these features are available.
hen the question form with corresponding fields is displayed. Users can also edit and remove quizzes as well as edit and remove questions. When users click on a quiz card *edit* button, they are taken to the quiz dashboard, where all these features are available.

    * `urls.py` - all app URLs referenced in the project `urls.py` file
    * `views.py` - all backend functions that defined URLs point to, which render HTTP responses on HTML templates and send JSON responses to the frontend
* `manage.py` - default django file
* `README.md` - this readme file


### Features
-----------

* Register and login, based on previous projects.
* Make a new quiz.
* Edit the title, description or visibility of your quiz.
* Add questions to your quiz from three possible types: type answer, multiple choice and true or false.
* Edit or remove questions.
* See all public quizzes on the main page and all your quizzes on your profile page.
* Take quizzes from other users.
* Check top scores: yours, from all users or specific quiz.
* Possible further future features may include: 
    * More types of questions.
    * Possibility to rate quizzes.
    * Quiz timer.

    
### Preview video
-----------

Video of a project demo is uploaded [here](https://www.youtube.com/watch?v=oRS3sPpaRCE).


### Distinctiveness and Complexity
-----------

The quizmaker app uses the knowledge gathered in the previous projects, such as *commerce*, *mail* and *network*, and tries to push it a little bit further. Instead of letting the user add a simple listing or a post, it gives them a possibility to choose the type of content they want to create, for example the number of questions in their quiz or the type of question they want to appear there. This feature makes both the necessary forms and the data to store in the database more diverse and complex than in the previous project sets. 

On the start page, users are asked to register and log in. Then the main quiz page appears, which shows responsive quiz cards of all public quizzes with at least one question or a corresponding message if there are none yet. When users clicks on their username, they are sent to their profile page containing all their private and public quizzes. At the bottom of each quiz card there is a button - *edit* if the user is the author of the quiz and *take* if someone else is the author.

Users are invited to make their own quizzes, where they specify the title, description and if the quiz should be public or private. After that, the quiz is saved in the database and receives its own theme color from the app color palette. 

Afterward, users can add questions selecting one from three types: type answer, multiple choice and true or false. Then the question form with corresponding fields is displayed. Users can also edit and remove quizzes as well as edit and remove questions. When users click on a quiz card *edit* button, they are taken to the quiz dashboard, where all these features are available.

When users decide to take someone else's quiz, they are taken to the quiz start view and are shown all questions one at a time. The question display depends on a question type. When they type and check the answer or choose an answer from the displayed buttons, they right answer is highlighted green and their answer, if wrong, red. After that, they are shown the next button to move further in the quiz.

After taking the quiz, users are invited to see the top scores, limited to ten best records. There they can choose to display their own scores, all scores or top scores for a specific quiz.