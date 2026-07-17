import React, { useState } from 'react';
import axios from 'axios';

const EligibilityForm = () => {
  const [userData, setUserData] = useState({
    name: '',
    age: '',
    gender: '',
    state: '',
    district: '',
    occupation: '',
    annualIncome: '',
    education: '',
    category: '',
    disabilityStatus: ''
  });

  const [eligibilityResults, setEligibilityResults] = useState([]);

  const handleChange = (e) => {
    setUserData({ ...userData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:8000/check-eligibility/', userData);
      setEligibilityResults(response.data.schemes);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div className="p-6 bg-white rounded-lg shadow-md">
      <h2 className="text-xl font-bold mb-4">Check Your Eligibility</h2>
      <form onSubmit={handleSubmit}>
        {/* Form fields */}
        <input type="text" name="name" placeholder="Name" onChange={handleChange} />
        <input type="number" name="age" placeholder="Age" onChange={handleChange} />
        {/* Other form fields */}
        <button type="submit" className="bg-blue-500 text-white px-4 py-2 rounded">Check Eligibility</button>
      </form>
    </div>
  );
};

export default EligibilityForm;
