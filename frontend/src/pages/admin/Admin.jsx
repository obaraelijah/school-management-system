import { useState } from 'react';
import Header from '../../components/headers/dashboard/Header';
import useApiQuery from '../../hooks/useApiQuery';
import { List, Tabs } from 'antd';

const SuperAdmin = () => {
  // tabs state
  const [activeKey, setActiveKey] = useState('schools');
  const { data: schools } = useApiQuery(['schools'], 'schools/');
  const { data: users } = useApiQuery(['users'], 'users/');
  console.log(users);
  return (
    <div>
      <Header />
      <Tabs
        activeKey={activeKey}
        onChange={(activeKey) => setActiveKey(activeKey)}
      >
        <Tabs.TabPane key={'schools'} tab='Schools' />
        <Tabs.TabPane key={'users'} tab='Users' />
      </Tabs>
      {activeKey === 'schools' ? (
        <List
          itemLayout='vertical'
          size='large'
          pagination={{
            onChange: (page) => page,
            pageSize: 15,
            align: 'center',
          }}
          dataSource={schools?.data}
          renderItem={(item) => (
            <List.Item key={item?.school_id}>
              <div className='grid grid-cols-7 items-center'>
                <img
                  src={item.school_logo}
                  alt='school logo'
                  className='rounded-full w-1/3 col-span-1'
                />
                <h2 className='col-span-2'>{item.school_name}</h2>
                <p className='col-span-3'>{item.school_id}</p>
              </div>
            </List.Item>
          )}
        />
      ) : (
        <List
          itemLayout='vertical'
          size='large'
          pagination={{
            onChange: (page) => page,
            pageSize: 15,
            align: 'center',
          }}
          dataSource={users?.data}
          renderItem={(item) => (
            <List.Item key={item?.id}>
              <div className='grid grid-cols-7 items-center'>
                <h2 className='col-span-2'>
                  {item.first_name} {item.last_name}
                </h2>
                <p className='col-span-3'>{item.role_name}</p>
                <p>{item.school_name}</p>
              </div>
            </List.Item>
          )}
        />
      )}
    </div>
  );
};

export default SuperAdmin;
