<h1 align="center">Scaletutor 1.0 Beta</h1>

[View the live project here](https://ericpp3.herokuapp.com/)

ScaleTutor is a command line learning tool for learning and/or testing your knowledge of musical scales a.k.a. modes. 
Perfect for musicians or anyone interested in music theory.

Take the opportunity to learn new scales, how they sound and how to use them.

Good luck and have fun!

ScaleTutor is the first stage of a much larger application that will include all sorts of music theory with a UI that is graphically appealing.

## Index – Table of Contents
* [User Experience (UX)](#user-experience-ux) 
* [Features](#features)
* [Design](#design)
* [Technologies Used](#technologies-used)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)

## User Experience (UX)

### User stories. 
As a user I want to:
  - Learn more about scales/modes.
  - I want to be able to choose between a variety of scales.
  - I want to receive relevant information about any chosen scale.
  - I want to get relevant examples of songs using the scale so that I can hear what they sound like.
  - I want to be able to test my understanding of the chosen scale.
  - I want to be able to see my result, where I went wrong and what notes I missed if any.
  - I want to continue playing for as long as I want.
  - I want to be able to change scale after each round.
  - I want to be able to quit the application after each round.

## Features

### Existing Features

- ###  __Welcome__

    - After starting the app the user is greeted and given a short briefing about the intentions of the programme. The idea is to give the user a basic understanding of what the software can offer.
The user will then be asked to either start or quit the programme. 

    - The user must answer either with 'y' or 'n'. Capital or not has no effect on the programme but any other characters will cause the programme to ask the user to answer with a valid choice. Which are 'y' or 'n'. 

      ![welcome](readme_content/welcome.png)

- ###  __Name Entry__
    - The user is prompted to enter a name. The only criteria that need to be met is that the name entered is at least one character in length. No other criteria needed.
The name is used to display personalized messages.

      ![name](readme_content/enter_name.png)

- ###  __Scale Menu__

    - Here the users name is used to ask which scale the user want to learn more about or test their knowledge of.
    The user can choose from the seven most used scales/modes in Western music.
    After choosing a scale their choice is displayed.

      ![name](readme_content/choose_scale.png)

- ###  __Scale Information__
    - After choosing a scale the user is shown information about the chosen scale.
    This information includes basic information about the scale as well as examples of known compositions or songs using the scale and a structure pattern.
    
    ![Scale_info](readme_content/scale_info_challenge.png)

- ###  __Challenge__
    - After the users has had a chance to learn about the scale, a command line drawing of a piano will be printed and a challenge will be displayed. The challenge is to enter the notes of the chosen scale in a random key.
Now the user can calculate the correct answer using the piano graphic and the provided scale pattern.  
  
    - The user must use valid notes to answer, or they will be asked to re-enter the answer. 
    - The rules for validation are:
      - Has to be a valid note (C,D,E,F,G,A,B) and the valid sharps. Flats are not used as they are synonymous to the sharp of the previous whole note.
      - Input must be as many valid notes as the scale contains.
      - All notes must be separated by a comma.

    ![user_input](readme_content/enter_notes.png)

- ###  __Result__

    - After input passes through validation a result is displayed.
    The result includes:
      - All notes of the correct scale.
      - Correct notes.
      - Wrong notes.
      - Missing notes.
      - Feedback based on the result.

    ![result](readme_content/result.png)

- ###  __Run again__
    - Round one is now finished, and the user is asked if they would like to quit or go for another round. 
    If choosing to quit - The software will stop running.
    If choosing to go again they will go back to scale menu.

    ![result](readme_content/bye.png)

### __How these features support the User Stories__

  Here are the user stories again with information on how the criteria are met in the application.

### User stories. 
As a user I want to:
- Learn more about scales/modes
  - The application gives information about any chosen scale.
- I want to be able to choose between a variety of scales.
  - The application currently includes 7 scales/modes.
- I want to receive relevant information about the chosen scale.
  - The application includes relevant information about each scale, including a scale pattern.
- I want to get relevant examples of songs using the scale so that I can hear what they sound like.
  - After choosing a scale the user receives information as well as song examples.
- I want to be able to test my understanding of the chosen scale.
  - After giving the user information and song examples of the scales they are asked to enter each note of the chosen scale in a randomly selected key.
- I want to be able to see my result, where I went wrong and what notes I missed if any.
  - After entering a valid answer, the user is shown:
    - All notes of the chosen scale in the random key.
    - All correct notes.
    - All wrong notes.
    - All missing notes.
    - A message based on how many notes was correct.
- I want to continue playing for as long as I want.
  - After each round the user is asked to play again or quit.
- I want to be able to change scale to learn about after each round.
  - When starting a new round the user is again asked to choose scale.
- I want to be able to quit the application after each round.
  - After each round the user is asked to play again or quit.

### Features which could be implemented in the future

- __UI__

  Since this is a command line application the UI is not the best. Creating a visually appealing interface would make the application way more fun.

- __Add scales__
  Music is amazing and there is no shortage of scales. The application currently contains the seven most common scales in western music. But all kind of world scales could easily be added by updating the list of dictionaries of scales and create a txt file with valid information about the scale. All code will work regardless of how many scales are added and the length of the added scale.

- __Add other music theory categories__
  - Circle of fifths
  - Chord progressions

## Application flow and structure

-   ### Flow Chart
       ![Flowchart](readme_content/flowchart.png)
 
## Technologies Used

### Languages Used

-   Python

### Frameworks, Libraries & Programs Used
- PyCharm
- Gitpod
- Git
- Lucid Charts
- Heroku
- randint() from random

## Testing
  The testing of this app has been me trying my best to raise errors.
  The app has also been tested by Greta Lindgren without finding errors or bugs.
  
### Validator Testing
- Code passes through PEP8 with no issues.

### Known bugs
If the notes are entered with a blank after each comma it will raise a ValueError because the length does not match the scale length. 
Maybe not quite a bug since I designed to software to continue anyway but it does show the same error message as when too many notes are entered. This will be addressed for the next version.

## Deployment

The application was created using Code Institutes template for PP3 via Github and GitPod. Deployed via Heroku.

### Deployment via Heroku

Step 1: Prepping code

  - Remove all commented out code.
  - Remove unnecessary imports
  - Add a new line (\n) in each input. 
  - run command: pip3 freeze > requirements.txt (this command will print requirements to requirements.txt. If there are any.)
  
Step 2: Setup Heroku Account
  - Go to http://www.heroku.com
  - Follow the steps to set up an account
  - When the account is set up you will arrive at the Heroku dashboard.

Step 3: Create App
  - Click "Create New App"
  - Give your app a name 
  - Choose your region
  - Confirm by clicking "Create App

Step 4: Set Up App
  - Click "Settings"
  - If app requires sensitive information inside for example a creds.json file, this has to be provided in the "Config Vars" section. Copy the file content and paste it into the "value" section and enter CREDS in the "Key" section.
  In the "Buildpack" section, click "Add Buildpack". 
    - Add the Python buildpack and click "Save Changes
    - Add the node.js Buildpack and click "Save Changes"

Step 5: Deploy
  - On the top of the page, choose "Deploy" in the menu.
  - Select Github in "Deployment Method" section.
  - Confirm that you want to connect to Github by clicking "Connect to Github"
  - In the "Connect to Github" section you can now find your Github repositories. Find the one you want to deploy, click "search" and then click "Connect" on the correct repository.
Step 6: Manual or automatic Deployment?
  - If you wish Heroku to automatically re-build your app every time you do a push, simply choose automatic deploy.
  - If you wish to manualy control when a new version is deployed choose "manual"
Step 7: View Deployed App
  - After successfully building your app, you will see the app has been built successfully and can now click "view" to test your app.
  Make sure it works.
  You are now online! Congratulations!

## Credits 

### Content 
The scale info provided after scale choice is taken from:
  - https://www.classicfm.com/discover-music/latest/guide-to-musical-modes/
    
### Code 
Sources used for coding information:
  - Stack Overflow
  - W3 Schools
  - Programiz.com
  - learnpython.org

### Readme
  - The structure of this readme is inspired by Elaine Broche and her MS3 project "Event Scheduler"

### Acknowledgments
Thanks to my mentor Brian Macharia for helping me with product development, code structure and keeping my spirit up.
Thanks to Greta Lindgren for product testing
