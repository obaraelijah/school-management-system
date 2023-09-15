import Logo from '../Logo';
import NavBar from '../nav/NavBar';
import { Outlet } from 'react-router-dom';
const RootLayout = () => {
  return (
    <>
      <header className='flex justify-between w-full py-7 px-5 bg-btn text-white'>
        <Logo />
        <NavBar />
      </header>
      <Outlet />
    </>
  );
};

export default RootLayout;
