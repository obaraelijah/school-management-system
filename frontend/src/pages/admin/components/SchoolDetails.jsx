import Input from '../../../components/forms/Input';
import { useForm } from 'react-hook-form';
import { useState } from 'react';
import authRequest from '../../../config/requests';
import { toast } from 'react-toastify';
import Button from '../../../components/Button';

const SchoolDetails = () => {
  const [image, setImage] = useState('');
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm({
    defaultValues: {
      school_name: '',
      school_address: '',
      school_email: '',
      school_logo: '',
      school_phone_number: '',
      school_city: '',
      school_country: '',
      school_state: '',
      school_postal_code: '',
    },
  });

  const convertFile = (file) => {
    const reader = new FileReader();

    reader.onloadend = () => {
      setImage(reader.result.toString());
    };
    return reader.readAsDataURL(file);
  };

  const onSubmit = async (data) => {
    convertFile(data.school_logo[0]);
    const logo = data.school_logo[0];

    const formData = new FormData();
    formData.append('school_logo', logo);
    formData.append('school_name', data.school_name);
    formData.append('school_address', data.school_address);
    formData.append('school_city', data.school_city);
    formData.append('school_email', data.school_email);
    formData.append('school_phone_number', data.school_phone_number);
    formData.append('school_postal_code', data.school_postal_code);
    formData.append('school_country', data.school_country);
    formData.append('school_state', data.school_state);

    try {
      const res = await authRequest.post('schools/', formData);
      console.log(res);
      if (res.status === 201) {
        const data = res.data;
        console.log(data);
      } else {
        toast.error('error creating school');
      }
    } catch (error) {
      console.log(error);
      toast.error(error.detail);
    }
  };

  return (
    <>
      <h2 className='text-2xl font-medium pb-3'>New school</h2>
      <div>
        <form onSubmit={handleSubmit(onSubmit)} className='w-full'>
          <div className={'md:flex gap-3 w-full'}>
            <Input
              name='school_name'
              register={register}
              className={'input'}
              error={errors.school_name}
              label={'school name'}
              options={{
                required: 'please provide school name',
              }}
              placeholder={'enter name of school'}
            />

            <Input
              name='school_email'
              register={register}
              className={'border input'}
              error={errors.school_email}
              label={'email'}
              options={{
                required: '',
                pattern: {
                  value: /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}$/i,
                  message: 'enter a valid email',
                },
              }}
              type={'email'}
              placeholder={'enter school email'}
            />
          </div>
          {image && <img src={image} />}
          <Input
            name='school_logo'
            register={register}
            className={'border ml-3 invalid:border-red-500 focus:outline-none'}
            error={errors.school_logo}
            label={'school logo'}
            options={{
              required: true,
            }}
            type={'file'}
          />

          <Input
            name='school_address'
            register={register}
            className={'border input'}
            error={errors.school_address}
            label={'school address'}
            options={{
              required: 'please provide school address',
            }}
            placeholder={'enter address'}
          />

          <div className={'md:flex gap-3'}>
            <Input
              name='school_country'
              register={register}
              className={'input'}
              error={errors.school_country}
              label={'school country'}
              options={{
                required: 'please provide school country',
              }}
              placeholder={'country'}
            />

            <Input
              name='school_city'
              register={register}
              className={'input'}
              error={errors.school_city}
              label={'school city'}
              options={{
                required: 'please provide school city',
              }}
              placeholder={'city'}
            />

            <Input
              name='school_state'
              register={register}
              className={'input'}
              error={errors.school_state}
              label={'school state'}
              options={{
                required: 'please provide school state',
              }}
              placeholder={'enter state'}
            />
          </div>

          <div className={'md:flex gap-3'}>
            <Input
              name='school_phone_number'
              register={register}
              className={'input'}
              error={errors.school_phone_number}
              label={'school phone number'}
              options={{
                required: 'please provide school phone number',
              }}
              placeholder={'phone number'}
            />

            <Input
              name='school_postal_code'
              register={register}
              className={'input'}
              error={errors.school_postal_code}
              label={'school school_postal_code'}
              options={{
                required: 'please provide school postal code',
              }}
              placeholder={'postal code'}
            />
          </div>
          <Button
            type='submit'
            className='px-5 bg-cm-orange-100 text-white py-2 rounded-lg text-xl'
          >
            register school
          </Button>
        </form>
      </div>
    </>
  );
};

export default SchoolDetails;
