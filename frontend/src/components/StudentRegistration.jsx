// src/StudentRegistration.jsx
import React, { useState } from 'react';

const StudentRegistration = () => {
  const [formData, setFormData] = useState({
    username: '',
    email: '',
    password: '',
    // Add other registration fields here
  });

  const handleInputChange = (e) => {
    // Handle input changes and update formData state
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Handle student registration form submission
  };

  return (
    <div className="container mx-auto mt-8">
      <h2 className="text-2xl font-semibold mb-4">Student Registration</h2>
      <form onSubmit={handleSubmit}>
        {/* Registration form fields */}
        <button type="submit" className="bg-blue-500 hover:bg-blue-600 text-white font-semibold py-2 px-4 rounded">
          Register
        </button>
      </form>
    </div>
  );
};

export default StudentRegistration;
