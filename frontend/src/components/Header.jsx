import NavBar from './nav/NavBar';
import { Link } from 'react-router-dom';

const Header = () => {
  return (
    <header className='flex justify-between items-center p-8'>
      <h1 className='md:text-5xl text-2xl'>
        {' '}
        <Link to={'/'}>smartEd</Link>
      </h1>
      <NavBar />
    </header>
  );
};

export default Header;
