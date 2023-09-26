import PropTypes from 'prop-types';
import { createContext, useEffect, useState } from 'react';
import fetchUser from '../utils/fetchUser';
import getUserIdFromToken from '../utils/getUserId';

const AuthContext = createContext(null);

export const AuthStateProvider = ({ children }) => {
  const user_id = getUserIdFromToken();
  const [user, setUser] = useState(null);

  useEffect(() => {
    if (user_id) {
      fetchUser(user_id).then((res) => setUser(res));
    }
  }, []);

  return (
    <AuthContext.Provider value={{ user, setUser }}>
      {children}
    </AuthContext.Provider>
  );
};

AuthStateProvider.propTypes = {
  children: PropTypes.node,
};

export default AuthContext;
