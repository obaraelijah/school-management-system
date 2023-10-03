import { useParams } from 'react-router-dom';
import useApiQuery from '../../../hooks/useApiQuery';

const StudentDetails = () => {
  const { id } = useParams();
  const { data } = useApiQuery([`students`, id], `students/${id}/`);
  console.log(data);
  return (
    <div className='bg-red-900 py-5'>
      StudentDetails <h2>hello world</h2>
    </div>
  );
};

export default StudentDetails;
