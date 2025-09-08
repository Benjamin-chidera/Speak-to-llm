# Conversational AI with Speech Recognition and Text-to-Speech

This project is a Python-based conversational AI application that listens to user speech, processes it using a conversational AI model, and responds with synthesized speech. It integrates speech recognition, a conversational AI model, and text-to-speech synthesis.

## Features

- **Speech Recognition**: Converts spoken input into text using Google Speech Recognition.
- **Conversational AI**: Processes the text input and generates a response using a conversational AI model.
- **Text-to-Speech**: Converts the AI-generated response into speech and plays it back to the user.

## Requirements

- Python 3.11 or higher
- Required Python packages (install via `pip`):
  - `speechrecognition`
  - `langchain`
  - `gtts`
  - `playsound`

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

## Function Flow Diagram

```plaintext
+---------------------+
| listen_for_speech() |
+---------------------+
          |
          v
+---------------------+
|  chat_with_bot()    |
+---------------------+
          |
          v
+---------------------+
|      speak()        |
+---------------------+
          |
          v
+---------------------+
|   Main Loop         |
| (Exit on "stop")    |
+---------------------+
