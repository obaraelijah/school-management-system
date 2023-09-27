import React from 'react';
import './About.css'; // Import your CSS file
import logo from '../images/smartEdConnect.logo.jpg';

const About = () => {
  return (
    <div className="about-container">
      <div className="about-content">
        <h1 className="about-heading">About Our School Management System</h1>
        <p className="about-paragraph">
          Welcome to our smartEdConnect School Management System, where we empower
          educational institutions with the tools they need to thrive in the digital age.
          Our mission is to streamline administrative tasks, enhance communication, and
          provide valuable insights to educators, students, and parents alike.
        </p>
        <p className="about-paragraph">
          With smartEdConnect, educational institutions can efficiently manage student
          records, track academic performance, and simplify communication channels. We
          believe in the transformative power of technology in education and are committed
          to supporting institutions in their quest for excellence.
        </p>
        <button className="learn-more-button">Learn More</button>
      </div>
      <div className="about-image">
        <img src={logo} alt="About Us" />
      </div>
    </div>
  );
};

export default About;
