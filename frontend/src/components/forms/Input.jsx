import PropTypes from 'prop-types';

const Input = (props) => {
  const {
    name,
    type = 'text',
    label,
    error,
    register,
    options = {},
    ...others
  } = props;

  return (
    <label
      htmlFor={name}
      className='block capitalize text-lg text-custom-green-100 pb-3'
    >
      {label}
      <input
        type={type}
        name={name}
        id={name}
        {...register(name, options)}
        {...others}
      />
      {error && (
        <p className='text-red-500 text-xs pt-1 normal-case italic'>
          {error?.message}
        </p>
      )}
    </label>
  );
};

Input.propTypes = {
  name: PropTypes.string.isRequired,
  type: PropTypes.string,
  error: PropTypes.object,
  label: PropTypes.string,
  register: PropTypes.func,
  options: PropTypes.object,
};

export default Input;