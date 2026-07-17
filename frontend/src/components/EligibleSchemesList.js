// import React from 'react';

// const EligibleSchemesList = ({ eligibilityResults = [] }) => {
//   return (
//     <div className="p-6 bg-white rounded-lg shadow-md mt-4">
//       <h2 className="text-xl font-bold mb-4">Eligible Schemes</h2>
//       <ul className="list-disc pl-4">
//         {eligibilityResults.map((scheme, index) => (
//           <li key={index}>{scheme}</li>
//         ))}
//       </ul>
//     </div>
//   );
// };

// export default EligibleSchemesList;

import React from 'react';

const EligibleSchemesList = ({ eligibilityResults = [] }) => {
  if (eligibilityResults.length === 0) {
    return (
      <div className="results-section">
        <h2>Eligible Schemes</h2>
        <p className="empty-state">No results yet — fill the form above to check eligibility.</p>
      </div>
    );
  }

  return (
    <div className="results-section">
      <h2>Eligible Schemes ({eligibilityResults.length})</h2>
      <div className="scheme-grid">
        {eligibilityResults.map((item, index) => (
          <div className="scheme-card" key={index}>
            <h3>{item.scheme}</h3>
            <p>{item.benefits}</p>
            {item.apply_link && (
              <a href={item.apply_link} target="_blank" rel="noopener noreferrer">
                Apply Now →
              </a>
            )}
          </div>
        ))}
      </div>
    </div>
  );
};

export default EligibleSchemesList;