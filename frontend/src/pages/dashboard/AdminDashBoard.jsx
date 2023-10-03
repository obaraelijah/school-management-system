import Header from '../../components/headers/dashboard/Header';
import useApiQuery from '../../hooks/useApiQuery';
import { Tabs, Button, Popconfirm } from 'antd';
import { useState } from 'react';
import { MdDelete, MdModeEdit } from 'react-icons/md';
import UserTable from '../../components/UserTable';
import authRequest from '../../config/requests';
import { toast } from 'react-toastify';

const AdminDashBoard = () => {
  const { data: students, refetch: refetchStudents } = useApiQuery(
    ['students'],
    'students/'
  );

  const { data: teachers } = useApiQuery(['teachers'], 'teachers/');
  const { data: users } = useApiQuery(['users'], 'users/');

  const [activeTab, setActiveTab] = useState('students');

  // delete student record
  const deleteStudent = async (id) => {
    try {
      const res = await authRequest.delete(`students/${id}`);
      if (res.status === 204) {
        toast.success('student deleted!');
        refetchStudents();
      } else {
        toast.error('An error occurred while deleting student');
      }
    } catch (error) {
      console.log(error);
      toast.error('An error occurred');
    }
  };

  // students table columns
  const studentsColumns = [
    {
      title: 'First Name',
      dataIndex: 'user_first_name',
      key: 'user_first_name',
    },
    {
      title: 'Last Name',
      dataIndex: 'user_last_name',
      key: 'user_last_name',
    },
    {
      title: 'Department',
      dataIndex: 'department_name',
      key: 'department_name',
    },
    {
      title: 'Action',
      dataIndex: 'actions',
      render: (_, record) => (
        <div className='flex items-center gap-1'>
          <Popconfirm
            title='delete user'
            description='Are you sure you want to delete this user? this action is irreversible'
            onCancel={(e) => e.stopPropagation()}
            onConfirm={(e) => {
              e.stopPropagation();
              deleteStudent(record.student_id);
            }}
            okButtonProps={{ className: 'bg-red-700' }}
          >
            <Button
              danger
              onClick={(e) => {
                e.stopPropagation();
              }}
              className='border-none flex items-center'
            >
              {' '}
              <MdDelete className='text-xl' />
            </Button>
          </Popconfirm>
          <Button
            onClick={(e) => {
              e.stopPropagation();
              console.log('cl');
            }}
            className='border-none flex items-center'
          >
            {' '}
            <MdModeEdit className='text-xl' />
          </Button>
        </div>
      ),
    },
  ];

  // teacher's table column
  const teacherColumns = [
    {
      title: 'First Name',
      dataIndex: 'user_first_name',
      key: 'user_first_name',
    },
    {
      title: 'Last Name',
      dataIndex: 'user_last_name',
      key: 'user_last_name',
    },
    {
      title: 'Departments',
      dataIndex: 'department',
      key: 'department',
      render: (_, { department }) => {
        {
          department?.map((dep) => <span key={dep}>{dep}</span>);
        }
      },
    },
  ];
  // users table columns
  const usersColumns = [
    {
      title: 'First Name',
      dataIndex: 'first_name',
      key: 'first_name',
    },
    {
      title: 'Last Name',
      dataIndex: 'last_name',
      key: 'last_name',
    },
    {
      title: 'Email',
      dataIndex: 'email',
      key: 'email',
    },
    {
      title: 'Role',
      dataIndex: 'role_name',
      key: 'role_name',
    },
  ];

  return (
    <>
      <Header />
      <Tabs
        activeKey={activeTab}
        onChange={(activeKey) => setActiveTab(activeKey)}
        items={[
          {
            label: 'students',
            key: 'students',
            children: (
              <UserTable
                columns={studentsColumns}
                data={students?.data}
                route={'/dashboard/student/'}
                rowKey={'student_id'}
              />
            ),
          },
          {
            label: 'teachers',
            key: 'teachers',
            children: (
              <UserTable
                columns={teacherColumns}
                data={teachers?.data}
                rowKey={'user_id'}
                route={''}
              />
            ),
          },
          {
            label: 'users',
            key: 'users',
            children: (
              <UserTable
                columns={usersColumns}
                data={users?.data}
                route={''}
                rowKey={'id'}
              />
            ),
          },
        ]}
      />
    </>
  );
};

export default AdminDashBoard;
