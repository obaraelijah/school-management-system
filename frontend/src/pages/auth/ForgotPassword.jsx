import React from 'react'; // Make sure to import React if not already imported
import Button from '../../components/Button'; // Make sure to import the Button component correctly

function ForgotPassword() {
  const handleResetPassword = () => {
    // Implement your password reset logic here
  };

  return (
    <div className="bg-gray-100 min-h-screen flex justify-center items-center">
      <div className="bg-white p-8 rounded-lg shadow-md w-full max-w-md">
        <h2 className="text-2xl font-semibold mb-4">Forgot Password</h2>
        <form onSubmit={handleResetPassword} className='flex flex-col gap-4' >
          <div>
            <label htmlFor="email" className="text-sm font-medium">Email:</label>
            <input
              type="email"
              id="email"
              name="email"
              placeholder="Enter your email"
              className="w-full px-3 py-2 border rounded-md focus:outline-none focus:border-blue-500"
            />
          </div>
          <Button type="submit" className="bg-blue-500 text-white py-2 rounded-lg">
            Reset Password
          </Button> {/* Button with child text */}
        </form>
      </div>
    </div>
  );
}

export default ForgotPassword;
