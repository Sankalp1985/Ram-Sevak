<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Q&A App (Online)</title>
  <style>
    body { font-family: Arial, sans-serif; padding: 20px; }
    .question { border: 1px solid #ccc; border-radius: 8px; padding: 15px; margin-bottom: 15px; }
    .answer { margin-left: 10px; margin-top: 5px; color: #444; }
    input[type="text"] { padding: 6px; margin-top: 8px; margin-bottom: 10px; width: 80%; }
    button { padding: 6px 10px; margin-left: 5px; }
  </style>

  <!-- Firebase -->
  <script src="https://www.gstatic.com/firebasejs/10.11.0/firebase-app.js"></script>
  <script src="https://www.gstatic.com/firebasejs/10.11.0/firebase-database.js"></script>
  <script>
    const firebaseConfig = {
      apiKey: "AIzaSyDBiMpeDoAe-paKbP8UA_VVYwQYueBNSRE",
      authDomain: "qa-app-b0e16.firebaseapp.com",
      databaseURL: "https://qa-app-b0e16-default-rtdb.firebaseio.com",
      projectId: "qa-app-b0e16",
      storageBucket: "qa-app-b0e16.appspot.com",
      messagingSenderId: "402612297087",
      appId: "1:402612297087:web:ad3b5c4137a751e217f1d6"
    };
    const app = firebase.initializeApp(firebaseConfig);
    const db = firebase.database();
  </script>
</head>
<body>
  <h1>Ask a Question</h1>
  <input type="text" id="questionInput" placeholder="Type your question here" />
  <button onclick="submitQuestion()">Submit</button>

  <h2>Questions</h2>
  <div id="questionList"></div>

  <script>
    document.addEventListener('DOMContentLoaded', loadQuestions);

    function submitQuestion() {
      const questionInput = document.getElementById('questionInput');
      const questionText = questionInput.value.trim();
      if (questionText === '') return;

      const newQuestion = { question: questionText, answers: [] };

      const questionRef = db.ref('questions').push();
      questionRef.set(newQuestion);

      // Add to localStorage for reference
      let questions = JSON.parse(localStorage.getItem('questions')) || [];
      questions.push({ ...newQuestion, id: questionRef.key });
      localStorage.setItem('questions', JSON.stringify(questions));

      addQuestionToPage(newQuestion, questions.length - 1, questionRef.key);
      questionInput.value = '';
    }

    function submitAnswer(button, index) {
      const answerInput = button.previousElementSibling;
      const answerText = answerInput.value.trim();
      if (answerText === '') return;

      let questions = JSON.parse(localStorage.getItem('questions')) || [];
      const questionId = questions[index].id;
      if (!questionId) return;

      const answersRef = db.ref(`questions/${questionId}/answers`);
      answersRef.once('value', snapshot => {
        const currentAnswers = snapshot.val() || [];
        currentAnswers.push(answerText);
        answersRef.set(currentAnswers);
      });

      questions[index].answers.push(answerText);
      localStorage.setItem('questions', JSON.stringify(questions));

      addAnswerToPage(button.parentElement, answerText);
      answerInput.value = '';
    }

    function addQuestionToPage(qObj, index, id = null) {
      const questionList = document.getElementById('questionList');

      const questionDiv = document.createElement('div');
      questionDiv.className = 'question';

      questionDiv.innerHTML = `
        <p><strong>Q:</strong> ${qObj.question}</p>
        <input type="text" placeholder="Your answer" />
        <button onclick="submitAnswer(this, ${index})">Answer</button>
      `;

      (qObj.answers || []).forEach(answer => {
        addAnswerToPage(questionDiv, answer);
      });

      questionList.appendChild(questionDiv);
    }

    function addAnswerToPage(questionDiv, answerText) {
      const answerPara = document.createElement('div');
      answerPara.className = 'answer';
      answerPara.innerHTML = `<strong>A:</strong> ${answerText}`;
      questionDiv.appendChild(answerPara);
    }

    function loadQuestions() {
      db.ref('questions').once('value', snapshot => {
        const data = snapshot.val() || {};
        const questions = [];

        for (let id in data) {
          const q = data[id];
          questions.push({ ...q, id });
        }

        localStorage.setItem('questions', JSON.stringify(questions));

        const questionList = document.getElementById('questionList');
        questionList.innerHTML = '';
        questions.forEach((qObj, index) => {
          addQuestionToPage(qObj, index, qObj.id);
        });
      });
    }
  </script>
</body>
</html>
