const chatBox = document.getElementById('chat-box');
const form = document.getElementById('question-form');
const robot = document.getElementById('robot');
const startBtn = document.getElementById('start-btn');

// Define initial greeting message
const greetingMessage = "Hello Visitor, I'm your Energy Efficiency Assistant! Let's upgrade your house's performance together. Click 'Start Diagnostics Analyst' to begin.";

// Display initial greeting message
displayMessage(greetingMessage, 'bot');

// Add event listener for the "Start Diagnostics" button
startBtn.addEventListener('click', startDiagnostics);

const questions = [
  {
      question: 'How many rooms do you have in your house?',
      inputType: 'number',
      name: 'rooms',
      min: 1,
      max: 10
  },
  {
      question: 'Do you use incandescent bulbs?',
      inputType: 'checkbox',
      name: 'incandescent'
  },
  {
      question: 'How would you rate your insulation?',
      inputType: 'select',
      name: 'insulation',
      options: [
          { value: '', text: 'Select' },
          { value: 'poor', text: 'Poor' },
          { value: 'average', text: 'Average' },
          { value: 'good', text: 'Good' }
      ]
  },
  {
      question: 'How efficient are your appliances?',
      inputType: 'select',
      name: 'appliances',
      options: [
          { value: '', text: 'Select' },
          { value: 'low', text: 'Low Efficiency' },
          { value: 'average', text: 'Average Efficiency' },
          { value: 'high', text: 'High Efficiency' }
      ]
  },
  {
      question: 'What type of windows do you have?',
      inputType: 'radio',
      name: 'windows',
      options: [
          { value: 'single', text: 'Single Pane' },
          { value: 'double', text: 'Double Pane' }
      ]
  },
  {
      question: 'Is your HVAC system old?',
      inputType: 'checkbox',
      name: 'old_hvac'
  },
  {
      question: 'Is renewable energy integration feasible for your house?',
      inputType: 'checkbox',
      name: 'renewable'
  },
  {
      question: 'Is a smart home system feasible for your house?',
      inputType: 'checkbox',
      name: 'smart_home'
  },
  {
      question: 'Is regular maintenance needed?',
      inputType: 'checkbox',
      name: 'maintenance'
  },
  {
      question: 'Do you have any unoccupied rooms?',
      inputType: 'checkbox',
      name: 'unoccupied'
  }
];

let currentQuestionIndex = 0;

function startDiagnostics() {
    // Clear initial message and form
    chatBox.innerHTML = '';
    form.innerHTML = '';

    // Display first question
    displayNextQuestion();
}

function displayNextQuestion() {
    const currentQuestion = questions[currentQuestionIndex];
    displayMessage(currentQuestion.question, 'bot');

    switch (currentQuestion.inputType) {
        case 'number':
            displayNumberInput(currentQuestion);
            break;
        case 'checkbox':
            displayCheckboxInput(currentQuestion);
            break;
        case 'select':
            displaySelectInput(currentQuestion);
            break;
        case 'radio':
            displayRadioInput(currentQuestion);
            break;
        default:
            break;
    }

    currentQuestionIndex++;
}

function displayNumberInput(question) {
    const inputDiv = document.createElement('div');
    inputDiv.innerHTML = `
        <label>${question.question}</label>
        <input type="number" name="${question.name}" min="${question.min}" max="${question.max}" required>
        <button type="button" onclick="submitAnswer()">Next</button>`;
    form.appendChild(inputDiv);
}

function displayCheckboxInput(question) {
    const inputDiv = document.createElement('div');
    inputDiv.innerHTML = `
        <label>${question.question}</label>
        <input type="checkbox" name="${question.name}">
        <label>Yes</label>
        <button type="button" onclick="submitAnswer()">Next</button>`;
    form.appendChild(inputDiv);
}

function displaySelectInput(question) {
    const inputDiv = document.createElement('div');
    const optionsHtml = question.options.map(option => `<option value="${option.value}">${option.text}</option>`).join('');
    inputDiv.innerHTML = `
        <label>${question.question}</label>
        <select name="${question.name}" required>
            ${optionsHtml}
        </select>
        <button type="button" onclick="submitAnswer()">Next</button>`;
    form.appendChild(inputDiv);
}

function displayRadioInput(question) {
    const inputDiv = document.createElement('div');
    const optionsHtml = question.options.map(option => `
        <input type="radio" id="${option.value}" name="${question.name}" value="${option.value}" required>
        <label for="${option.value}">${option.text}</label>`).join('');
    inputDiv.innerHTML = `
        <label>${question.question}</label>
        ${optionsHtml}
        <button type="button" onclick="submitAnswer()">Next</button>`;
    form.appendChild(inputDiv);
}

function submitAnswer() {
    const currentQuestion = questions[currentQuestionIndex - 1]; // Get the current question
    const userResponse = getUserResponse(currentQuestion); // Get user's response based on question type
    displayUserResponse(userResponse); // Display user's response in the chat
    form.innerHTML = ''; // Clear previous question inputs

    if (currentQuestionIndex < questions.length) {
        displayNextQuestion();
    } else {
        displayMessage('Thank you for completing the diagnostics!', 'bot');
    }
}

function displayMessage(message, sender) {
    const messageElement = document.createElement('div');
    messageElement.classList.add('message', sender);
    messageElement.innerText = message;
    chatBox.appendChild(messageElement);
}

function displayUserResponse(message) {
    const responseElement = document.createElement('div');
    responseElement.classList.add('message', 'user-response');
    responseElement.innerText = message;
    chatBox.appendChild(responseElement);
}

function getUserResponse(question) {
    switch (question.inputType) {
        case 'number':
            return form.querySelector(`input[name="${question.name}"]`).value;
        case 'checkbox':
            return form.querySelector(`input[name="${question.name}"]:checked`) ? 'Yes' : 'No';
        case 'select':
            return form.querySelector(`select[name="${question.name}"]`).value;
        case 'radio':
            return form.querySelector(`input[name="${question.name}"]:checked`).value;
        default:
            return ''; // Handle other input types as needed
    }
}

// Call this function to display the initial greeting message
displayMessage(greetingMessage, 'bot');


form.addEventListener('submit', (event) => {
  event.preventDefault(); // Prevent default form submission
  const formData = new FormData(form); // Get form data
  fetch('{% url "home" %}', { // Replace '{% url "home" %}' with your actual URL path
      method: 'POST',
      body: formData,
  })
  .then(response => response.json())
  .then(data => {
      console.log(data); // Process response data if needed
      // Optionally, display a message in the chat confirming successful submission
      displayMessage('Answers submitted successfully!', 'bot');
  })
  .catch(error => {
      console.error('Error:', error);
      // Handle errors if needed
  });
});