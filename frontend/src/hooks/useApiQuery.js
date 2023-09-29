import authRequest from '../config/requests';
import { useQuery } from '@tanstack/react-query';
//import getNewToken from '../utils/getNewToken';

const useApiQuery = (queryKey, endpoint) => {
  const results = useQuery({
    queryKey,
    queryFn: async () => {
      const response = await authRequest.get(endpoint);
      return response?.data;
    },
    onError: (err) => {
      console.log('err', err);
      return err;
    },
  });
  return results;
};

export default useApiQuery;
