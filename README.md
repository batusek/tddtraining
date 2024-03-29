# Test-driven development training

This repository is an add on to the one day [Test-Driven Development training](https://batusek.cz/en/domu-cestina/trainings/test-driven-development/)

# Instructions

## Prerequisites

- Install Docker
- Install a git client
- Install Visual Studio Code
- Install Remote-Containers extension

## Steps

- Checkout repo `git clone https://github.com/batusek/tddtraining.git`
- Start Visual Studio Code
- Command Palette (F1): Select **Remote-Containers: Open Folder in Container...** and Select folder where you cloned the git repo

### Python
- Command Palette (F1): **Python: Run All Tests** or go to Test Explorer and click on the green arrow icon
The only existing test in `exercise1/leapyeartest.py` should fail

### .Net
- `cd exercise1`
- Type "dotnet test" in terminal
The only existing test in `exercise1/LeapYearTest.cs` should fail

### vuejs
- `cd exercise1`
- Type "npm install" in terminal.
- Type "npm test" in terminal. Alternatively, press Ctrl+F5 to start watching changes.
The only existing test in `exercise1/leapyear.test.ts` should fail


# Exercises

## Exercise 1 - Embrace the tooling
The first exercise is trivial from the programming point of view and its main purpose is to get acquainted with the tooling.
To finish it it should be enough to write 4 tests and appropriate code inside one function. Please write the production code one test at a time!

Instructions: [Leap year](http://codingdojo.org/kata/LeapYears/)

## Exercise 2 - Practice baby steps
Try to do as many Red-Green-Refactor cycles as you can. One cycle should not take more than a couple of minutes.

Instructions: [Numbers in words](http://codingdojo.org/kata/NumbersInWords/)

## Exercise 3 - Grow my code
Start from scratch and grow your code with Red-Green-Refactor cycles. This exercise is a bit longer than the previous one. You probably start with only Red-Green for the first few tests. Over time you will observe that you added -Refactor to your flow - you code will call for it.

Instructions: [IPv6 address validator](https://www.codewars.com/kata/54fa4e210609868fce0002bf)

## Exercise 4 - Getting rid of dependencies
An existing code that calls some infrastructure code inside is available including an integration test. Rewrite the code 3 times using various techniques for getting rid of dependencies and using tiny and safe refactorings before you write more focused tests. The three methods:
- Use mocks/stubs
- Use a virtual method and subclassing
- Make dependency explicit


# TODO
## Exercise X - Refactor and existing class/method
E.g. http://codingdojo.org/kata/GildedRose/


## Exercise X Get rid of dependency alternative
E.g. https://github.com/sandromancuso/trip-service-kata or HTML formatter

