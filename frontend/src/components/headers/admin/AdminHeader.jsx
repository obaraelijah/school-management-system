import AdminNav from '../../nav/AdminNav';
import Logo from '../../Logo';

const AdminHeader = () => {
  return (
    <header className='md:p-5 bg-header text-white flex flex-col items-start justify-start gap-5'>
      <Logo />
      <AdminNav />
    </header>
  );
};

export default AdminHeader;
