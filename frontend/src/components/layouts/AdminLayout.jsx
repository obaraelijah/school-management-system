import { Outlet } from 'react-router-dom';
import AdminHeader from '../headers/admin/AdminHeader';

const AdminLayout = () => {
  return (
    <div className='flex md:h-screen overflow-hidden '>
      <AdminHeader />
      <div className='hide-scrollbar overflow-y-scroll p-5'>
        <Outlet />
      </div>
    </div>
  );
};

export default AdminLayout;
