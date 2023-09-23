import useApiQuery from '../../hooks/useApiQuery';
//import { Spinner } from '@chakra-ui/react';
import Header from '../../components/headers/dashboard/Header';
import useAuthState from '../../hooks/useAuth';

const AdminDashBoard = () => {
  const { user } = useAuthState();
  const { data } = useApiQuery(['schools'], 'schools/');
  console.log('school', data);
  console.log('user', user);
  return (
    <>
      <Header />
    </>
  );
};

export default AdminDashBoard;
