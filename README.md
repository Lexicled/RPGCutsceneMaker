# RPG Cutscene Editor

## What is this?

This is a tool I'm working on designed to speed up RPG development - specifically cutscenes. It is designed to take *your* code and *your* current systems, and use them to create cutscenes that you can edit visually, making iteration over designs faster and cutscenes far easier to create. Right now, I am working on making it specifically for GameMaker, but I plan on expanding it to other 2D engines like Godot, RPGMaker and Unity once a full, working version is complete.

## Why is this?

I was inspired to make this because I saw a clip from PirateSoftware (aka Thor) discussing how cutscene development majorly slows down gamedev as nothing there is reusable - so I wanted to make something that you can setup once for your project, and then make most of the simple cutscenes for your game with relative ease, and export them straight to code you can paste in the editor.

## Current Status

Right now, I have started planning the project and created this README. Below is a list here of the features that need to be added until I'm happy to make a full release - both to help me keep track of things, help anyone who is waiting for the release have an idea of how long it will be and to give anyone who wants to contribute some ideas of what to do.

**Todo List:**

*Changes coming very soon:*

- Add requirements functionality to Timeline class
- Finish unit tests for Command class
- Add command subclasses (will elaborate more once I start work on them)
- Add GameMaker import functionality (will elaborate more once I start work on it)
- Build UI (will elaborate more once I start work on it)

*Changes coming in the further future:*

- Branching timeline
- Python modding framework

## How to Contribute

There are a few ways to contribute. One is just to give me ideas - if there's a feature you think would be neat, however small, let me know - if I think it's feasible and worth the time it takes to implement, I'll add it to the list above! You can do so by adding an issue with the "enhancement" label. You can also fix any typos, syntax, logical or graphical errors me or any other contributers make - it'll help me focus more on adding larger features than bugtesting (or, failing that, add it as an issue with the "typo" tag)! You can also test it on different operating systems - I'll be developing and testing mostly on Linux, and testing on Windows 10 every once in a while. If you have any other operating systems, feel free to test and report any bugs you find - it'll save me a lot of time and improve the tool for anyone else on your OS! And lastly - you can of course contribute by helping fix bugs or add features! To fix typos and bugs or add features yourself, you'll need to make a pull request - if you don't know how, you should probably learn before trying to contribute in this way - but if you do, then great, just follow the guidelines in the section below!

## Pull Request Guidelines

Note - don't contribute right now. I haven't written any code, or put any features on the todo list. This should be pretty obvious, but I'll put it here just in case - I'll remove this bit once the project is ready!

I'm not very experienced with Git or Github - I mainly use it for personal version control - so please try your best to make my job easy! You can do that by tring your best to do the following:
- 1 fix/feature per PR - don't group features/fixes, I'll decline your PR if you do - keep them focused on one feature - fair enough if you need to fix something to get your feature to work, but even so, try to keep them seperate!
- Be concise in your title and description - Be clear about what you're changing, and (if relevant) why. Reference any issues that you are acting on if you are working on one of those!
- Match the style I'll be using - I'll probably still merge the PR if you do this, but then I'll have to fix all the formatting, and it'll waste my time. Also, try to write comments where necessary so everyone knows what's going on - nothing excessive, just enough for people to understand what you're trying to do!
- Include or update tests where necessary.
- Remove any debug code (or at least comment it out) before submitting.

That's basically all, just use common sense and try not to make me suffer - thanks!