import { useState } from 'react';
import authRequest from '../config/requests';
import Input from './forms/Input';
import { useForm } from 'react-hook-form';
import { toast } from 'react-toastify';
import { Modal, Button as AntButton } from 'antd';
import { AiOutlineSend } from 'react-icons/ai';
import { Typography } from 'antd';
import { MdContentCopy, MdOutlineCheckCircle } from 'react-icons/md';
import useAuthState from '../hooks/useAuth';
import useApiQuery from '../hooks/useApiQuery';

const NewUser = () => {
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [roleId, setRoleId] = useState('');
  const [isNewRole, setIsNewRole] = useState(false);

  const { Paragraph, Title } = Typography;

  const { data: roles } = useApiQuery(['roles'], 'roles/');

  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm({
    defaultValues: {
      role_name: '',
    },
  });

  const { user } = useAuthState();
  const isSchoolAdmin = user.role_name.toLowerCase() === 'schooladmin';
  const {
    register: registerUser,
    handleSubmit: handleUserSubmit,
    formState: { errors: Errors },
    watch,
    reset,
  } = useForm({
    defaultValues: {
      first_name: '',
      last_name: '',
      email: '',
      password: '',
      role_id: '',
      school_id: '',
      confirm_password: '',
    },
  });

  // handle new role creation
  const onSubmit = async (data) => {
    try {
      const res = await authRequest.post('roles/', data);
      if (res.status === 201) {
        toast.success('role id created successfully!');
        setRoleId(res.data.data.role_id);
      } else {
        toast.error('error creating role!');
      }
    } catch (error) {
      console.log(error);
      toast.error('An error occurred');
    }
  };

  // handle new user creation
  const createUser = async (data) => {
    try {
      const res = await authRequest.post('auth/sign_up/', data);
      console.log(res);
      if (res.status === 201) {
        setIsModalOpen(true);
        reset();
      } else {
        toast.error('error registering user');
      }
    } catch (error) {
      toast.error(error.detail);
    }
  };

  // handle utton toggle for new role name creation
  const toggleButton = () => {
    setIsNewRole((prev) => !prev);
  };

  return (
    <>
      <Modal
        open={isModalOpen}
        onCancel={() => setIsModalOpen(false)}
        footer={[
          <AntButton key={'ok'} onClick={() => setIsModalOpen(false)}>
            ok
          </AntButton>,
        ]}
        centered={true}
        confirmLoading={true}
      >
        <p>user created successfully!</p>
      </Modal>
      {/* {roleId && (
        <>
          <div>
            <Title>role id:</Title>
            <Paragraph
              copyable={{
                icon: [
                  <MdContentCopy key={'copy-icon'} />,
                  <MdOutlineCheckCircle key={'copied-icon'} />,
                ],
                tooltips: ['click here to copy', 'copied!'],
              }}
            >
              {roleId}
            </Paragraph>
          </div>
          {isSchoolAdmin
            ? AiOutlineSend(
                <div>
                  <Title>school id:</Title>
                  <Paragraph
                    copyable={{
                      icon: [
                        <MdContentCopy key={'copy-icon'} />,
                        <MdOutlineCheckCircle key={'copied-icon'} />,
                      ],
                      tooltips: ['click here to copy', 'copied!'],
                    }}
                  >
                    {user.school_id}
                  </Paragraph>
                </div>
              )
            : null}
        </>
      )} */}

      <div
        className={`flex flex-col justify-center px-5 md:px-10 py-4 rounded-md my-5 ${
          isNewRole && 'border'
        }`}
      >
        <AntButton
          className={`self-end transition transform ease-in-out duration-75 ${
            isNewRole && 'text-red-500 border-red-500'
          }`}
          onClick={toggleButton}
        >
          {isNewRole ? 'close' : 'create role name'}
        </AntButton>

        {isNewRole && (
          <form onSubmit={handleSubmit(onSubmit)}>
            <Input
              name='role_name'
              register={register}
              error={errors.role_name}
              options={{
                required: 'please provide a role name',
              }}
              placeholder={isSchoolAdmin ? 'student or teacher' : 'schooladmin'}
              className={'input'}
              label={'role name:'}
            />
            <AntButton htmlType='submit'>submit</AntButton>
          </form>
        )}
      </div>
      <form onSubmit={handleUserSubmit(createUser)}>
        <div className='flex flex-col md:flex-row gap-3'>
          <Input
            name='first_name'
            register={registerUser}
            className={'input'}
            error={Errors.first_name}
            label={'first name'}
            options={{
              required: 'please provide first name',
            }}
            placeholder={'first name'}
          />

          <Input
            name='last_name'
            register={registerUser}
            className={'input'}
            error={Errors.last_name}
            label={'last name'}
            options={{
              required: 'please provide last name',
            }}
            placeholder={'last name'}
          />
        </div>
        <Input
          name='email'
          register={registerUser}
          className={'input border w-full'}
          error={Errors.email}
          label={'email'}
          options={{
            required: '',
            pattern: {
              value: /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}$/i,
              message: 'enter a valid email',
            },
          }}
          placeholder={'enter email address'}
          type='email'
        />

        <div className='flex flex-col md:flex-row gap-3'>
          <Input
            name='password'
            register={registerUser}
            className={'input'}
            error={Errors.password}
            label={'password'}
            options={{
              required: 'please provide password',
            }}
            placeholder={'*******'}
            type='password'
          />
          <Input
            name='confirm_password'
            register={registerUser}
            className={'input'}
            error={Errors.confirm_password}
            label={'confirm password'}
            options={{
              required: true,
              validate: (val) => {
                if (watch('password') !== val) {
                  return 'passwords do not match';
                }
              },
            }}
            placeholder={'*******'}
            type='password'
          />
        </div>
        <div className='flex flex-col md:flex-row gap-3'>
          <Input
            name='role_id'
            register={registerUser}
            className={'input'}
            error={Errors.role_id}
            label={'role id'}
            options={{
              required: 'please provide role id above',
            }}
            placeholder={'enter role id'}
          />
          <Input
            name='school_id'
            register={registerUser}
            className={'input'}
            error={Errors.school_id}
            label={'school id'}
            options={{
              required: 'please provide school id',
            }}
            placeholder={'enter school id'}
          />
        </div>
        <AntButton
          htmlType='submit'
          icon={<AiOutlineSend />}
          className='flex items-center'
          size='middle'
          type='default'
          loading=''
        >
          submit
        </AntButton>
      </form>
    </>
  );
};

export default NewUser;
