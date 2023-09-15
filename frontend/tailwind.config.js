/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{html,js,jsx}'],
  theme: {
    extend: {
      colors: {
        'custom-green': {
          100: '#2071B2',
        },
        header: '#001C27',
        btn: '#49BBBD',
        'light-btn': 'rgba(73, 187, 189, 0.60)',
      },
      backgroundColor: {
        'custom-green': {
          100: '#2071B2',
        },
        header: '#001C27',
        btn: '#49BBBD',
        light: 'rgba(255, 255, 255, 0.30)',
      },
      padding: {
        sm: '0.625rem',
        base: '0.9375rem',
      },
    },
  },
  plugins: [],
};
