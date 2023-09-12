import { Routes, Route } from 'react-router-dom';
import Home from './pages/landing_pge/Home';
import Signup from './pages/signup/Signup';
import Login from './pages/login/Login';
import RootLayout from './components/layouts/RootLayout';
import DashboardLayout from './components/layouts/DashboardLayout';
import DashBoard from './pages/dashboard/DashBoard';

function App() {
  return (
    <>
      <Routes>
        <Route element={<RootLayout />}>
          <Route index element={<Home />} />
          <Route path='signup' element={<Signup />} />
          <Route path='login' element={<Login />} />
        </Route>

        <Route path='dashboard' element={<DashboardLayout />}>
          <Route index element={<DashBoard />} />
        </Route>
      </Routes>
    </>
  );
}

export default App;
