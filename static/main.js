// Initialize variables
const questionContainer = document.getElementById('question-container');
const form = document.getElementById('question-form');
const submitBtn = document.getElementById('submit-btn');

// Define initial greeting message
const greetingMessage = "Hello! Let's assess your energy efficiency. Please answer the following questions.";

// Questions and image options
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
        inputType: 'image',
        name: 'lighting',
        options: [
            { value: 'incandescent', imageUrl: '{% static "images/images.jpeg" %}', alt: 'Incandescent Bulbs' },
            { value: 'led', imageUrl: "{% static 'images/images.jpeg' %}", alt: 'LED Bulbs' }
        ]
    },
];

let currentQuestionIndex = 0;

// Display initial greeting message
displayMessage(greetingMessage, 'bot');

// Event listener for submit button
submitBtn.addEventListener('click', submitForm);

// Start the diagnostics process
displayNextQuestion();

function displayNextQuestion() {
    const currentQuestion = questions[currentQuestionIndex];
    clearQuestionContainer();
    displayMessage(currentQuestion.question, 'bot');

    switch (currentQuestion.inputType) {
        case 'number':
            displayNumberInput(currentQuestion);
            break;
        case 'image':
            displayImageOptions(currentQuestion);
            break;
        // Add more input types if needed
        default:
            break;
    }
}

function displayNumberInput(question) {
    const inputDiv = document.createElement('div');
    inputDiv.innerHTML = `
        <label for="${question.name}">${question.question}</label>
        <input type="number" id="${question.name}" name="${question.name}" min="${question.min}" max="${question.max}" required>
    `;
    questionContainer.appendChild(inputDiv);
}

function displayImageOptions(question) {
    const inputDiv = document.createElement('div');
    inputDiv.innerHTML = `
        <label>${question.question}</label>
        <div class="option-container">
            ${question.options.map(option => `
                <div class="option">
                    <input type="radio" id="${option.value}" name="${question.name}" value="${option.value}" onchange="handleImageSelection('${option.value}')">
                    <label for="${option.value}">
                        <img src="${option.imageUrl}" alt="${option.alt}">
                    </label>
                </div>`).join('')}
        </div>
    `;
    questionContainer.appendChild(inputDiv);
}

function handleImageSelection(selectedValue) {
    // Handle selected image option if needed
}

function submitForm() {
    const formData = new FormData(form);
    const userResponses = {};
    for (const [name, value] of formData.entries()) {
        userResponses[name] = value;
    }
    // Send userResponses to the backend for processing
    console.log(userResponses); // Example: send to backend using fetch or other methods
    // Proceed to the next question or show the final result as needed
    currentQuestionIndex++;
    if (currentQuestionIndex < questions.length) {
        displayNextQuestion();
    } else {
        displayMessage('Thank you for completing the diagnostics!', 'bot');
    }
}

function clearQuestionContainer() {
    questionContainer.innerHTML = '';
}

function displayMessage(message, sender) {
    const messageElement = document.createElement('div');
    messageElement.classList.add('message', sender);
    messageElement.innerText = message;
    questionContainer.appendChild(messageElement);
}
