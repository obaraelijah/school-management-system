import { Outlet } from 'react-router-dom';
import Sidebar from '../headers/dashboard/Sidebar';

const DashboardLayout = () => {
  return (
    <main className='md:flex md:h-screen overflow-hidden'>
      <Sidebar />
      <section className='overflow-y-scroll hide-scrollbar w-full md:px-10 py-8 bg-background relative bottom-20 md:bottom-0 px-5'>
        <Outlet />
      </section>
    </main>
  );
};

export default DashboardLayout;
