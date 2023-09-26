import Input from '../../components/forms/Input';
import { useForm } from 'react-hook-form';
import { useState } from 'react';
import Button from '../../components/Button';
import { toast } from 'react-toastify';
import { baseUrl } from '../../consts';
import useAuthState from '../../hooks/useAuth';
import { MoonLoader } from 'react-spinners';
import { Navigate, useNavigate } from 'react-router-dom';

const LogIn = () => {
  const [isLoading, setIsLoading] = useState(false);
  const navigate = useNavigate();

  const { setUser, user } = useAuthState();
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm({
    defaultValues: {
      email: '',
      password: '',
    },
  });

  const onSubmit = async (data) => {
    try {
      setIsLoading(true);
      const response = await fetch(`${baseUrl}auth/sign_in/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      });
      const res = await response.json();
      if (response.ok) {
        localStorage.setItem('auth', JSON.stringify(res));
        const user = res.data;
        setUser(user);
        toast.success('signed in!');
        navigate(`/dashboard/${user.role.toLowerCase()}`);
      } else {
        console.log('error');
        toast.error(res.detail);
      }
    } catch (error) {
      console.log(error);
      toast.error(error.detail);
    } finally {
      setIsLoading(false);
    }
  };

  if (user) return <Navigate to={`/dashboard/${user.role}`} replace />;

  return (
    <div className='flex flex-col justify-center items-center gap-6 w-full  my-8 bg-[url("../src/assets/girl.png")] py-20 bg-contain bg-no-repeat bg-right-bottom relative'>
      <form
        onSubmit={handleSubmit(onSubmit)}
        className={`${
          isLoading ? 'opacity-50' : ''
        } md:w-1/4 flex flex-col bg-form px-4 py-4 rounded-md`}
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
          type={'password'}
        />
        <Button
          type='submit'
          className='bg-btn w-1/2 rounded-2xl py-2 self-center'
        >
          login
        </Button>
      </form>

      {isLoading && (
        <div className='fixed'>
          <MoonLoader color='#000' className='z-20' width={500} />
        </div>
      )}
    </div>
  );
};

export default LogIn;
