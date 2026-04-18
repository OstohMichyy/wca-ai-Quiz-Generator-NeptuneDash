#  Quiz Generator

##  Project Description

The **Quiz Generator** is a Python-based application that automatically creates multiple-choice quiz questions using AI. It allows users to input either a **topic** or a **paragraph**, and then generates a set of quiz questions based on that input.

This project is designed to help students study, test their knowledge, and make learning more interactive.

---

## How the System Works

### 1. User Input

When the program starts (`main.py`), the user is prompted to choose:

* Generate quiz from a **topic**
* Generate quiz from a **paragraph**

The user then provides:

* The topic name OR the paragraph text
* Number of questions (e.g., 5)
* Difficulty level (`easy`, `medium`, `hard`)

---

### 2. Sending Data to AI

The input is sent to an AI model via an API (such as OpenAI or Gemini).
The program constructs a prompt instructing the AI to:

* Create multiple-choice questions
* Provide 4 answer options per question
* Indicate the correct answer clearly

---

### 3. Question Generation

The AI processes the request and generates quiz content based on:

* Key concepts from the topic
* Important details from the paragraph

Each question follows this format:

```
Question
A. Option 1
B. Option 2
C. Option 3
D. Option 4
Answer: Correct option
```

---

### 4. Output Display

The generated quiz is displayed directly in the terminal.
This allows the user to:

* Read the questions
* Test themselves manually

---

##  Project Structure

```
quiz_generator/
│
├── main.py              # Runs the program and handles user input
├── ai_generator.py      # Handles API requests and AI interaction

```

---

##  How to Run the Project

### 1. Install Python

Make sure Python 3.10 or higher is installed.

### 2. Install Dependencies

```
pip install -r requirements.txt
```

### 3. Add API Key

Open `ai_generator.py` and insert your API key:

```python
api_key = "your_api_key_here"
```

### 4. Run the Program

```
python main.py
```

---

##  Features

* Generate quizzes from a **topic**
* Generate quizzes from a **paragraph**
* Multiple-choice questions (MCQs)
* Custom number of questions
* Difficulty selection

---

##  Future Improvements

* Add a graphical user interface (GUI)
* Save quizzes as PDF or text files
* Add automatic scoring system
* Support more question types (true/false, fill-in-the-blank)

---

##  Example Use Case

A student pastes a paragraph from their notes, and the system instantly generates 5 quiz questions to help them revise.

---

##  Author

This project was built as a beginner-friendly introduction to working with APIs and AI in Python.

---

##  Notes

* Requires an internet connection
* API usage may cost money depending on the provider

---

**Build, learn, and improve your Quiz Generator! **
