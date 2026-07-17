import React, { useState, useEffect } from 'react';
import EligibilityForm from './components/EligibilityForm';
import EligibleSchemesList from './components/EligibleSchemesList';
import VoiceAssistant from './components/VoiceAssistant';  // ← ADDED
import './App.css';

function App() {
  const [results, setResults] = useState(() => {
    const cached = localStorage.getItem('lastResults');
    return cached ? JSON.parse(cached) : null;
  });
  const [isOnline, setIsOnline] = useState(navigator.onLine);

  useEffect(() => {
    const goOnline = () => setIsOnline(true);
    const goOffline = () => setIsOnline(false);
    window.addEventListener('online', goOnline);
    window.addEventListener('offline', goOffline);
    return () => {
      window.removeEventListener('online', goOnline);
      window.removeEventListener('offline', goOffline);
    };
  }, []);

  const handleResults = (data) => {
    setResults(data);
    localStorage.setItem('lastResults', JSON.stringify(data));
  };

  const handleVoiceCommand = (command) => {  // ← ADDED
    console.log('Voice command received:', command);
  };  // ← ADDED

  return (
    <div className="app-container">
      {!isOnline && (
        <div className="offline-banner">
          ⚠️ You're offline. Showing last saved results.
        </div>
      )}
      <h1 className="app-title">Government Scheme Eligibility Checker</h1>
      <VoiceAssistant onCommand={handleVoiceCommand} />  {/* ← ADDED */}
      <EligibilityForm onResults={handleResults} />
      <EligibleSchemesList results={results} />
    </div>
  );
}
export default App;