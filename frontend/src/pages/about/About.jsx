import React from 'react';
import logo from '../images/smartEdConnect.logo.jpg';

const About = () => {
  return (
    <div className="bg-gray-100 py-12">
      <div className="container mx-auto flex items-center">
        <div className="w-1/2">
          <h1 className="text-4xl font-semibold text-gray-800 mb-4">
            About Our School Management System
          </h1>
          <p className="text-lg text-gray-600 mb-4">
            Welcome to our smartEdConnect School Management System, where we empower
            educational institutions with the tools they need to thrive in the digital age.
            Our mission is to streamline administrative tasks, enhance communication, and
            provide valuable insights to educators, students, and parents alike.
          </p>
          <p className="text-lg text-gray-600 mb-4">
            With smartEdConnect, educational institutions can efficiently manage student
            records, track academic performance, and simplify communication channels. We
            believe in the transformative power of technology in education and are committed
            to supporting institutions in their quest for excellence.
          </p>
          <button className="bg-blue-500 text-white px-6 py-3 rounded-full hover:bg-blue-600">
            Learn More
          </button>
        </div>
        <div className="w-1/2">
          <img src={logo} alt="About Us" className="rounded-lg shadow-lg" />
        </div>
      </div>
    </div>
  );
};

export default About;
