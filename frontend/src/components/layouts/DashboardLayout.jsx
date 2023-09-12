import { Outlet } from 'react-router-dom';

const DashboardLayout = () => {
  return (
    <>
      <h2>DashboardLayout header</h2>
      <Outlet />
    </>
  );
};

export default DashboardLayout;
