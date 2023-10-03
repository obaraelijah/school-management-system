import { Outlet } from 'react-router-dom';
import Header from '../headers/root/Header';

const RootLayout = () => {
  const date = new Date();
  return (
    <>
      <Header />
      <Outlet />
      <footer className='bg-white text-center py-4'>
        <p>&copy; {date.getFullYear()} smartEdConnect. All rights reserved</p>
      </footer>
    </>
  );
};

export default RootLayout;
