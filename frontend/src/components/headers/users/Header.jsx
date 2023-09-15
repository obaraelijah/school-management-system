import Logo from '../../Logo';
import NavBar from '../../nav/NavBar';
import Hero from './Hero';

const Header = () => {
  return (
    <header className='flex p-3 bg-btn text-white h-screen flex-col'>
      <div className='flex justify-between w-full py-5'>
        <Logo />
        <NavBar />
      </div>
      <Hero />
    </header>
  );
};

export default Header;
