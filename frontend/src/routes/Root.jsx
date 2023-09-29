import { Route } from 'react-router-dom';
import App from '../App.jsx';
import Home from '../pages/landing_pge/Home.jsx';
import SignUp from '../pages/auth/SignUp.jsx';
import LogIn from '../pages/auth/Login.jsx';
import About from '../pages/about/About.jsx';
import Contact from '../pages/contact/Contact.jsx';
import DashboardLayout from '../components/layouts/DashboardLayout.jsx';
import AdminDashBoard from '../pages/dashboard/AdminDashBoard.jsx';
import RootLayout from '../components/layouts/RootLayout.jsx';
import Admin from '../pages/admin/Admin.jsx';
import StudentDashboard from '../pages/students/StudentDashboard.jsx';
import RequireAuth from '../components/RequireAuth.jsx';
import Settings from '../pages/settings/Settings.jsx';
import NotFound from '../pages/error/NotFound.jsx';
import SchoolDetails from '../pages/admin/components/SchoolDetails.jsx';
import RegisterUser from '../pages/roles/RegisterUser.jsx';
import StudentDetails from '../pages/students/components/StudentDetails.jsx';
import Departments from '../pages/dashboard/Departments.jsx';

const Root = (
  <Route path='/' element={<App />} errorElement={<NotFound />}>
    {/* unauthenticated routes */}
    <Route element={<RootLayout />}>
      <Route index element={<Home />} />
      <Route path='signup' element={<SignUp />} />
      <Route path='login' element={<LogIn />} />

      <Route path='/about' element={<About />} />
      <Route path='/contact' element={<Contact />} />
    </Route>

    {/* authenticted routes */}
    <Route
      element={
        <RequireAuth
          allowedRoles={['schooladmin', 'student', 'teacher', 'superuser']}
        />
      }
    >
      <Route path='dashboard' element={<DashboardLayout />}>
        {/* student allowed routes */}
        <Route path='student' element={<StudentDashboard />} />

        <Route path='student/:id' element={<StudentDetails />} />

        {/* end */}
        <Route
          element={<RequireAuth allowedRoles={['schooladmin', 'superuser']} />}
        >
          <Route path='register' element={<RegisterUser />} />

          {/* school admin allowed routes */}
          <Route
            path='schooladmin'
            element={<RequireAuth allowedRoles={['schooladmin']} />}
          >
            <Route index element={<AdminDashBoard />} />
            <Route path='departments' element={<Departments />} />
          </Route>
          {/* end */}

          {/* super admin routes */}
          <Route
            path='superuser'
            element={<RequireAuth allowedRoles={['superuser']} />}
          >
            <Route index element={<Admin />} />
            <Route path='new_school' element={<SchoolDetails />} />
          </Route>
          {/* end */}
        </Route>
        <Route path='settings' element={<Settings />} />
      </Route>
    </Route>
  </Route>
);

export default Root;
