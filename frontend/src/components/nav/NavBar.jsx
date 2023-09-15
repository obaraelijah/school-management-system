import { NavLink } from 'react-router-dom';

const NavBar = () => {
  return (
    <nav>
      <ul className='flex gap-7'>
        <li>
          <NavLink to={'login'} className={'bg-white text-black'}>
            login
          </NavLink>
        </li>

        <li>
          <NavLink to={'signup'}>signup</NavLink>
        </li>
      </ul>
    </nav>
  );
};

export default NavBar;