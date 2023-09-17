import { NavLink } from 'react-router-dom';

const NavBar = () => {
  return (
    <nav className='text-white hidden md:block'>
      <ul className='flex gap-7'>
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
