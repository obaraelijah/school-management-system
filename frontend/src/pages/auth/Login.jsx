import Input from '../../components/forms/Input';
import { useForm } from 'react-hook-form';
//import { useState } from 'react';
import img from '../../assets/books.webp';
import { NavLink } from 'react-router-dom';
import Button from '../../components/Button';

const LogIn = () => {
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
    <>
      <h2 className='pb-4 md:text-xl text-center'>Welcome to smartEdConnect</h2>
      <div className='grid grid-cols-2 gap-6 w-full'>
        <div className='col-span-1'>
          <img src={img} alt='' className='w-full h-full rounded-lg' />
        </div>
        <div className='w-full col-span-1 px-10'>
          <div className='capitalize flex justify-between items-center bg-light-btn text-white w-2/3 mx-auto p-3 text-center rounded-3xl mb-10'>
            <NavLink to={'/login'} className={'bg-btn w-1/2 rounded-2xl py-2'}>
              login
            </NavLink>
            <NavLink to={'/signup'} className={'w-1/2'}>
              register
            </NavLink>
          </div>
          <form
            onSubmit={handleSubmit(onSubmit)}
            className='w-full flex flex-col'
          >
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
              placeholder={'enter your email'}
            />

            <Input
              name='password'
              register={register}
              className={'input'}
              error={errors.password}
              label={'password'}
              options={{
                required: 'please input your password',
              }}
              placeholder={'enter your password'}
            />
            <Button
              type='submit'
              className='bg-btn w-1/2 rounded-2xl py-2 self-center'
            >
              login
            </Button>
          </form>
          <p className='mt-4 text-center'>
            <NavLink to={'/forgot-password'} className='text-blue-500 hover:underline'>
              Forgot Password?
            </NavLink>
          </p>
        </div>
      </div>
    </>
  );
};

export default LogIn;
