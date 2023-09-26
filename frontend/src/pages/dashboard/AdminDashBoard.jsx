import Header from '../../components/headers/dashboard/Header';
import useApiQuery from '../../hooks/useApiQuery';
import { List, Tabs, Table, Space } from 'antd';
import { useState } from 'react';

const AdminDashBoard = () => {
  const { data: students } = useApiQuery(['students'], 'students/');
  const { data: teachers } = useApiQuery(['teachers'], 'teachers/');

  const [activeTab, setActiveTab] = useState('students');

  const studentsColumns = [
    {
      title: 'First Name',
      dataIndex: 'user_first_name',
      key: 'first_name',
    },
    {
      title: 'Last Name',
      dataIndex: 'user_last_name',
      key: 'last_name',
    },
    {
      title: 'Department',
      dataIndex: 'department_name',
      key: 'department_name',
    },
  ];
  const teacherColumns = [
    {
      title: 'First Name',
      dataIndex: 'user_first_name',
      key: 'first_name',
    },
    {
      title: 'Last Name',
      dataIndex: 'user_last_name',
      key: 'last_name',
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

  console.log(teachers);
  return (
    <>
      <Header />
      <Tabs
        activeKey={activeTab}
        onChange={(activeKey) => setActiveTab(activeKey)}
      >
        <Tabs.TabPane key={'students'} tab='Students' />
        <Tabs.TabPane key={'teachers'} tab='Teachers' />
      </Tabs>

      {activeTab === 'students' ? (
        <Table
          columns={studentsColumns}
          dataSource={students?.data}
          pagination={{ position: ['bottomCenter'], pageSize: 15 }}
        />
      ) : (
        <Table columns={teacherColumns} dataSource={teachers?.data} />
      )}
    </>
  );
};

export default AdminDashBoard;
