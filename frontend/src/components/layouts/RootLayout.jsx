import { Outlet } from 'react-router-dom';
import Header from '../headers/root/Header';

const RootLayout = () => {
  return (
    <>
      <Header />
      <Outlet />
    </>
  );
};

export default RootLayout;
