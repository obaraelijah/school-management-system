import React from 'react';
import './Contact.css'; // Import your CSS file for styling

const Contact = () => {
  return (
    <div className="contact-container">
      <div className="contact-content">
        <h1>Contact Us</h1>
        <p>
          Have questions or need assistance with our Education Management
          System? We're here to help!
        </p>
        <div className="contact-details">
          <p>Email: info@schoolmanagementsystem.com</p>
          <p>Phone: +1 123-456-7890</p>
          <p>Address: 123 Main Street, City, Country</p>
        </div>
      </div>
      <div className="contact-image">
        <img
          src="/images/contact-image.jpg" // Replace with the correct image path
          alt="Contact Us"
        />
      </div>
    </div>
  );
};

export default Contact;
