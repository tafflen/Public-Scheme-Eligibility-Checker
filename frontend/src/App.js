import React from 'react';
import EligibilityForm from './components/EligibilityForm';
import EligibleSchemesList from './components/EligibleSchemesList';

function App() {
  return (
    <div className="bg-gray-100 min-h-screen">
      <header className="bg-blue-500 text-white p-4">
        <h1 className="text-2xl font-bold">Government Scheme Eligibility Checker</h1>
      </header>
      <main className="container mx-auto py-6">
        <EligibilityForm />
        <EligibleSchemesList />
      </main>
    </div>
  );
}

export default App;
import React from 'react';
import EligibilityForm from './components/EligibilityForm';
import EligibleSchemesList from './components/EligibleSchemesList';

function App() {
  return (
    <div className="bg-gray-100 min-h-screen">
      <header className="bg-blue-500 text-white p-4">
        <h1 className="text-2xl font-bold">Government Scheme Eligibility Checker</h1>
      </header>
      <main className="container mx-auto py-6">
        <EligibilityForm />
        <EligibleSchemesList />
      </main>
    </div>
  );
}

export default App;
