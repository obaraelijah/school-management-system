import { Outlet } from 'react-router-dom';
import { ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import { AnimatePresence } from 'framer-motion';

function App() {
  return (
    <AnimatePresence>
      <ToastContainer />
      <Outlet />
    </AnimatePresence>
  );
}

export default App;
