import React from 'react';
import ReactDOM from 'react-dom/client';
import {
  createBrowserRouter,
  createRoutesFromElements,
  Route,
  RouterProvider,
} from 'react-router-dom';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import App from './App.jsx';
import './index.css';
import Home from './pages/landing_pge/Home.jsx';
import SignUp from './pages/auth/SignUp.jsx';
import LogIn from './pages/auth/Login.jsx';
import About from './pages/about/About.jsx';
import Contact from './pages/contact/Contact.jsx';
import DashboardLayout from './components/layouts/DashboardLayout.jsx';
import DashBoard from './pages/dashboard/DashBoard.jsx';
import SchoolInfo from './pages/admin/components/SchoolInfo.jsx';
import RootLayout from './components/layouts/RootLayout.jsx';
import AdminLayout from './components/layouts/AdminLayout.jsx';
import Admin from './pages/admin/Admin.jsx';

const queryClient = new QueryClient();

const router = createBrowserRouter(
  createRoutesFromElements(
    <Route path='/' element={<App />}>
      <Route element={<RootLayout />}>
        <Route index element={<Home />} />
        <Route path='signup' element={<SignUp />} />
        <Route path='login' element={<LogIn />} />

        <Route path='/about' element={<About />} />
        <Route path='/contact' element={<Contact />} />
      </Route>

      <Route path='dashboard' element={<DashboardLayout />}>
        <Route index element={<DashBoard />} />
      </Route>
      <Route path='admin' element={<AdminLayout />}>
        <Route index element={<Admin />} />
        <Route path='new-school' element={<SchoolInfo />} />
      </Route>
    </Route>
  )
);

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <RouterProvider router={router}>
      <QueryClientProvider client={queryClient}>
        <App />
      </QueryClientProvider>
    </RouterProvider>
  </React.StrictMode>
);
