import Logo from '../Logo';
import NavBar from '../nav/NavBar';
import { NavLink, Outlet } from 'react-router-dom';
import { RiMenu2Line } from 'react-icons/ri';

const RootLayout = () => {
  return (
    <>
      <header className='flex justify-between w-full py-7 px-5 bg-btn text-white sticky top-0 items-center z-50'>
        <RiMenu2Line className='text-3xl md:hidden ' />
        <Logo />
        <NavBar />
        <div className='flex justify-between gap-1 md:gap-4 items-center'>
          <NavLink
            to={'/login'}
            className={'bg-white text-black px-3 py-1 rounded-lg'}
          >
            login
          </NavLink>

          <NavLink to={'/signup'} className={'bg-light px-3 py-1 rounded-lg '}>
            signup
          </NavLink>
        </div>
      </header>
      <Outlet />
    </>
  );
};

export default RootLayout;
