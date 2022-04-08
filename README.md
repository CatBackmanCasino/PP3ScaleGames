<h1 align="center">Scaletutor 1.0 Beta</h1>

[View the live project here](https://ms3-event-scheduler.herokuapp.com/)

ScaleTutor is a command line learning tool for learning and/or testing your knowledge of musical scales a.k.a. modes.
Perfect for musicians or anyone interested in music theory.

The tool includes a variety of scales for the user to learn more about and after choosing a scale the user can learn more about the scale, including the scale structure. This can then be used to figure out wich notes are included in the scale in any key.

ScaleTrainer is the first of a range of games aimed to teach different parts of music theory.


## Index – Table of Contents
* [User Experience (UX)](#user-experience-ux) 
* [Features](#features)
* [Design](#design)
* [Technologies Used](#technologies-used)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)

## User Experience (UX)

-   ### User stories: as a user I want to:
  - Learn more about scales/modes
  - I want be able to choose between a variety of scales.
  - I want to recieve relevant information about chosen scales.
  - I want to get relevant examples of songs using the scale so that i can hear what they sound like.
  - I want to be able to test my understandinig of the chosen scale.
  - I want to be able to see my result, where i went wrong and what notes i missed if any
  - I want to continue playing for as long as i want
  - I want to be able to change scale to learn about after each round.
  - I want to be able to quit the application after each round.

## Features

### Existing Features

- ###  __Welcome__

    - After starting the app the user is greeted and given a short briefing about the intentions of the programme. The idea is to give the user a basic understanding of what the software can offer.
    The user will then be asked to either start or quit the programme. 

      ![Main Menu](documentation/images/f01-main-menu-1.png)

    - The user has to answer either with 'y' or 'n'. Capital or not has no effect on the programme but any other characters will cause the programme to ask the user to answer with a valid choice. Which are 'y' or 'n'. 

      ![Main Menu Message](documentation/images/f01-main-menu-2.png)

- ###  __Name Entry__
    - The user is prompted to enter a name. The only criteria that needs to be met is that the name entered is at least one character in length. No other criteria needed.
    The name is used to display personalized messages.

      ![Events Menu](documentation/images/f02-manage-events-submenu.png)

- ###  __Scale Menu__

    - Here the users name is used to ask which scale the user want to learn more about or test their knowledge of.
    The user can choose from the seven most used scales/modes in Western music.

    After choosing a scale their choice is displayed.

      ![Active Events](documentation/images/f03-show-active-events.png)

- ###  __Scale Information__
    - After choosing a scale the user is shown information about the chosen scale.
    This information includes basic information about the scale as well as examples of known compositions or songs using the scale and a structure pattern.
    
    ![Add Event](documentation/images/f04-add-event.png)

- ###  __Challenge__
    - After the users has had a chance to learn about the scale they will be given a random key, a command line drawing of a piano and a random key.
    The challenge is to test the users understanding of the scale by entering each note of the scale in the given key using the previously provided scale pattern as a guide.
    
    - The user can only use valid notes to answer or they will be asked to re-enter the answer. 
    - The rules for validation are:
      - Has to be a valid note (C,D,E,F,G,A,B) and the valid sharps. Flats are not used as they are synonymos to the sharp of the previous whole note.
      - Input has to be as many valid notes as the scale contains.
      - All notes has to be separated by a comma.

    ![Add Event](documentation/images/f04-add-event.png)

- ###  __Result__

    - After input passes through validation a result is displayed.
    The result includes:
      - All notes of the correct scale.
      - Correct notes.
      - Wrong notes.
      - Missing notes.
      - Feedback based on the result.

- ###  __Run again__
    - Round one is now finished and the user is asked if they would like to quit or go for another round. 
    If choosing to quit - The software will stop running.
    If choosing to go again they will go back to scale menu.

- ### __How these features support the User Stories__

  Here is the user stories again with added information on how the functions adress the user stories:
- #### __As a
  - Learn more about scales/modes
    - Addresse
  - I want be able to choose between a variety of scales.
  - I want to recieve relevant information about chosen scales.
  - I want to get relevant examples of songs using the scale so that i can hear what they sound like.
  - I want to be able to test my understandinig of the chosen scale.
  - I want to be able to see my result, where i went wrong and what notes i missed if any
  - I want to continue playing for as long as i want
  - I want to be able to change scale to learn about after each round.
  - I want to be able to quit the application after each round.

### Features which could be implemented in the future

- __Appropriate UI__

  As this application uses the command line interface it is not very user friendly for a human end-user.  An obvious future feature of this application would be to build a better user-interace layer using HTML/CSS and possibly Javascript to make it much more intuititve to use.

- __Extended Data Model__

  The data model representing the Events and Bookings is very simplistic in terms of the data elements it stores.  This could be extended to store additional data with more complex data relationship rules.  The data model and code could also be re-structured to use a better Object Oriented approach, where Events and Bookings could be handled as Object types with methods and attributes.

- __Extended Data Analysis__

  The Review Past Events feature of the application gives a breakdown of cancelled events vs events that weren't cancelled and shows % seats booked for those that went ahead.  Analysis of the data could be extended to find other information from the data, such as how frequently are certain events cancelled due to lack of bookings, which courses are most popular etc. and then this information could help the users plan ahead when trying to schedule events.  This type of information could also potentially be used to automate some tasks - e.g. automatically send an administrator an email highlighting a particular event has below a certain threshold of bookings coming up to it's scheduled date, so that the administrator has time to take action - e.g. send out a marketing email to draw attention to the event.

## Design

-   ### Flow Charts
    The diagrams below outline the high level flow of control within the application :

    <details>
       <summary>Diagrams</summary>
       ![Main Flowchart](documentation/flowcharts/ms3-main-flowchart.png)

    </details>

    
## Technologies Used

### Languages Used

-   [Python 3.8.10](https://www.python.org/)

### Frameworks, Libraries & Programs Used

## Testing

### Validator Testing

### Known bugs

## Deployment

### How to clone the GitHub repository

### How this site was deployed to Heroku 

## Credits 

### Content 
    
### Code 

### Acknowledgments

- 