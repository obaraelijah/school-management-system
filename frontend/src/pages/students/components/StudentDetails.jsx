import { useParams } from 'react-router-dom';
import useApiQuery from '../../../hooks/useApiQuery';

const StudentDetails = () => {
  const { id } = useParams();
  const { data } = useApiQuery([`students`, id], `students/${id}/`);
  console.log(data);
  return <div>StudentDetails</div>;
};

export default StudentDetails;
