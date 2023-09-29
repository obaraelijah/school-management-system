import { Tabs } from 'antd';
import { useSearchParams } from 'react-router-dom';
import UserTable from '../../components/UserTable';
import useApiQuery from '../../hooks/useApiQuery';
import NewDepartment from './components/NewDepartment';

const Departments = () => {
  const [searchParams, setParams] = useSearchParams({ tab: 'all' });
  const activeTab = searchParams.get('tab');

  const { data: departments } = useApiQuery(['departments'], 'departments/');

  // table columns for departments
  const columns = [
    {
      title: 'Name',
      dataIndex: 'department_name',
      key: 'departmet_name',
    },
    {
      title: 'Id',
      dataIndex: 'department_id',
      key: 'departmet_id',
    },
  ];

  return (
    <div>
      <h2>Departments</h2>
      <Tabs
        activeKey={activeTab}
        onChange={(activeKey) =>
          setParams(
            (prev) => {
              prev.set('tab', activeKey);
              return prev;
            },
            { replace: true }
          )
        }
        items={[
          {
            label: 'All',
            key: 'all',
            children: (
              <UserTable
                columns={columns}
                data={departments?.data}
                route={''}
                type={'department'}
                rowKey={'department_id'}
                allowClick={false}
              />
            ),
          },
          {
            label: 'New',
            key: 'new',
            children: <NewDepartment />,
          },
        ]}
      />
    </div>
  );
};

export default Departments;
