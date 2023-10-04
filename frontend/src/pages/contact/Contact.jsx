import React from 'react';

const Contact = () => {
  return (
    <div className="bg-gray-100 py-12">
      <div className="container mx-auto flex items-center">
        <div className="w-1/2">
          <div className="contact-content">
            <h1 className="text-4xl font-semibold text-gray-800 mb-4">Contact Us</h1>
            <p className="text-lg text-gray-600 mb-4">
              Have questions or need assistance with our Education Management System? We're here to help!
            </p>
            <div className="contact-details">
              <p className="text-lg text-gray-600 mb-2">Email: info@schoolmanagementsystem.com</p>
              <p className="text-lg text-gray-600 mb-2">Phone: +1 123-456-7890</p>
              <p className="text-lg text-gray-600">Address: 123 Main Street, City, Country</p>
            </div>
          </div>
        </div>
        <div className="w-1/2">
          <img
            src="/images/contact-image.jpg" // Replace with the correct image path
            alt="Contact Us"
            className="rounded-lg shadow-lg"
          />
        </div>
      </div>
    </div>
  );
};

export default Contact;
