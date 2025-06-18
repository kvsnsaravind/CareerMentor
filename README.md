# CareerMentor

CareerMentor is an AI-powered resume and interview assistant.

It analyzes resumes and generates tailored feedback or interview questions for a selected job role using the Llama 3 model via the Groq API.

---

## 🚀 Features

- **Resume Feedback:** Get AI-generated feedback for your resume based on your target job role.
- **Interview Questions:** Generate relevant interview questions for your resume and chosen role.
- **Easy-to-edit Prompt Templates:** Uses Markdown (`.md`) files for prompt customization.

---

## 🛠️ Technologies Used

- **Python 3**
- **[Streamlit](https://streamlit.io/):** For the web interface
- **[Groq Python SDK](https://pypi.org/project/groq/):** For Llama 3 model API calls
- **Markdown (`.md`) files:** For prompt templates

---

## ⚙️ Setup Instructions

1. **Clone the repository:**
    ```sh
    git clone https://github.com/kvsnsaravind/careermentor.git
    cd careermentor
    ```

2. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

3. **Set your Groq API key:**
    ```sh
    set GROQ_API_KEY=your-groq-api-key
    ```
    *(Use `export` instead of `set` on Mac/Linux)*

4. **Run the app:**
    ```sh
    streamlit run careermentor/app.py
    ```

---

## 📄 Summary

1. **User Input:**  
   The user uploads a resume and selects a job role in the Streamlit UI app.

2. **Task Selection:**  
   The app determines whether to provide resume feedback or generate interview questions.

3. **Controller Layer:**  
   The controller receives the request and calls the appropriate function in the model layer.

4. **Model Layer:**  
   - Loads a Markdown prompt template.
   - Fills in the template with the user’s resume and role.
   - Sends the prompt to the Llama 3 model via the Groq API.

5. **LLM Response:**  
   The model returns feedback or questions, which are displayed to the user.

User input → Controller → Model (prompt building) → LLM (Groq/Llama 3) → Response → Display

---

## 📂 Project Structure

```
careermentor/
│
├── app.py
├── controller/
│   └── controller.py
├── model/
│   └── model.py
├── context/
│   ├── resume_feedback.md
│   └── interview_qa.md
└── requirements.txt
```

---

## 📝 License

MIT License

---

## 🙏 Acknowledgements

- [Groq](https://groq.com/)
- [Streamlit](https://streamlit.io/)
