import { NavLink } from 'react-router-dom';

const NavBar = () => {
  return (
    <nav>
      <ul className='flex gap-7'>
        <li>
          <NavLink to={''} className={' text-black'}>
            home
          </NavLink>
        </li>
        <li>
          <NavLink to={'/about'} className={'text-black'}>
            about
          </NavLink>
        </li>
        <li>
          <NavLink to={'/contact'} className={'text-black'}>
            contact
          </NavLink>
        </li>
        <li>
          <NavLink
            to={'/login'}
            className={'bg-white text-black px-3 py-1 rounded-lg'}
          >
            login
          </NavLink>
        </li>

        <li>
          <NavLink to={'/signup'} className={'bg-light px-3 py-1 rounded-lg '}>
            signup
          </NavLink>
        </li>
      </ul>
    </nav>
  );
};

export default NavBar;
