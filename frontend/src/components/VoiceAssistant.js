import React, { useState, useRef } from 'react';

const VoiceAssistant = ({ onCommand }) => {
  const [listening, setListening] = useState(false);
  const [transcript, setTranscript] = useState('');
  const recognitionRef = useRef(null);

  const startListening = () => {
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    if (!SpeechRecognition) {
      alert('Voice recognition not supported in this browser. Try Chrome.');
      return;
    }
    const recognition = new SpeechRecognition();
    recognition.lang = 'en-IN';
    recognition.continuous = false;
    recognition.interimResults = false;

    recognition.onresult = (event) => {
      const text = event.results[0][0].transcript;
      setTranscript(text);
      handleVoiceCommand(text.toLowerCase());
    };

    recognition.onend = () => setListening(false);
    recognition.onerror = () => setListening(false);

    recognitionRef.current = recognition;
    recognition.start();
    setListening(true);
  };

  const speak = (text) => {
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = 'en-IN';
    window.speechSynthesis.speak(utterance);
  };

  const handleVoiceCommand = (text) => {
    if (text.includes('check') && text.includes('scheme')) {
      speak('Please fill in your details and I will check your eligible schemes.');
      onCommand('check');
    } else if (text.includes('read') || text.includes('repeat')) {
      speak('Reading your eligible schemes now.');
      onCommand('read');
    } else if (text.includes('search') && text.includes('farmer')) {
      speak('Searching farmer schemes.');
      onCommand('search-farmer');
    } else if (text.includes('document')) {
      speak('Please check the required documents section for each scheme.');
      onCommand('documents');
    } else {
      speak("Sorry, I didn't understand that. Try saying check my schemes.");
    }
  };

  return (
    <div className="voice-assistant">
      <button
        className={`voice-btn ${listening ? 'listening' : ''}`}
        onClick={startListening}
      >
        🎤 {listening ? 'Listening...' : 'Voice Assistant'}
      </button>
      {transcript && <p className="voice-transcript">You said: "{transcript}"</p>}
    </div>
  );
};

export default VoiceAssistant;