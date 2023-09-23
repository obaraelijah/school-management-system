import { useState } from 'react';
import authRequests from '../../config/requests';
import Input from '../../components/forms/Input';
import { useForm } from 'react-hook-form';
import { Button } from '@chakra-ui/react';
import { toast } from 'react-toastify';

const RegisterAdmin = () => {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm({
    defaultValues: {
      role_name: '',
    },
  });

  const {
    register: registerAdmin,
    handleSubmit: handleAdminSubmit,
    formState: { errors: AdminErrors },
  } = useForm({
    defaultValues: {
      first_name: '',
      last_name: '',
      email: '',
      password: ' ',
      role_id: '',
    },
  });

  const [roleId, setRoleId] = useState('');
  // useEffect(() => {
  //   roles();
  // }, []);
  // const roles = async () => {
  //   const res = await authRequests.get('roles/');
  //   console.log(res);
  // };

  // school_admmin : "e443bc5c-59a1-4518-ac22-695c3842338b"
  const onSubmit = async (data) => {
    console.log(data);
    try {
      const res = await authRequests.post('roles/', data);
      if (res.status === 201) {
        toast.success('admin role created successfully!');
        setRoleId(res.data.data.role_id);
      } else {
        toast.error('error!');
      }
    } catch (error) {
      console.log(error);
    }
  };

  const createUser = async (data) => {
    try {
      const res = await authRequests.post('auth/sign_up/', data);
      console.log(res);
      console.log('here');
      if (res.status === 201) {
        toast.success('admin user created successfully');
      } else {
        toast.error('error!');
      }
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <div>
      <h2>RegisterAdmin</h2>
      {roleId && <p>{roleId}</p>}
      <form onSubmit={handleSubmit(onSubmit)}>
        <Input
          name='role_name'
          register={register}
          error={errors.role_name}
          options={{
            required: 'please enter role name',
          }}
          placeholder={'role name '}
        />
        <Button type='submit'>submit</Button>
      </form>

      {roleId && (
        <form onSubmit={handleAdminSubmit(createUser)}>
          <Input
            name='first_name'
            register={registerAdmin}
            className={'input'}
            error={AdminErrors.first_name}
            label={'first name'}
            options={{
              required: 'please provide first name',
            }}
            placeholder={'first name'}
          />

          <Input
            name='last_name'
            register={registerAdmin}
            className={'input'}
            error={AdminErrors.last_name}
            label={'last name'}
            options={{
              required: 'please provide last name',
            }}
            placeholder={'last name'}
          />

          <Input
            name='email'
            register={registerAdmin}
            className={'input border w-full'}
            error={AdminErrors.email}
            label={'email'}
            options={{
              required: '',
              pattern: {
                value: /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}$/i,
                message: 'enter a valid email',
              },
            }}
            placeholder={'enter email address'}
          />

          <Input
            name='password'
            register={registerAdmin}
            className={'input'}
            error={AdminErrors.password}
            label={'password'}
            options={{
              required: 'please provide password',
            }}
            placeholder={'first name'}
          />

          <Input
            name='role_id'
            register={registerAdmin}
            className={'input'}
            error={AdminErrors.role_id}
            label={'role id'}
            options={{
              required: 'please provide role id above',
            }}
            placeholder={'enter role id'}
          />
          <Button type='submit'>submit</Button>
        </form>
      )}
    </div>
  );
};

export default RegisterAdmin;
