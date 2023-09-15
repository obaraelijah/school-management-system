import Input from '../../components/forms/Input';
import { useForm } from 'react-hook-form';
//import { useState } from 'react';
import img from '../../assets/books.webp';
import { NavLink } from 'react-router-dom';

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
    <>
      <h2 className='pb-8 md:text-xl text-center'>welcome to smartEdConnect</h2>
      <div className='grid grid-cols-2 gap-6 w-full'>
        <div className='col-span-1'>
          <img src={img} alt='' className='h-full w-full rounded-lg' />
        </div>

        <div className='w-full col-span-1 px-10'>
          <div className='capitalize flex justify-between items-center bg-light-btn text-white w-2/3 mx-auto p-3 text-center rounded-3xl mb-10'>
            <NavLink to={'/login'} className={'w-1/2'}>
              login
            </NavLink>
            <NavLink to={'/signup'} className={'bg-btn w-1/2 rounded-2xl py-2'}>
              register
            </NavLink>
          </div>

          <form
            onSubmit={handleSubmit(onSubmit)}
            className='w-full col-span-2 flex flex-col'
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
            <button type='submit' className='submit self-center'>
              Add
            </button>
          </form>
        </div>
      </div>
    </>
  );
};

export default SignUp;
