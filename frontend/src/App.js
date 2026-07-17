// import React from 'react';
// import EligibilityForm from './components/EligibilityForm';
// import EligibleSchemesList from './components/EligibleSchemesList';

// function App() {
//   return (
//     <div className="bg-gray-100 min-h-screen">
//       <header className="bg-blue-500 text-white p-4">
//         <h1 className="text-2xl font-bold">Government Scheme Eligibility Checker</h1>
//       </header>
//       <main className="container mx-auto py-6">
//         <EligibilityForm />
//         <EligibleSchemesList />
//       </main>
//     </div>
//   );
// }

// export default App;


// import React, { useState } from 'react';
// import EligibilityForm from './components/EligibilityForm';
// import EligibleSchemesList from './components/EligibleSchemesList';
// import './App.css';

// function App() {
//   const [results, setResults] = useState(null));

//   return (
//     <div className="app-container">
//       <h1 className="app-title">Government Scheme Eligibility Checker</h1>
//       <EligibilityForm onResults={setResults} />
//       <EligibleSchemesList eligibilityResults={results} />
//     </div>
//   );
// }

// export default App;


import React, { useState, useEffect } from 'react';
import EligibilityForm from './components/EligibilityForm';
import EligibleSchemesList from './components/EligibleSchemesList';
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

  return (
    <div className="app-container">
      {!isOnline && (
        <div className="offline-banner">
          ⚠️ You're offline. Showing last saved results.
        </div>
      )}
      <h1 className="app-title">Government Scheme Eligibility Checker</h1>
      <EligibilityForm onResults={handleResults} />
      <EligibleSchemesList results={results} />
    </div>
  );
}
export default App;
