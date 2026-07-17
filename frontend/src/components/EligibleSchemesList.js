import React from 'react';

const OFFICIAL_DOMAINS = ['gov.in', 'nic.in'];

const isOfficialLink = (url) => {
  try {
    const domain = new URL(url).hostname;
    return OFFICIAL_DOMAINS.some(d => domain.endsWith(d));
  } catch {
    return false;
  }
};

const SchemeCard = ({ item, status }) => {
  const borderColor = status === 'eligible' ? '#22c55e' : status === 'partial' ? '#f59e0b' : '#ef4444';
  return (
    <div className="scheme-card" style={{ borderLeftColor: borderColor }}>
      <h3>{item.scheme}</h3>
      <p>{item.benefits}</p>
      {status !== 'eligible' && item.reasons?.length > 0 && (
        <div className="ineligible-reasons">
          <strong>Why not eligible:</strong>
          <ul>
            {item.reasons.map((r, i) => <li key={i}>{r}</li>)}
          </ul>
        </div>
      )}
      {status === 'eligible' && item.apply_link && (
        <>
          <a href={item.apply_link} target="_blank" rel="noopener noreferrer">Apply Now →</a>
          {!isOfficialLink(item.apply_link) && (
            <p className="fraud-warning">
              ⚠️ This link doesn't look like an official .gov.in site. Verify before entering personal details.
            </p>
          )}
        </>
      )}
    </div>
  );
};

const EligibleSchemesList = ({ results }) => {
  const { eligible = [], partial = [], not_eligible = [] } = results || {};

  if (!eligible.length && !partial.length && !not_eligible.length) {
    return (
      <div className="results-section">
        <h2>Eligible Schemes</h2>
        <p className="empty-state">No results yet — fill the form above to check eligibility.</p>
      </div>
    );
  }

  return (
    <div className="results-section">
      {eligible.length > 0 && (
        <>
          <h2>✅ Eligible Schemes ({eligible.length})</h2>
          <div className="scheme-grid">
            {eligible.map((item, i) => <SchemeCard key={i} item={item} status="eligible" />)}
          </div>
        </>
      )}
      {partial.length > 0 && (
        <>
          <h2>⚠️ Partially Eligible ({partial.length})</h2>
          <div className="scheme-grid">
            {partial.map((item, i) => <SchemeCard key={i} item={item} status="partial" />)}
          </div>
        </>
      )}
      {not_eligible.length > 0 && (
        <>
          <h2>❌ Not Eligible ({not_eligible.length})</h2>
          <div className="scheme-grid">
            {not_eligible.map((item, i) => <SchemeCard key={i} item={item} status="not_eligible" />)}
          </div>
        </>
      )}
    </div>
  );
};

export default EligibleSchemesList;