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
import RegisterTeacher from '../pages/roles/RegisterTeacher.jsx';
import RegisterStudent from '../pages/roles/RegisterStudent.jsx';
import RegisterAdmin from '../pages/roles/RegisterAdmin.jsx';
import NotFound from '../pages/error/NotFound.jsx';
import SchoolDetails from '../pages/admin/components/SchoolDetails.jsx';

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
          allowedRoles={['admin', 'student', 'teacher', 'superuser']}
        />
      }
    >
      <Route path='dashboard' element={<DashboardLayout />}>
        {/* student allowed routes */}
        <Route path='student' element={<StudentDashboard />} />

        {/* end */}

        {/* school admin allowed routes */}
        <Route path='admin' element={<RequireAuth allowedRoles={['admin']} />}>
          <Route index element={<AdminDashBoard />} />
          <Route path='new_teacher' element={<RegisterTeacher />} />
          <Route path='new_student' element={<RegisterStudent />} />
        </Route>
        {/* end */}

        {/* super admin routes */}
        <Route
          path='superuser'
          element={<RequireAuth allowedRoles={['superuser']} />}
        >
          <Route index element={<Admin />} />
          <Route path='new_admin' element={<RegisterAdmin />} />
          <Route path='new_school' element={<SchoolDetails />} />
        </Route>
        {/* end */}
        <Route path='settings' element={<Settings />} />
      </Route>
    </Route>
  </Route>
);

export default Root;
