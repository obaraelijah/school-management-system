import { Route } from 'react-router-dom';
import App from '../App.jsx';
import Home from '../pages/landing_pge/Home.jsx';
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
import Courses from '../pages/dashboard/Courses.jsx';
import ViewCourse from '../pages/dashboard/components/ViewCourse.jsx';
import CourseMaterials from '../pages/course-materials/CourseMaterials.jsx';
import ForgotPassword from '../pages/auth/ForgotPassword.jsx';
import ResetPassword from '../pages/auth/ResetPassword.jsx';
import ConfirmEmail from '../pages/auth/ConfirmEmail.jsx';
import TeacherDetails from '../pages/teachers/TeacherDetails.jsx';

const Root = (
  <Route path='/' element={<App />} errorElement={<NotFound />}>
    {/* unauthenticated routes */}
    <Route element={<RootLayout />}>
      <Route index element={<Home />} />
      <Route path='login' element={<LogIn />} />
      <Route path='forgot_password' element={<ForgotPassword />} />
      <Route path='confirm_email' element={<ConfirmEmail />} />
      <Route path='reset_password' element={<ResetPassword />} />
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
        <Route
          path='student'
          element={
            <RequireAuth
              allowedRoles={['student', 'superuser', 'schooladmin']}
            />
          }
        >
          <Route index element={<StudentDashboard />} />

          <Route path=':id' element={<StudentDetails />} />
        </Route>
        {/* end */}

        {/* teacher allowed routes */}
        <Route
          path='teacher'
          element={
            <RequireAuth
              allowedRoles={['teacher', 'superuser', 'schooladmin']}
            />
          }
        >
          {/* <Route index element={<TeacherDashboard />} /> */}

          <Route path=':id' element={<TeacherDetails />} />
        </Route>
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
            <Route path='courses' element={<Courses />} />
            <Route path='courses/:id' element={<ViewCourse />} />
            <Route path='materials' element={<CourseMaterials />} />
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
