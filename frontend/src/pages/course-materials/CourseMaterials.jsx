import { useSearchParams } from 'react-router-dom';
import useAuthState from '../../hooks/useAuth';
import { useState } from 'react';
import useApiQuery from '../../hooks/useApiQuery';
import authRequest from '../../config/requests';
import { toast } from 'react-toastify';
import { Button, Popconfirm, Tabs } from 'antd';
import { MdDelete, MdModeEdit } from 'react-icons/md';
import UserTable from '../../components/UserTable';
import EditModal from '../../components/modals/EditModal';
import { BiSolidDownload } from 'react-icons/bi';

const CourseMaterials = () => {
  const { user } = useAuthState();
  const [searchParams, setParams] = useSearchParams({
    tab: 'all',
    modal: false,
  });
  const [record, setRecord] = useState(null);

  const activeTab = searchParams.get('tab');
  const isModalOpen = searchParams.get('modal') === 'true';

  const { data: materials, refetch } = useApiQuery(
    ['materials'],
    'course-materials/'
  );

  console.log(materials);

  // new course default from values

  const defaultValues = {
    course_name: '',
    course_code: '',
    course_description: '',
    course_credit: '',
    course_duration: '',
    departments: [],
    school_id: user?.school_id,
  };

  // edit course default form values
  const editDefaultValues = {
    course_name: record?.course_name,
    course_code: record?.course_code,
    course_description: record?.course_description,
    course_credit: record?.course_credit,
    course_duration: record?.course_duration,
    departments: record?.departments,
    school_id: user.school_id,
  };

  // handle course delete
  const deleteCourse = async (id) => {
    try {
      const res = await authRequest.delete(`courses/${id}/`);
      if (res.status === 204) {
        toast.success('course deleted!');
        refetch();
      } else {
        toast.error('An error occurred while deleting course');
      }
    } catch (error) {
      console.log(error);
      toast.error('An error occurred');
    }
  };

  //handle modal close
  const closeModal = () => {
    console.log('function');
    setParams((prev) => {
      prev.delete('modal');
      return prev;
    });
  };

  // table columns for courses
  const columns = [
    {
      title: 'Course name',
      dataIndex: 'course_name',
      key: 'course_name',
    },
    {
      title: 'Course Material Name',
      dataIndex: 'course_material_name',
      key: 'course_material_name',
    },
    {
      title: 'Download',
      dataIndex: 'course_material_file',
      key: 'course_material_file',
      render: (file) => {
        return (
          <a href={file} download onClick={(e) => e.stopPropagation()}>
            <BiSolidDownload />
          </a>
        );
      },
    },
    {
      title: 'Action',
      dataIndex: 'actions',
      render: (_, record) => (
        <div className='flex items-center gap-1'>
          <Popconfirm
            title='delete course'
            description='Are you sure you want to delete this course? this action is irreversible'
            onCancel={(e) => e.stopPropagation()}
            onConfirm={(e) => {
              e.stopPropagation();
              deleteCourse(record.course_id);
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
              setParams((prev) => {
                prev.set('modal', true);
                return prev;
              });
              setRecord(record);
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

  return (
    <div className=''>
      <h2 className='font-semibold text-3xl capitalize pb-4'>
        course materials
      </h2>
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
                data={materials?.data}
                route={''}
                type={'materials'}
                rowKey={'course_material_id'}
                allowClick={true}
              />
            ),
          },
          {
            label: 'New',
            key: 'new',
          },
        ]}
      />

      <EditModal
        isModalOpen={isModalOpen}
        handleSubmit={closeModal}
        handleClose={closeModal}
      >
        <h3 className='font-semibold'>Edit course material</h3>
        {/* <NewCourse defaultValues={editDefaultValues} id={record?.course_id} /> */}
      </EditModal>
    </div>
  );
};

export default CourseMaterials;
