import { useForm } from 'react-hook-form';
import Input from '../../components/forms/Input';
import useApiMutation from '../../hooks/useApiMutation';
import { toast } from 'react-toastify';
import { Button } from 'antd';
import useAuthState from '../../hooks/useAuth';

const RegisterTeacherProfile = () => {
  const { user } = useAuthState();
  const {
    register,
    handleSubmit,
    formState: { errors },
    reset,
  } = useForm({
    defaultValues: {
      phone_number: '',
      date_of_birth: '',
      gender: '',
      street_address: '',
      city: '',
      state: '',
      country: '',
      school_id: user?.school_id,
      user_id: '',
      postal_code: '',
      licence_certificate: '',
      licence_number: '',
    },
  });

  const { mutateAsync } = useApiMutation(['teachers'], 'teachers/');

  const onSubmit = async (data) => {
    //8d972b9b-c174-4773-8169-fb4092517554 vincent
    console.log(data);
    try {
      const res = await mutateAsync(data);
      console.log(res);
    } catch (error) {
      console.log(error);
      toast.error('request failed, please try again');
    }
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <Input
        name={'user_id'}
        label={'user id'}
        error={errors?.user_id}
        register={register}
        options={{
          required: 'please enter user id',
        }}
        className='input'
        placeholder={'user id'}
      />
      <Button htmlType='submit'>create profile</Button>
    </form>
  );
};

export default RegisterTeacherProfile;
