import { NavLink } from 'react-router-dom';

const NavBar = () => {
  return (
    <nav className='text-white'>
      <ul className='flex gap-7 md:flex-row flex-col capitalize'>
        <li>
          <NavLink to={''} className={' '}>
            home
          </NavLink>
        </li>
        <li>
          <NavLink to={'/about'} className={''}>
            about
          </NavLink>
        </li>
        <li>
          <NavLink to={'/contact'} className={''}>
            contact
          </NavLink>
        </li>
      </ul>
    </nav>
  );
};

export default NavBar;
