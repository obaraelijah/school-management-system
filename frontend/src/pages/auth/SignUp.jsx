import Input from '../../components/forms/Input';
import { useForm } from 'react-hook-form';
//import { useState } from 'react';
import { Link } from 'react-router-dom';

const SignUp = () => {
  //const [image, setImage] = useState('');
  const {
    register,
    handleSubmit,
    reset,
    formState: { errors },
  } = useForm({
    defaultValues: {
      schoolName: '',
      address: '',
      email: '',
      phoneNumber: '',
      files: '',
    },
  });

  const convertFile = (file) => {
    const reader = new FileReader();

    reader.onloadend = () => {
      //setImage(reader.result.toString());
    };
    return reader.readAsDataURL(file);
  };

  const onSubmit = (data) => {
    convertFile(data.files[0]);
    reset();
  };

  return (
    <div className='flex flex-col justify-center px-7 items-center lg:items-end lg:pr-20 w-full md:my-5 md:m-0 lg:bg-[url("../src/assets/designer.png")] bg-no-repeat py-10'>
      <p className='self-center'>
        already have an account?{' '}
        <Link to={'/login'} className='text-blue-500'>
          login
        </Link>
      </p>
      <form
        onSubmit={handleSubmit(onSubmit)}
        className=' md:w-2/4 lg:1/3 col-span-2 flex flex-col bg-form px-6 py-3 rounded-md mt-3'
      >
        <Input
          name='schoolName'
          register={register}
          className={'input'}
          error={errors.schoolName}
          label={'school name'}
          options={{
            required: 'please provide school name',
          }}
          placeholder={'enter name of school'}
        />

        <Input
          name='email'
          register={register}
          className={'input border w-full'}
          error={errors.email}
          label={'email'}
          options={{
            required: '',
            pattern: {
              value: /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}$/i,
              message: 'enter a valid email',
            },
          }}
          placeholder={'enter your email address'}
        />

        <Input
          name='address'
          register={register}
          className={'input'}
          error={errors.address}
          label={'school address'}
          options={{
            required: 'please provide school address',
          }}
          placeholder={'enter school'}
        />

        <Input
          name='phoneNumber'
          register={register}
          className={'input'}
          error={errors.phoneNumber}
          label={'phone number'}
          options={{
            required: 'please provide phone number',
          }}
          placeholder={'phone number'}
        />

        <Input
          name='files'
          register={register}
          className={'input'}
          error={errors.files}
          label={'school logo'}
          type={'file'}
        />
        <button type='submit' className='submit self-center capitalize'>
          register
        </button>
      </form>
    </div>
  );
};

export default SignUp;
