import Header from '../headers/users/Header';
import { Outlet } from 'react-router-dom';
const RootLayout = () => {
  return (
    <>
      <Header />
      <Outlet />
    </>
  );
};

export default RootLayout;
