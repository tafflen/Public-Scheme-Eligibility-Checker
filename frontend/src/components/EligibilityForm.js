// import React, { useState } from 'react';
// import axios from 'axios';

// const EligibilityForm = () => {
//   const [userData, setUserData] = useState({
//     name: '',
//     age: '',
//     gender: '',
//     state: '',
//     district: '',
//     occupation: '',
//     annualIncome: '',
//     education: '',
//     category: '',
//     disabilityStatus: ''
//   });

//   const [eligibilityResults, setEligibilityResults] = useState([]);

//   const handleChange = (e) => {
//     setUserData({ ...userData, [e.target.name]: e.target.value });
//   };

//   const handleSubmit = async (e) => {
//     e.preventDefault();
//     try {
//       const response = await axios.post('http://localhost:8000/check-eligibility/', userData);
//       setEligibilityResults(response.data.schemes);
//     } catch (error) {
//       console.error(error);
//     }
//   };

//   return (
//     <div className="p-6 bg-white rounded-lg shadow-md">
//       <h2 className="text-xl font-bold mb-4">Check Your Eligibility</h2>
//       <form onSubmit={handleSubmit}>
//         {/* Form fields */}
//         <input type="text" name="name" placeholder="Name" onChange={handleChange} />
//         <input type="number" name="age" placeholder="Age" onChange={handleChange} />
//         {/* Other form fields */}
//         <button type="submit" className="bg-blue-500 text-white px-4 py-2 rounded">Check Eligibility</button>
//       </form>
//     </div>
//   );
// };

// export default EligibilityForm;


import React, { useState } from 'react';

const EligibilityForm = ({ onResults }) => {
  const [formData, setFormData] = useState({
    age: '',
    gender: 'male',
    annual_income: '',
    occupation: 'farmer'
  });
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      const response = await fetch('http://127.0.0.1:8000/check-eligibility', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          age: parseInt(formData.age),
          gender: formData.gender,
          annual_income: parseInt(formData.annual_income),
          occupation: formData.occupation
        })
      });
      const data = await response.json();
      // onResults(data.eligible || []);
      onResults(data); 
    } catch (err) {
      console.error('Error checking eligibility:', err);
      onResults([]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="eligibility-form">
      <h2>Check Your Eligibility</h2>
      <form onSubmit={handleSubmit}>
        <div className="form-grid">
          <div className="form-group">
            <label>Age</label>
            <input type="number" name="age" value={formData.age} onChange={handleChange} required />
          </div>
          <div className="form-group">
            <label>Gender</label>
            <select name="gender" value={formData.gender} onChange={handleChange}>
              <option value="male">Male</option>
              <option value="female">Female</option>
              <option value="other">Other</option>
            </select>
          </div>
          <div className="form-group">
            <label>Annual Income (₹)</label>
            <input type="number" name="annual_income" value={formData.annual_income} onChange={handleChange} required />
          </div>
          <div className="form-group">
            <label>Occupation</label>
            <select name="occupation" value={formData.occupation} onChange={handleChange}>
              <option value="farmer">Farmer</option>
              <option value="student">Student</option>
              <option value="entrepreneur">Entrepreneur</option>
              <option value="unemployed">Unemployed</option>
              <option value="any">Other</option>
            </select>
          </div>
        </div>
        <button type="submit" className="submit-btn" disabled={loading}>
          {loading ? 'Checking...' : 'Check Eligibility'}
        </button>
      </form>
    </div>
  );
};

export default EligibilityForm;