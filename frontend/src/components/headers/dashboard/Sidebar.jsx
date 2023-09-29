import { NavLink, useNavigate } from 'react-router-dom';
import { AiOutlineHome } from 'react-icons/ai';
import { IoSettingsOutline } from 'react-icons/io5';
import { TbLogout2 } from 'react-icons/tb';
import { GiArchiveRegister } from 'react-icons/gi';
import { FcDepartment } from 'react-icons/fc';
import Logo from '../../Logo';
import Button from '../../Button';
import useAuthState from '../../../hooks/useAuth';

const Sidebar = () => {
  const { user, setUser } = useAuthState();
  const role = user?.role.toLowerCase();
  const superAdmin = role === 'superuser';
  const admin = role === 'schooladmin';
  const admins = admin || superAdmin;
  //const teacher = role === 'teacher';
  //const student = role ==='student';
  const navigate = useNavigate();
  const handleSignOut = () => {
    setUser(null);
    localStorage.removeItem('auth');
    navigate('/login');
  };

  return (
    <aside className='h-full bg-header   text-white md:w-3/12 mx-auto'>
      <div className='hidden  w-full py-8 h-full md:flex flex-col'>
        <Logo />
        <nav className='md:py-10'>
          <ul className='flex gap-7 flex-col justify-center'>
            <li>
              <NavLink
                to={`/dashboard/${role}`}
                className={`${({ isActive }) =>
                  isActive ? 'dashboard-active' : ''} dashboard-link`}
              >
                <AiOutlineHome className='icon' />
                dashboard
              </NavLink>
            </li>
            {/* superuser and school admins have access */}
            {admins && (
              <>
                <li>
                  <NavLink
                    to={`/dashboard/register?tab=user`}
                    className={`${({ isActive }) =>
                      isActive ? 'bg-active' : ''}  dashboard-link`}
                  >
                    <GiArchiveRegister className='icon' />
                    register user
                  </NavLink>
                </li>
              </>
            )}

            {admin && (
              <>
                <li>
                  <NavLink
                    to={`/dashboard/schooladmin/departments?tab=all`}
                    className={`${({ isActive }) =>
                      isActive ? 'bg-active' : ''}  dashboard-link`}
                  >
                    <FcDepartment className='icon' />
                    departments
                  </NavLink>
                </li>
              </>
            )}

            {superAdmin && (
              <>
                <li>
                  <NavLink
                    to={'/dashboard/superuser/new_school/'}
                    className={`${({ isActive }) =>
                      isActive ? 'dashboard-active' : ''} dashboard-link`}
                  >
                    register school
                  </NavLink>
                </li>
              </>
            )}
            <li>
              <NavLink
                to={'/dashboard/settings'}
                className={`${({ isActive }) =>
                  isActive ? 'dashboard-active' : ''} dashboard-link`}
              >
                <IoSettingsOutline />
                settings
              </NavLink>
            </li>
          </ul>
        </nav>

        <Button
          className={
            'mt-auto px-12 w-full py-2 rounded-sm flex items-center gap-2 font-bold text-base capitalize text-cm-orange-100'
          }
          onClick={handleSignOut}
        >
          <TbLogout2 /> sign out
        </Button>
      </div>

      {/* mobile nav */}
      <div className='py-3 md:hidden'>
        <Logo />
      </div>

      <div className='fixed z-50 bottom-0 flex md:hidden bg-header w-full py-3 px-4 overflow-x-scroll text-white'>
        <nav>
          <ul className='flex  justify-center items-center capitalize'>
            <li>
              <NavLink
                to={'/dashboard/admin'}
                className={`${({ isActive }) =>
                  isActive ? 'dashboard-active' : ''} dashboard-link`}
              >
                <AiOutlineHome className='icon' />
                dashboard
              </NavLink>
            </li>
            {admin && (
              <>
                <li>
                  <NavLink
                    to={'/dashboard/new-teacher'}
                    className={`${({ isActive }) =>
                      isActive ? 'dashboard-active' : ''} dashboard-link`}
                  >
                    register teacher
                  </NavLink>
                </li>
                <li>
                  <NavLink
                    to={'/dashboard/new-student'}
                    className={`${({ isActive }) =>
                      isActive ? 'dashboard-active' : ''} dashboard-link`}
                  >
                    register student
                  </NavLink>
                </li>
              </>
            )}

            {superAdmin && (
              <>
                <li>
                  <NavLink
                    to={'/dashboard/superuser/new_school'}
                    className={`${({ isActive }) =>
                      isActive ? 'dashboard-active' : ''} dashboard-link`}
                  >
                    register school
                  </NavLink>
                </li>
                <li>
                  <NavLink
                    to={'/dashboard/superuser/new_admin'}
                    className={`${({ isActive }) =>
                      isActive ? 'dashboard-active' : ''} dashboard-link`}
                  >
                    school admin
                  </NavLink>
                </li>
              </>
            )}
            <li>
              <NavLink
                to={'/dashboard/settings'}
                className={`${({ isActive }) =>
                  isActive ? 'dashboard-active' : ''} dashboard-link`}
              >
                <IoSettingsOutline />
                settings
              </NavLink>
            </li>
          </ul>
        </nav>
      </div>
    </aside>
  );
};

export default Sidebar;
