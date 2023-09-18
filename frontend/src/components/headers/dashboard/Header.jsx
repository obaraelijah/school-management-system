import { NavLink } from 'react-router-dom';

import Logo from '../../Logo';

const Header = () => {
  return (
    <header className='md:w-3/12 h-full'>
      <div className='hidden md:block bg-dashboard-100 w-full text-white text-center py-8 h-full'>
        <Logo />
        <nav>
          <ul className='flex gap-7 flex-col justify-center items-center'>
            <li>
              <NavLink to={'/dashboard'} className={' '}>
                dashboard
              </NavLink>
            </li>
            <li>
              <NavLink to={'/dashboard/add'} className={''}>
                Add
              </NavLink>
            </li>
            {/*<li>
            <NavLink to={} className={``}>
              
            </NavLink>
          </li> */}
          </ul>
        </nav>
      </div>
      {/* <div className='md:hidden'>
        <Logo />
      </div> */}

      <div className='fixed bottom-0 flex md:hidden bg-dashboard-100 w-full py-6 px-4 overflow-x-scroll text-white'>
        <nav>
          <ul className='flex gap-7  justify-center items-center capitalize'>
            <li>
              <NavLink to={'/dashboard'} className={' '}>
                dashboard
              </NavLink>
            </li>

            <li>
              <NavLink to={'/dashboard/add'} className={''}>
                Add
              </NavLink>
            </li>
            {/*<li>
            <NavLink to={} className={``}>
              
            </NavLink>
          </li> */}
          </ul>
        </nav>
      </div>
    </header>
  );
};

export default Header;
