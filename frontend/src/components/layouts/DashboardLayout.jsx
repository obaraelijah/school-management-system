import { Outlet } from 'react-router-dom';
import Header from '../headers/dashboard/Header';

const DashboardLayout = () => {
  return (
    <main className='md:flex md:h-screen'>
      <Header />
      <Outlet />
    </main>
  );
};

export default DashboardLayout;
