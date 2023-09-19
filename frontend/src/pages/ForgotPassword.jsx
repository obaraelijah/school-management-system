import React from 'react';
import Button from '../components/Button'; // Make sure to import the Button component correctly
import Input from '../components/forms/Input'; // Make sure to import the Input component correctly

function ForgotPassword() {
  const handleResetPassword = () => {
    // Implement your password reset logic here
  };

  return (
    <div>
      <h2>Forgot Password</h2>
      <form onSubmit={handleResetPassword}>
        <div>
          <label htmlFor="email">Email:</label>
          <Input type="email" id="email" name="email" placeholder="Enter your email" />
        </div>
        <Button type="submit">Reset Password</Button> {/* Button with child text */}
      </form>
    </div>
  );
}

export default ForgotPassword;
