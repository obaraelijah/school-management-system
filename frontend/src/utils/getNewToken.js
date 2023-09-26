import axios from 'axios';
import { baseUrl } from '../consts';

const fetchToken = async () => {
  const auth = JSON.parse(localStorage.getItem('auth'));
  try {
    const res = await axios.post(`${baseUrl}refresh_token/`, {
      refresh: auth.refresh,
    });

    const token = await res.data;
    const new_auth = { ...auth, access: token.access };
    localStorage.setItem('auth', JSON.stringify(new_auth));
  } catch (error) {
    console.log(error.detail);
  }
};

export default fetchToken;
