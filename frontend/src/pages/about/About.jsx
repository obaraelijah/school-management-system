import React from 'react';
import './About.css'; // Import your CSS file

const About = () => {
  return (
    <div className="about-container">
      <div className="about-content">
        <h1>About Our Education Management System</h1>
        <p>
          Welcome to our smartEdConnect Education Management System ,where we
          empower educational institutions with the tools they need to thrive in the
          digital age. Our mission is to streamline administrative tasks, enhance
          communication, and provide valuable insights to educators, students, and
          parents alike.
        </p>
        <p>
          With smartEdConnect, educational institutions can efficiently manage student records,
          track academic performance, and simplify communication channels. We believe in
          the transformative power of technology in education and are committed to
          supporting institutions in their quest for excellence.
        </p>
        <button className="learn-more-button">Learn More</button>
      </div>
      <div className="about-image">
        <img
          src="https://via.placeholder.com/400x300" // Replace with an image related to your EMS
          alt="Education Management System"
        />
      </div>
    </div>
  );
};

export default About;
