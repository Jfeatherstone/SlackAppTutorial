## Tutorial: Creating a Slack Anonymous App

Howdy!

![hat](https://raw.githubusercontent.com/Jfeatherstone/SlackAppTutorial/master/hat.png)

This is a tutorial on how to setup a basic app for a Slack workspace that will allow you to anonymously send messages. If you are interested in building a Slack app other than an anonymous messager, I'd still recommend you check out the tutorial, since you'll find that a lot of the code will be the same regarldess of the project.

I will assume that you have little to no prior knowledge of programming (a little bit of Python may be useful though), server hosting, or Slack apps in general. I have done my best to explain every topic as clearly and simply as possible, and it is my hope that anyone will be able to setup a similar app in less than a few hours with the help of this tutorial. If you're ready to jump right in, head over on over to the [wiki](https://github.com/Jfeatherstone/SlackAppTutorial/wiki), otherwise stick around for a brief overview of the tutorial.

If you're already familiar with Python/server hosting, feel free to just clone this repository and use the wiki as a reference.

If you have any questions/comments about the tutorial, you can submit an issue on the repository (if you know how to do that) or just send me an email (can be found on my Github profile page).

*This tutorial is very much a work in progress, and certain pages may be incomplete/non-existent. If you would like help with a step that isn't posted yet, feel free to email me and I'd be more than happy to help out!*

### Tutorial Outline

1. Overview of Concepts
    - We begin by discussing a bit of background information on how Slack apps work, what an HTTP request is, and how you would respond to one. There's no programming involved here, so if you're already familiar with this stuff, feel free to skim/skip it.
2. Creating a Slack App
    - Here we'll cover how to create an app from the Slack API side of things, and how to configure some of the properties that define how it looks to your users.
3. What is a "Platform as a Service"
    - In this section, I talk about what a "Platform as a Service" is, and describe two particular examples that I will explicitly cover in this tutorial: AWS and Heroku. From here on out, there will be two separate pages for the next few steps, one for each service.
4. Setting up Accounts
    - These two pages focus on how to set up the required accounts for each service, and a basic introduction to navigating the project dashboard.
5. Project Workflow
    - Here I describe how one would actually modify the code for either service, and how to setup your computer to do such things. At this point, one could feasibly just copy the code from the repository into the account created prior, and be done; I would recommend learning a bit of how the programs work though!
6. Basic Code Structure
    - This page describes how each of the services is set up, and what actually happens when one receives an HTTP request. This is the last of the split pages, and from here on out, the code will be the same for both.
7. Parsing and Authentication
    - Here I describe how one would parse the information from an HTTP request (since it gets encoded as it is sent) and how to make sure that the request you are receiving is one that you want to respond to.
8. Sending a Message
    - This is where we get into how to have the app actually send a message to the workspace.
9. Finishing Up
    - The final page, where I discuss some extensions of the program, as well as slightly more advanced concepts.
