import React from 'react';

const EligibleSchemesList = ({ eligibilityResults = [] }) => {
  return (
    <div className="p-6 bg-white rounded-lg shadow-md mt-4">
      <h2 className="text-xl font-bold mb-4">Eligible Schemes</h2>
      <ul className="list-disc pl-4">
        {eligibilityResults.map((scheme, index) => (
          <li key={index}>{scheme}</li>
        ))}
      </ul>
    </div>
  );
};

export default EligibleSchemesList;