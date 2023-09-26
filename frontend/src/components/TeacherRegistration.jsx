// src/TeacherRegistration.jsx
import React, { useState } from 'react';

const TeacherRegistration = () => {
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
    // Handle teacher registration form submission
  };

  return (
    <div className="container mx-auto mt-8">
      <h2 className="text-2xl font-semibold mb-4">Teacher Registration</h2>
      <form onSubmit={handleSubmit}>
        {/* Registration form fields */}
        <button type="submit" className="bg-green-500 hover:bg-green-600 text-white font-semibold py-2 px-4 rounded">
          Register
        </button>
      </form>
    </div>
  );
};

export default TeacherRegistration;
