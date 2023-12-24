function submitCommand() {
    var userInput = document.getElementById('inputText').value;
    appendMessage(userInput,'user');

    // Use the Fetch API to send a POST request to your Django backend
    fetch('/processing/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken') // Include CSRF token for Django
        },
        body: JSON.stringify({ 'user_input': userInput })
    })
    .then(response => response.json())
    .then(data => {
        // Update the #output div with the response from the backend
        // var outputDiv = document.getElementById('chat-display');
        // outputDiv.innerHTML = `<div>${data.response}</div>`;
        
        // Speak the response using the Web Speech API
        if(data.response==null){
            speak('Completed');
            appendMessage('Completed','Bot');
        }else{
            appendMessage(data.response,'Bot');
            speak(data.response);
        }
    })
    .catch(error => console.error('Error:', error));
};

// Function to get CSRF token from cookies
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            };
        };
    };
    return cookieValue;
};

// Function to speak the provided text using the Web Speech API
function speak(text) {
    var synth = window.speechSynthesis;
    var voices = synth.getVoices();
    
    // Use a female voice (you may need to adjust this based on available voices in your browser)
    var voice = voices.find(v => v.name.includes('female'));

    // Create a SpeechSynthesisUtterance instance
    var utterance = new SpeechSynthesisUtterance(text);
    utterance.voice = voice;

    // Speak the text
    synth.speak(utterance);
};




var btn=document.querySelector('.talk');
const Send=document.querySelector('.sendbutton');
var input=document.getElementById('inputText');

const SpeechRecognition=window.SpeechRecognition || window.webkitSpeechRecognition;
const recognition=new SpeechRecognition();



recognition.onresult=(event)=>{
    const current=event.resultIndex;
    const transcript=event.results[current][0].transcript;
    content.textContent=transcript;
    input.value=transcript.toLowerCase();
    submitCommand();

};


btn.addEventListener('click',()=>{
    recognition.start();
})

input.addEventListener('focus',()=>{
    Send.style.display='block';
    btn.style.display='none';

});

document.querySelector('.container').addEventListener('click',()=>{
    Send.style.display='none';
    btn.style.display='block';

});


Send.addEventListener('click',()=>{
    submitCommand();
});


input.addEventListener('keyup', (event) => {
    if (event.key === 'Enter') {
        Send.click();
    };

});

const chatDisplay = document.getElementById('chat-display');

// const userInput = document.getElementById('inputText');

// const sendButton = document.querySelector('.sendbutton');


function appendMessage(message, sender) {
    const messageElement = document.createElement('div');
    messageElement.classList.add('post');
    messageElement.textContent = `${message}`;

    const reElement = document.createElement('div');
    reElement.classList.add('get');
    reElement.textContent = `${message}`;
    if (sender=='Bot') {
        chatDisplay.appendChild(messageElement);
    } else {
        chatDisplay.appendChild(reElement);
        
    };
    chatDisplay.scrollTop = chatDisplay.scrollHeight;
    input.value='';

};

document.addEventListener('DOMContentLoaded',()=>{
    appendMessage('Hi, please how may I help you?','Bot')

});