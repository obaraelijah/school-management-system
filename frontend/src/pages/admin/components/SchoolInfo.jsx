import Input from '../../../components/forms/Input';
import { useForm } from 'react-hook-form';
//import { useState } from 'react';
import img from '../../../assets/wall.webp';

const SchoolInfo = () => {
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
      <h2 className='py-3 md:text-xl'>New school details</h2>
      <div className='grid grid-cols-3 gap-6 w-full'>
        <div>
          <img src={img} alt='' className='col-span-1 h-screen rounded-lg' />
        </div>
        <form onSubmit={handleSubmit(onSubmit)} className='w-full col-span-2'>
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
          {/* {image && <img src={image} />} */}

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
          <button type='submit' className='submit'>
            Add
          </button>
        </form>
      </div>
    </>
  );
};

export default SchoolInfo;
