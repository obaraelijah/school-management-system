import school from '../../../assets/image6.png';
import Button from '../../../components/Button';

const Hero = () => {
  return (
    <div className='lg:py-10 bg-btn flex flex-col md:flex-row  items-center relative mask'>
      <div className='md:w-1/2 px-10 md:p-16'>
        <h1 className='text-2xl font-bold md:text-4xl mb-5 lg:text-5xl text-cm-orange-100'>
          Empowering Schools with Innovative Management
        </h1>
        <p className=''>
          Uncover the ultimate solution for effortless school management.
          Whether it&#39;s efficient class scheduling or precise attendance
          tracking, we&#39;ve got every aspect of school management expertly
          covered.
        </p>
        <Button
          className={
            'bg-light rounded-3xl w-2/3 py-2 capitalize  text-2xl my-5'
          }
        >
          get started
        </Button>
      </div>

      <div className='md:w-1/2 px-10 md:px-16'>
        <img
          src={school}
          alt=''
          className='w-full rounded-full md:rounded-e-full -rotate-3 shadow-hero md:rounded-s-none'
        />
      </div>
    </div>
  );
};

export default Hero;
