---
layout: page
title: About
permalink: /about/
---

# About Armaghan Zarak 😎   

## About Me

- I love to play sports such as Basketball, Soccer, and American football.
- I love to travel and visit new and beautiful places around the world. Below, I have inserted an image of my recent travels to Cappadocia in Turkey:

  <img src="/Armaghan_2025/assets/images/Picture1.jpeg" alt="Hot air balloons littering the Sunrise" width="400px" height="500px"/>

## Goals for this year

- Some goals I have for this school year are to be able to code well enough to create my own website and to know the basics of how to code.

## Previous Experience

- I have taken a 2-day course outside of school. But other than this, I have no other experience in coding.

## Interests

- I love to learn about geography and play sports with friends.
- When I actually have time, I love to play video games with friends.

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Country Quiz</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #2c3e50; /* Darker background */
            color: #ecf0f1; /* Lighter text color */
            text-align: center;
            padding: 20px;
        }
        .quiz-container {
            max-width: 600px;
            margin: auto;
            background-color: #34495e; /* Slightly lighter background for the quiz container */
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        .question {
            font-size: 18px;
            margin-bottom: 15px;
        }
        .answers button {
            display: block;
            width: 100%;
            margin: 5px 0;
            padding: 10px;
            font-size: 16px;
            border-radius: 5px;
            border: 1px solid #7f8c8d;
            background-color: #1abc9c; /* Button color */
            color: #fff; /* White text color for buttons */
            cursor: pointer;
            transition: background-color 0.3s, transform 0.3s; /* Added transition for animation */
        }
        .answers button:hover {
            background-color: #16a085; /* Darker shade on hover */
        }
        .correct {
            background-color: #2ecc71 !important; /* Green color for correct answers */
            transform: scale(1.05); /* Slightly increase the size */
        }
        .wrong {
            background-color: #e74c3c !important; /* Red color for wrong answers */
            transform: scale(0.95); /* Slightly decrease the size */
        }
        .result {
            font-size: 20px;
            margin-top: 20px;
        }
    </style>
</head>
<body>

<div class="quiz-container">
    <h2>Country Quiz</h2>
    <div id="quiz">
        <div class="question" id="question"></div>
        <div class="answers" id="answers"></div>
        <div class="result" id="result"></div>
    </div>
</div>

<script>
    const quizData = [
        {
            question: "Where is France located?",
            options: ["Europe", "Asia", "Africa", "South America"],
            answer: "Europe"
        },
        {
            question: "Which continent is Australia part of?",
            options: ["Asia", "Europe", "Oceania", "North America"],
            answer: "Oceania"
        },
        {
            question: "Where is Brazil located?",
            options: ["South America", "North America", "Europe", "Africa"],
            answer: "South America"
        },
        {
            question: "Which continent is Egypt part of?",
            options: ["Asia", "Africa", "Europe", "South America"],
            answer: "Africa"
        },
        {
            question: "Where is Japan located?",
            options: ["Europe", "Asia", "Oceania", "South America"],
            answer: "Asia"
        }
    ];

    let currentQuestion = 0;
    let score = 0;

    function loadQuestion() {
        if (currentQuestion < quizData.length) {
            const questionData = quizData[currentQuestion];
            document.getElementById("question").innerText = questionData.question;
            const answersContainer = document.getElementById("answers");
            answersContainer.innerHTML = "";
            questionData.options.forEach(option => {
                const button = document.createElement("button");
                button.innerText = option;
                button.onclick = () => selectAnswer(button, option);
                answersContainer.appendChild(button);
            });
        } else {
            showResult();
        }
    }

    function selectAnswer(button, selectedOption) {
        const questionData = quizData[currentQuestion];
        if (selectedOption === questionData.answer) {
            button.classList.add("correct");
            score++;
        } else {
            button.classList.add("wrong");
        }

        // Disable all buttons after an answer is selected
        const buttons = document.querySelectorAll(".answers button");
        buttons.forEach(btn => btn.disabled = true);

        // Proceed to the next question after a short delay
        setTimeout(() => {
            currentQuestion++;
            loadQuestion();
        }, 1000); // 1 second delay to show the color change
    }

    function showResult() {
        document.getElementById("quiz").innerHTML = `
            <div class="result">
                You got ${score} out of ${quizData.length} correct!
            </div>
        `;
    }

    loadQuestion();
</script>

</body>
</html>







<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Interactive Button</title>
    <style>
        .button {
            display: inline-block;
            padding: 10px 20px;
            font-size: 16px;
            color: white;
            background-color: #007bff;
            border: none;
            border-radius: 5px;
            text-decoration: none;
            text-align: center;
            cursor: pointer;
        }
        .button:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <a href="https://espn.com/nfl/player/_/id/3116406/tyreek-hill" class="button" target="_blank">
        Tyreek Hill
    </a>
</body>
</html>