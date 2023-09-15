import Input from '../forms/Input';
import { useForm } from 'react-hook-form';
import { useState } from 'react';

const SchoolDetails = () => {
  const [image, setImage] = useState('');
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
      setImage(reader.result.toString());
    };
    return reader.readAsDataURL(file);
  };

  const onSubmit = (data) => {
    convertFile(data.files[0]);
    reset();
  };

  return (
    <>
      <h2>School details</h2>
      <div>
        <div></div>
        <form onSubmit={handleSubmit(onSubmit)}>
          <Input
            name='schoolName'
            register={register}
            className={
              'border w-full invalid:border-red-500 focus:outline-none py-base px-sm'
            }
            error={errors.schoolName}
            label={'school name'}
            options={{
              required: 'please provide school name',
            }}
            placeholder={'enter name of school'}
          />
          {image && <img src={image} />}
          <Input
            name='files'
            register={register}
            className={
              'border w-full invalid:border-red-500 focus:outline-none'
            }
            error={errors.files}
            label={'school logo'}
            options={{
              required: true,
            }}
            type={'file'}
          />
          {/* <Input
          name='email'
          register={register}
          className={'border w-full'}
          error={errors.email?.message}
          label={'email'}
          options={{
            required: '',
            pattern: {
              value: /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}$/i,
              message: 'enter a valid email',
            },
          }}
        /> */}
          <button type='submit'>ok</button>
        </form>
      </div>
    </>
  );
};

export default SchoolDetails;
