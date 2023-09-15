import { Routes, Route } from 'react-router-dom';
import Home from './pages/landing_pge/Home';
import SignUp from './pages/auth/SignUp';
import LogIn from './pages/auth/Login';
import RootLayout from './components/layouts/RootLayout';
import DashboardLayout from './components/layouts/DashboardLayout';
import DashBoard from './pages/dashboard/DashBoard';
import { ToastContainer } from 'react-toastify';
import AdminLayout from './components/layouts/AdminLayout';
import Admin from './pages/admin/Admin';
import SchoolInfo from './pages/admin/components/SchoolInfo';

function App() {
  return (
    <>
      <ToastContainer />
      <Routes>
        <Route element={<RootLayout />}>
          <Route index element={<Home />} />
          <Route path='signup' element={<SignUp />} />
          <Route path='login' element={<LogIn />} />
        </Route>

        <Route path='dashboard' element={<DashboardLayout />}>
          <Route index element={<DashBoard />} />
        </Route>
        <Route path='admin' element={<AdminLayout />}>
          <Route index element={<Admin />} />
          <Route path='new-school' element={<SchoolInfo />} />
        </Route>
      </Routes>
    </>
  );
}

export default App;
