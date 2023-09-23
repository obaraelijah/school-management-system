import axios from 'axios';
import { baseUrl } from '../consts';

const fetchToken = async () => {
  // fetch(`${baseUrl}refresh_token/`, {
  //   method: 'POST',
  //   headers: {
  //     'content-type': 'application/json',
  //   },
  //   body: JSON.stringify({ refresh: token.refresh }),
  // })
  //   .then((res) => res.json())
  //   .then((da) => localStorage.setItem('token', da.access))
  //   .catch((err) => console.log(err));
  // return;

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
